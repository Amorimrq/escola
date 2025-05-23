matriz = [
    ['-', '-', '-' ],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end=' ')
        print('')
print_(matriz)

def check_winner(matriz, player):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == player or \
           matriz[0][i] == matriz[1][i] == matriz[2][i] == player:
            return True
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == player or \
       matriz[0][2] == matriz[1][1] == matriz[2][0] == player:
        return True
    return False

player = 'X'
while True:
    print('Jogador', player, 'escolha uma posição:')
    lin_input = input('Linha: ')
    col_input = input('Coluna: ')
    
    if lin_input == '' or col_input == '':
        print('Posição inválida. Tente novamente.')
        continue
    
    lin = int(lin_input)
    col = int(col_input)
    
    if lin < 0 or lin > 2 or col < 0 or col > 2:
        print('Posição inválida. Tente novamente.')
        continue
    if matriz[lin][col] != '-':
        print('Posição já preenchida. Tente novamente.')
        continue
    matriz[lin][col] = player
    print_(matriz)
    if check_winner(matriz, player):
        print('Jogador', player, 'venceu!')
        break
    if all(all(cell != '-' for cell in row) for row in matriz):
        print('Empate!')
        break
    player = 'O' if player == 'X' else 'X'
    print('')
