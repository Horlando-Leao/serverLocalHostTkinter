from tkinter import*
janela = Tk()

#função ler arquivo.
ler = open("python-severInLocal\src\Teste.txt", "r") #o arquivo deve existir e estar na mesma pasta do progrma pra poder executar. 
x = ler.read()

cs = Scrollbar (janela)
cs.pack(side=RIGHT, fill=Y)
texto = Text (janela, font="Arial 12")
texto.pack(expand=YES, fill=BOTH)
texto.insert(0.0, x) #inserindo a leitura do arquivo dentro do Text. 
#aqui configuramos o scrolbar no elemento Text. 
texto.config (yscrollcommand=cs.set)
cs.config (command=texto.yview)

janela.mainloop()