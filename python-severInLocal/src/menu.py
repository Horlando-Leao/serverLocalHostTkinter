from tkinter import *
from server import chamadasServidor


def Janela():

    janela_1 = Tk()
    janela_1.geometry('600x600')
    janela_1.title('    SERVIDOR LOCAL PYTHON')
    janela_1.configure()
    
    botao1 = Button(janela_1, width=7, text='START',bg='green' ,command = lambda:chamadasServidor('abrir') )
    botao1.place(x=230, y=20)
    
    botao2 = Button(janela_1, width=7, text='STOP',bg='red', command = lambda:chamadasServidor('fechar') )
    botao2.place(x=300, y=20)
    
    rotulo1 = Label(janela_1, text="dados a ser exibidos", font= "Arial 14")
    rotulo1.place(x=70, y=65)
    
    janela_1.mainloop()

Janela()

        
