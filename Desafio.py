#Samuel / Roberto / Pedro / Felipe / Caio Oliveira / Caio Antonio
import argparse
from PIL import Image
import os

# Lista vazia de tarefas
listaTarefas = []
tarefas_concluidas = []

# Utilize loops (for e/ou while) para apresentar um menu de opções ao usuário e realizar operações repetidas.
while True:
    print("\n-------------Sistema de gerenciamento de tarefas-------------")
    print("1- Adicionar Tarefa")
    print("2- Listar Tarefas Pendentes")
    print("3- Editar Tarefa")
    print("4- Marcar Tarefa como Concluída")
    print("5- Listar Tarefas Concluídas")
    print("6- Remover Tarefa")
    print("7- EXODIA")
    print("0- Sair")

    # Pegar a opção do usuário.
    opcao = input("Escolha: ")

    # 1. Adicionar Tarefa: Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
    if opcao == "1":
        print("\nOpções de entrega:")
        print("1- Entregar no mesmo dia")
        print("2- Entregar em 7 dias")
        print("3- Entregar em 15 dias")
        opcao_entrega = input("Escolha a opção de entrega: ")
        if opcao_entrega not in ["1", "2", "3"]:
            print("Opção de entrega inválida.")
            continue
        tarefa = input("Digite a tarefa a ser adicionada: ")
        listaTarefas.append((tarefa, opcao_entrega))
        print("Tarefa adicionada com sucesso!")

    # 2. Listar Tarefas Pendentes: Mostrar todas as tarefas pendentes na lista, enumerando-as.
    elif opcao == "2":
        print("\nTarefas pendentes:")
        for i, (tarefa, prazo) in enumerate(listaTarefas):
            if prazo == "1":
                prazo_descricao = "Entregar no mesmo dia"
            elif prazo == "2":
                prazo_descricao = "Entregar em 7 dias"
            else:
                prazo_descricao = "Entregar em 15 dias"
            print(f"{i+1} - {tarefa} (Prazo: {prazo_descricao})")
            
    # 3. Editar Tarefa: Permitir ao usuário editar uma tarefa pendente.
    elif opcao == "3":
        print("\nTarefas pendentes:")
        for i, (tarefa, prazo) in enumerate(listaTarefas):
            if prazo == "1":
                prazo_descricao = "Entregar no mesmo dia"
            elif prazo == "2":
                prazo_descricao = "Entregar em 7 dias"
            else:
                prazo_descricao = "Entregar em 15 dias"
            print(f"{i+1} - {tarefa} (Prazo: {prazo_descricao})")

        if len(listaTarefas) == 0:
            print("Não há tarefas pendentes para atualizar.")
        else:
            tarefa_atualizar = int(input("Digite o número da tarefa a atualizar: "))
            if tarefa_atualizar <= len(listaTarefas) and tarefa_atualizar > 0:
                nova_descricao = input("Digite a nova descrição da tarefa: ")
                listaTarefas[tarefa_atualizar - 1] = (nova_descricao, listaTarefas[tarefa_atualizar - 1][1])
                print("\033[1mTarefa atualizada com sucesso!\033[0m")
            else:
                print("\033[1mNúmero de tarefa inválido.\033[0m")
    
    # 4. Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída.
    elif opcao == "4":
        print("\nTarefas pendentes:")
        for i, (tarefa, prazo) in enumerate(listaTarefas):
            if prazo == "1":
                prazo_descricao = "Entregar no mesmo dia"
            elif prazo == "2":
                prazo_descricao = "Entregar em 7 dias"
            else:
                prazo_descricao = "Entregar em 15 dias"
            print(f"{i+1} - {tarefa} (Prazo: {prazo_descricao})")

        if len(listaTarefas) == 0:
            print("Não há tarefas pendentes para marcar como concluídas.")
        else:
            tarefa_concluida = int(input("Digite o número da tarefa concluída: "))
            if tarefa_concluida <= len(listaTarefas) and tarefa_concluida > 0:
                tarefa, entrega = listaTarefas.pop(tarefa_concluida - 1)
                tarefas_concluidas.append((tarefa, entrega))
                print("Tarefa marcada como concluída!")
            else:
                print("Número de tarefa inválido.")

    # 5. Listar Tarefas Concluídas: Mostrar todas as tarefas concluídas na lista, enumerando-as.
    elif opcao == "5":
        print("\nTarefas concluídas:")
        for i, (tarefa, _) in enumerate(tarefas_concluidas):
            print(f"{i+1} - {tarefa}")

    # 6. Remover Tarefa: Dar ao usuário a opção de remover uma tarefa da lista.
    elif opcao == "6":
        print("\nTarefas pendentes:")
        for i, (tarefa, prazo) in enumerate(listaTarefas):
            if prazo == "1":
                prazo_descricao = "Entregar no mesmo dia"
            elif prazo == "2":
                prazo_descricao = "Entregar em 7 dias"
            else:
                prazo_descricao = "Entregar em 15 dias"
            print(f"{i+1} - {tarefa} (Prazo: {prazo_descricao})")

        if len(listaTarefas) == 0:
            print("Não há tarefas pendentes para remover.")
        else:
            tarefa_remover = int(input("Digite o número da tarefa a remover: "))
            if tarefa_remover <= len(listaTarefas) and tarefa_remover > 0:
                tarefa, _ = listaTarefas.pop(tarefa_remover - 1)
                print(f"Tarefa '{tarefa}' removida com sucesso!")
            else:
                print("Número de tarefa inválido.")
    
    # 7. EXODIA: Exibir uma imagem.
    elif opcao == "7":
        exodia_image_path = "EXODIA/FELPO.jpg"
        try:
            exodia_image = Image.open(exodia_image_path)
            exodia_image.show()
        except FileNotFoundError:
            print("Erro: Imagem não encontrada.")
    
    # 0. Sair: Encerrar o programa.
    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
