tarefas = []
opcao1 = "1 Adicionar tarefa"
opcao2 = "2 Ver tarefas"
opcao3 = "3 remover tarefa"

nome = input("Digite o titulo da pagina: ")
print(f"{nome.upper()}")

while True :
    print(opcao1)
    print(opcao2)
    print(opcao3)

    resposta = int(input("escolha uma das opcoes: "))

    if resposta == 1:
        print(f"Escolha: {resposta}")
        adicionar = input("Digite a tarefa: ")
        tarefas.append(adicionar)
        print("Tarefa adicionada!")

    if resposta == 2:
        print(f"Escolha: {resposta}")
        if len(tarefas) == 0:
            print("Nenhuma tarefa ainda!")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

    if resposta == 3:
        print(f"Escolha: {resposta}")
        for i, tarefa in enumerate(tarefas, 1):
                print(f"seus itens: {i}-{tarefa}")
        if len(tarefas) > 0:
            remover = int(input("Qual tarefa quer remover? "))
            tarefas.pop(remover - 1)
            print("Tarefa removida!")
        else:
            print("Nenhuma tarefa para remover!")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
            print("Encerrando...")
            break
