import sqlite3 as lite

class DadosCliente():
    def __init__(self, userName, userEmail, userPassword, userSaldo):
        self.userName = userName
        self.userEmail = userEmail
        self.userPassword = userPassword
        self.userSaldo = userSaldo
    def GetInfo():
    
        DadosCliente.userName = input("Qual o seu Nome?\n ")
        DadosCliente.userEmail = input("Qual será seu email para registro?\n ")
        DadosCliente.userPassword = input("Qual será sua senha? \n ")
        DadosCliente.userSaldo = 0

        banco = lite.connect("User_Database.db")

        cursor = banco.cursor()
        with banco:
            cursor.execute("INSERT OR IGNORE INTO UseData (name, email, psk, saldo) VALUES('"+DadosCliente.userName+"','"+DadosCliente.userEmail+"','"+DadosCliente.userPassword+"','"+str(DadosCliente.userSaldo)+"')")

            banco.commit()
        