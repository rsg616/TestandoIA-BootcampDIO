# Jogo da Velha em Python

def criar_tabuleiro():
    return [" " for _ in range(9)]

def mostrar_tabuleiro(tabuleiro):
    print()
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print()

def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8), # linhas
        (0,3,6), (1,4,7), (2,5,8), # colunas
        (0,4,8), (2,4,6)           # diagonais
    ]
    for comb in combinacoes:
        if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    return " " not in tabuleiro

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)
        try:
            movimento = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[movimento] != " ":
                print("Essa posição já está ocupada. Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Movimento inválido. Escolha um número de 1 a 9.")
            continue

        tabuleiro[movimento] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()
