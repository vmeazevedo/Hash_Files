#Importa as bilbiotecas necessárias
from tkinter import *
from tkinter import filedialog
import hashlib
 
#Cria e configura a janela principal do programa
root = Tk()
root.title("Hash de Arquivos")
root.resizable(False, False)
root.geometry("565x220+433+234")
 
#Variáveis para que os objetos tipo tkinter.Entry recebam seu conteúdo
stringArquivo = StringVar()
stringMD5 = StringVar()
stringSHA1 = StringVar()
stringSHA224 = StringVar()
stringSHA256 = StringVar()
stringSHA384 = StringVar()
stringSHA512 = StringVar()
 
#Função para escolher o arquivo e gerar os hashes dele
def hashArquivo():
    caminho = filedialog.askopenfilename()
    stringArquivo.set(caminho)
    arquivo = open(caminho, 'rb')
 
    bufferSize = 65536      #Para usar na função uptade
 
    # Apenas declara os objetos dos tipos de hash
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha224 = hashlib.sha224()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()
 
    # Atualiza todos os hashes ao mesmo tempo, senão necessitaríamos retornar o ponteiro do arquivo
    while True:  # Laço para ler os bytes do arquivo e atualizar os hashes
        data = arquivo.read(bufferSize)  # Lê do arquivo a quantidade de bytes determinada
        if not data:  # Se não houver mais dados a serem lidos ele sai do laço
            break
        md5.update(data)  # Atualiza os hashes
        sha1.update(data)
        sha224.update(data)
        sha256.update(data)
        sha384.update(data)
        sha512.update(data)
 
    #Escreve o resultado nos objeto do tipo tkinter.
    stringMD5.set(md5.hexdigest())
    stringSHA1.set(sha1.hexdigest())
    stringSHA224.set(sha224.hexdigest())
    stringSHA256.set(sha256.hexdigest())
    stringSHA384.set(sha384.hexdigest())
    stringSHA512.set(sha512.hexdigest())
 
    arquivo.close()     #Fecha o arquivo
 
#Cria e configura os objetos do tipo tkinter.Label
lb1 = Label(root, text="Arquivo").place(x=5, y=5)
lb2 = Label(root, text="MD5").place(x=5, y=35)
lb3 = Label(root, text="SHA1").place(x=5, y=65)
lb4 = Label(root, text="SHA224").place(x=5, y=95)
lb5 = Label(root, text="SHA256").place(x=5, y=125)
lb6 = Label(root, text="SHA384").place(x=5, y=155)
lb7 = Label(root, text="SHA512").place(x=5, y=185)
 
#Cria e configura os objetos do tipo tkinter.Entry
et1 = Entry(root, width=65, textvariable=stringArquivo).place(x=55, y=5)
et2 = Entry(root, width=65, textvariable=stringMD5).place(x=55, y=35)
et3 = Entry(root, width=65, textvariable=stringSHA1).place(x=55, y=65)
et4 = Entry(root, width=65, textvariable=stringSHA224).place(x=55, y=95)
et5 = Entry(root, width=65, textvariable=stringSHA256).place(x=55, y=125)
et6 = Entry(root, width=65, textvariable=stringSHA384).place(x=55, y=155)
et7 = Entry(root, width=65, textvariable=stringSHA512).place(x=55, y=185)
 
#Cria e configura o objeto do tipo tkinter.Button
bt1 = Button(root, text="Escolher arquivo", height=2, command=hashArquivo).place(x=460, y=5)
 
#mainloop() serve para abrir a janela do programa e "ouvir" o que seus componentes fazem
root.mainloop()