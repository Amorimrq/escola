import random
from time import sleep
lista_golpes =("pedra", 'papel', 'tesoura')
print("PEDRA PAPEL TESOURA")
computador = random.choice(lista_golpes)
print("Computador escolhendo")
escolha = input("Sua escolha: ")

if escolha == computador:   
    print("Empate") 
elif escolha == 'papel' and computador =='tesoura':
    print("Você perdeu")
elif escolha == 'tesoura' and computador == 'pedra':
     print("Você perdeu")
elif escolha == 'pedra' and computador == 'papel':
    print("Você perdeu")
elif escolha == "papel" and computador == 'pedra':
    print("Você ganhou")
elif escolha == 'tesoura' and computador == 'papel':
    print("Você ganhou")  
elif escolha == 'pedra' and computador == 'tesoura':
    print("Você ganhou")  
