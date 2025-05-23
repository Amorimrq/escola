matriz = [
    ['-', '-', '-' ],
    ['-', '-', '-'],
    ['-', '-', '-']
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna], end=' ')
    print('')
    
while True:
    print('Escolha uma posição:')
    lin = int(input('Linha: '))
    col = int(input('Coluna: '))
    matriz[lin][col] = 'X'
    matriz[lin][col] = 'O'
    for linha in matriz:
        for i in matriz:
            print(i, end=' ')
    print('')