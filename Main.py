import sqlite3 as lite

banco = lite.connect("User_Database.db")
with banco:
    cursor = banco.cursor()
    #cursor.execute("CREATE TABLE UseData(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, psk TEXT, saldo REAL)")



print("Bem vindo ao MathBank!\n O que gostaria de fazer? ")

answer = input("[L]ogin [R]egistrar [S]air\n")

##Escolha do usuário entre Logar, Registrar e Sair

if answer == "L":
    print("Você escolheu Logar")
    import Modulo_Login
    Modulo_Login
    
elif answer == "R":
    import Modulo_Registro
    print("Você escolheu Registrar")
    Modulo_Registro.DadosCliente.GetInfo()
else:
    print("Você escolhu Sair")
    import Main
    Main
