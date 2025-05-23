from random import choice, randint
from time import sleep
golpes= ['Soco', 'chute', 'voadora']
j1 = 100
j2 = 100
nome1 = input("Digite o nome do seu lutador:  ")
nome2 = input("Digite o nome do outro lutador: ")
print(1)
sleep(1)
print(2)
sleep(1)
print(3)
sleep(1)
print("LUTEM!!!!!")
while j1 > 0 and j2 > 0 :
    escolha = choice(golpes)
    print(f'O lutador {nome1} deu um {escolha} em {nome2}')
    dano = j1 - randint(1,50)
    print("="*30)
    dano2 = j2 - randint(1,50)
    print(f'O lutador {nome2} deu um {escolha} em {nome1}')
    print("="*30)
    
    if j1 < 0 :
       print(f"O lutador {nome2} Ganhou")
    elif j2 < 0:
        print(f'O lutador {nome1} Ganhou')
    
    
