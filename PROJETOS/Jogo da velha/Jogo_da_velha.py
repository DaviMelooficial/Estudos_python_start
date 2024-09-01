import random
import os

class velha:
    def __init__(self):
        self.reset_board()
    
    # Printar todo o tabuleiro
    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    # Definindo a matriz que vai guardar as jogadas 
    def reset_board(self):
        self.board =[[" "," "," "],[" "," "," "],[" "," "," "]]
        self.done = " "

    # Função que verifica se houve uma vitória, derrota ou empate
    # Deve haver um jeito mais fácil de fazer e com menos código, mas foi isso que saiu
    def check(self):
        dict_vitoria = {}

        for i in ["X", "O"]:
            #Horizontal
            dict_vitoria[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_vitoria[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_vitoria[i]
            dict_vitoria[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_vitoria[i]

            #Verticais
            dict_vitoria[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_vitoria[i]
            dict_vitoria[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_vitoria[i]
            dict_vitoria[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_vitoria[i]

            #Diagonais
            dict_vitoria[i] = (self.board[0][0] == self.board[1][2] == self.board[2][2] == i) or dict_vitoria[i]
            dict_vitoria[i] = (self.board[0][2] == self.board[1][1] == self.board[2][0] == i) or dict_vitoria[i]

        if dict_vitoria["X"]:
            self.done = "X"
            print("X venceu!")
        elif dict_vitoria["O"]:
            self.done = "O"
            print("O venceu!")

        c = 0

        # Iteração para verificar o empate caso todos os campos tenham sido preenchidos
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c += 1
                    break
        if c == 9: # 9 é o número de posições no tabuleiro
            self.done = "d"
            print("Empate!")
            return

    # Recebe os movimentos do jogador
    def get_jogador_move(self):
        movimento_invalido = True
        
        # Laço de repetição que usei para caso o úsuario digite uma opção inválida
        while movimento_invalido:
            try:
                print("Digite a linha da sua jogada:")
                x = int(input())

                print("Escolha a coluna do seu movimento:")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Opção inválida!")

                if self.board[x][y] != " ":
                    print("Posição já preenchida!")
                    continue
            except Exception as e:
                print(e)
                continue

            movimento_invalido = False
        self.board[x][y] = "X" # altera a posição dentro da matriz para X

    # Faz a jogada da máquina de forma aleatória
    def make_move(self):
        movimentos_computador = []
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    movimentos_computador.append((i, j))
            
        if len(movimentos_computador) > 0:
            x, y = random.choice(movimentos_computador)
            self.board[x][y] = "O"

velha = velha()
velha.print_board()
next = 0

# Laço de repetição para que o jogo seja executado até que o valor de next mude
while next == 0:
    os.system("cls")
    velha.print_board()
    while velha.done == " ":
        velha.get_jogador_move()
        velha.make_move()
        os.system("cls")
        velha.print_board()
        velha.check()
    
    print("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.")
    next = int(input())
    
    if next == 1:
        break
    else:
        velha.reset_board()
        next = 0




