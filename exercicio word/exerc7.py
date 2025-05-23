#Login Simples* Crie um programa que peça um nome de usuário e uma senha. 
# Caso o usuário digite "admin" como nome e "1234" como senha, exiba "Login bem-sucedido". Caso contrário, exiba "Usuário ou senha incorretos". 

senha = 1234
nome = input("Seu nome: ")
sen = int(input("Qual a sua senha"))
nom = 'admin'
if senha == 1234 and nome == nom:
    print("login bem sucedido")
else:
    print("Usuario ou senha incorreto")