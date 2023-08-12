import random

opcoes = ["Pedra", "Papel", "Tesoura"]

escolha_usuario = input("Digite 1 para Pedra, 2 para Papel e 3 para Tesoura: ")

escolha_pc = random.choice(opcoes)

print(f"Você escolheu {escolha_usuario} e o PC {escolha_pc}. Assim:")


def confere_vencedor(escolha_usuario, escolha_pc):
    if (escolha_usuario == "Pedra" and escolha_pc == "Tesoura") or (escolha_usuario == "Papel" and escolha_pc == "Pedra") or (escolha_usuario == "Tesoura" and escolha_pc == "Papel"):
        print("Você ganhou")
    elif escolha_pc == escolha_usuario:
        print("Jogo empatou")
    else:
        print("PC ganhou")


confere_vencedor(escolha_usuario, escolha_pc)
