#Nota e Conceito* Faça um programa que receba uma nota de 0 a 10 e classifique-a conforme a seguinte tabela: 
# A se a nota for 9 ou 10 B se for 7 ou 8 C se for 5 ou 6 D se for 3 ou 4 F se for menor que 3.
n = int(input("Diga sua nota: "))
if n == 9 or n == 10:
    print("A")
elif n == 8 or n == 7:
    print("B")
elif n == 5 or n == 6:
    print("C")
elif n == 3 or n == 4:
    print("D")
elif n <= 3:
    print("F")