from time import sleep
#2. Par ou Ímpar* Crie um programa que solicite um número ao usuário e informe se ele é par ou ímpar. 
print("Par ou Impar")
number = int(input("Diga um numero?"))
sleep (1)
if number % 2:
    print("numero impar")
else :
    print("numero par")