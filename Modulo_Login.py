import sqlite3 as DB

banco = DB.connect('User_Database.db')
cursor = banco.cursor()

class Login ():
        

                userChoice = input("Deseja utilizar seu Nome ou Email para login\n")
                if userChoice == "Nome":
                        TextNome = input("Digite seu Nome\n")
                        try:
                                cursor.execute("SELECT psk FROM UseData WHERE name = '{}'".format(TextNome))
                                userSenha = cursor.fetchall()
                        except:
                                print("Erro, Nome de usuario nao cadastrado")

                        senha = input("Agora, digite sua senha: \n")
                        if senha == userSenha[0][0]:
                                print("Voce esta logado")
                        else: 
                                print("Nome/Email e(ou) senha incorretos")
                elif userChoice == "Email":
                        TextEmail = input("Digite seu Email\n")
                        try:
                                cursor.execute("SELECT psk FROM UseData WHERE email = '{}'".format(TextEmail))
                                userSenha = cursor.fetchall()
                        
                        except:
                                print("Erro, Email de usuario nao cadastrado")
                        senha = input("Agora, digite sua senha: \n")
                
                        if senha == userSenha[0][0]:
                                print(f"Bem vindo {TextEmail}")
                        else: 
                                print("Nome/Email e(ou) senha incorretos")
                else:
                        print("Erro, Nao foi selecionado nenhuma das opcoes dadas\n")
                        import Modulo_Login

def UserLogado (self, userChoice, TextEmail, TextNome):
        print({TextEmail})
        if userChoice == "Nome":
                cursor.execute("SELECT id FROM UseData WHERE name = '{}'".format(TextNome))
                cursor.fetchall()
        elif userChoice == "Email":
                cursor.execute("SELECT id FROM UseData WHERE email = '{}'".format(TextEmail))
                cursor.fetchall()   
