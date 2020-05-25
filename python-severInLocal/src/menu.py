from tkinter import *
from server import chamadasServidor


def Janela():
    #CARACTERICAS DA JANELA
    janela_1 = Tk()
    janela_1.geometry('600x600')
    janela_1.title('    SERVIDOR LOCAL PYTHON')
    janela_1.configure()


    def getDateDir(DIR):
        pass
    
    #lIGAR SERVIDOR
    botao1 = Button(janela_1, width=7, text='START',bg='green' ,command = lambda:chamadasServidor('abrir') )
    botao1.place(x=230, y=20)
    
    #DESLIGAR SERVIDOR
    botao2 = Button(janela_1, width=7, text='STOP',bg='red', command = lambda:chamadasServidor('fechar') )
    botao2.place(x=300, y=20)

    #INPUT DO CAMINHO DIR
    rotulo1 = Label(janela_1, text="Caminho do diretório", font= "Arial 14")
    rotulo1.place(x=70, y=65)

    caixa1 = Entry(janela_1)
    caixa1.place(x=176, y=100, width=200, height=25)
    
    botao3 = Button(janela_1, width=10, height=1 ,text='OK', command = lambda: getDateDir(caixa1.get()))
    botao3.place(x=75, y=100)

    #DADOS A SEREM EXIBIDO
    rotulo2 = Label(janela_1, text="dados a ser exibidos", font= "Arial 14")
    rotulo2.place(x=70, y=250)

    janela_1.mainloop()

Janela()

        
