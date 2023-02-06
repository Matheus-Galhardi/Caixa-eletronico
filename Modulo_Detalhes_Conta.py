import sqlite3 as lite
from Modulo_Login import Login
banco = lite.connect("User_Database.db")
cursor = banco.cursor()

class UserDetails():
    def __init__(self, userChoice, TextNome, TextEmail, userSenha):
        self.userChoice = userChoice
        self.TextNome = TextNome
        self.TextEmail = TextEmail
        self.userSenha = userSenha

    def AccountDetails(self, userChoice):
        userChoice = input("Escolha:")
        return userChoice

    def choice(self, userChoice, TextNome, TextEmail):
        if userChoice == "Nome":
            cursor.execute("SELECT id FROM UseData WHERE name = '{}'".format(TextNome))
            cursor.fetchall()

        elif userChoice == "Email":
            cursor.execute("SELECT id FROM UseData WHERE email = '{}'".format(TextEmail))
            cursor.fetchall()          
        
teste = UserDetails.AccountDetails
print(teste)

#if answer == "R":
   #QuantiaR = input("Quanto deseja retirar")
   #print(QuantiaR)
#elif answer == "D":
    #QuantiaD = input("Quanto deseja depositar")
    #print(QuantiaD)
#elif answer == "S":
#    print(saldo)
