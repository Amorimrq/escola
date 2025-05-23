#Triângulo Válido* Desenvolva um programa que receba três números inteiros representando os lados de um triângulo. O programa deve verificar se a 
#soma de dois lados é sempre maior que o terceiro e informar se os valores formam um triângulo válido. 

n1 = int(input("Diga a b e c respecivamente"))
n2 = int(input("Diga a b e c respecivamente"))
n3 = int(input("Diga a b e c respecivamente"))
soma = n1 + n2 
if soma > n3:
    print("Triangulo Valido")
else :
    print("Triangulo Invalido")
    

