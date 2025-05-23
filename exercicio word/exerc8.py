#Ano Bissexto* Elabore um programa que solicite um ano ao usuário e determine se ele é bissexto ou não. 
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400. 
ano = int(input("Diga um ano: "))
if ano /4 or ano != 100 :
    print("")
else :
    print("ano bissextoS")
