
def soma ():
    a = float(input("Diga um valor: "))
    b = float(input("Diga outro valor: "))
    s = a + b
    print(s)
    
def subtração ():
    a = float(input("Diga um valor: "))
    d = float(input("Diga outro valor: "))
    sub = a - d
    print (sub)

def multiplicação ():
    a = float(input("Diga um valor: "))
    b = float(input("Diga outro valor: "))
    m = a * b
    print(m)

def divisão ():
    a = float(input("Diga um valor: "))
    b = float(input("Diga outro valor: "))
    d = a / b
    print(d)

print("Vamos calcular?")
v = float(input("[1] SIM, [2]NÃO: "))
escolha = input("Qual a operação da conta?: ")
while v < 2:

    if escolha == 'soma':
        soma()
        print("Denovo?")
        v = float(input("[1] SIM, [2]NÃO: "))
    escolha = input("Qual a operação da conta?: ")
    if escolha == 'subtração':
        subtração()
        print("Denovo?")
        v = float(input("[1] SIM, [2]NÃO: "))
    escolha = input("Qual a operação da conta?: ")
    if escolha == 'multiplicação':
        multiplicação()
        print("Denovo?")
        v = float(input("[1] SIM, [2]NÃO: "))
    escolha = input("Qual a operação da conta?: ")
    if escolha == 'divisão':
        divisão()
        print("Denovo?")
        v = float(input("[1] SIM, [2]NÃO: "))
    if v == 2 :
        print("FINALIZADO")