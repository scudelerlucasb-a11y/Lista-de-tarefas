print("Jogo de pedra, papel e tesoura")
opcao1 = "1 - Pedra"
opcao2 = "2 - Papel"
opcao3 = "3 - Tesoura"
while True:

    print("escolha uma das opcoes:")
    print(opcao1)
    print(opcao2)
    print(opcao3)

    resposta = int(input("escolha uma das opcoes:"))

    if resposta == 1:
        print("sua escolha foi: pedra")
    if resposta == 2:
        print("sua escolha foi: papel")
    if resposta == 3:
        print("sua escolha foi: tesoura")

    import random
    opcoes = ["Pedra", "Papel", "Tesoura"]
    computador = random.choice(opcoes)
    print(f"Computador escolheu: {computador}")

    if resposta == 1:
        if computador == "Pedra":
            print("empate")
        elif computador == "Papel":
            print("computador ganhou")
        else :
            print("voce ganhou")

    if resposta == 2:
                if computador == "Papel":
                    print("empate")
                elif computador == "Tesoura":
                    print("computador ganhou")
                else :
                    print("voce ganhou")

    if resposta == 3:
        if computador == "Tesoura":
            print("empate")
        elif computador == "Pedra":
            print("computador ganhou")
        else :
            print("voce ganhou")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
        print("Encerrando...")
        break



