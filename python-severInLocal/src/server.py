from importes import *

#apagarConsole = os.system('cls')if(platform.system()=="Windows")else(os.system('clear'))
hoje = datetime.now()
data_atual = "{}/{}/{}".format(hoje.year, hoje.month, hoje.day)
hora_atual = "{}/{}".format(hoje.hour ,hoje.minute)
#global httpd
#httpd = False

def chamarServidor():
    PORT = int(os.getenv('PORT', 8000))#leia a porta selecionada do servidor do seu aplicativo
    global diretorioServidor
    diretorioServidor = os.chdir('./servicos') #alterar o diretório atual para evitar a exposição do arquivo de controle

    global httpd
    httpd = Server(("", PORT), Handler)

    try:
        #mostrar em tela
        print("Startando servidor na porta {0} - Data: {1} - Hora: {2}".format(PORT, data_atual, hora_atual))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Conexão fechada na porta {0} - Data: {1} - Hora: {2}".format(PORT, data_atual, hora_atual))
    except EnvironmentError as ambiente:
        print("Erro de ambiente ({})".format(ambiente))
    else:
        print('Que os jogos comecem...')
    httpd.server_close

def fecharServidor():
    httpd.server_close
    print("Conexão fechada na porta")
   

def chamadasServidor(escolha):
    servidorThread = Thread(target = chamarServidor)
    if escolha == 'abrir':
        servidorThread.start()
    elif escolha == 'fechar':
        servidorThread = Thread(target = fecharServidor)
        servidorThread.run()

        
   
        
        

   

