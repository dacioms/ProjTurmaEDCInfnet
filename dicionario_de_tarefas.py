# Lista de tarefas
tarefas = []
 
# Função para adicionar uma nova tarefa
def adicionar_tarefa(lista, id_tarefa, nome, descricao, data_inicio, data_conclusao, concluida):
    # Criando o dicionário de tarefa
    tarefa = {
        "id": id_tarefa,
        "nome": nome,
        "descricao": descricao,
        "data_inicio": data_inicio,
        "data_conclusao": data_conclusao,
        "concluida": concluida
    }
    # Adicionando a tarefa à lista especificada
    lista.append(tarefa)
 
# Função para exibir todas as tarefas de uma lista específica
def exibir_tarefas(lista = None, id_tarefa = None):
    # Se nenhuma lista for especificada, exibe todas as tarefas de todas as listas
    if lista is None:
        for tarefas_lista in tarefas:
            for tarefa in tarefas_lista:
                imprimir_tarefa(tarefa)
            print()
    else:
        # Se uma lista for especificada, exibe apenas as tarefas dessa lista
        for tarefa in lista:
            if id_tarefa is not None and tarefa['id'] == id_tarefa:
                imprimir_tarefa(tarefa)
                return
            elif id_tarefa is None:
                imprimir_tarefa(tarefa)
 
# Função para imprimir uma tarefa
def imprimir_tarefa(tarefa):
    print(f"ID: {tarefa['id']}")
    print(f"Nome: {tarefa['nome']}")
    print(f"Descrição: {tarefa['descricao']}")
    print(f"Data de Início: {tarefa['data_inicio']}")
    print(f"Data de Conclusão: {tarefa['data_conclusao']}")
    print(f"Concluída: {'Sim' if tarefa['concluida'] else 'Não'}")
    print()
 
# Adicionar algumas tarefas de exemplo
adicionar_tarefa(tarefas, 1, "Fazer compras", "Comprar comida e produtos de limpeza", "2024-03-14", "2024-03-15", True)
adicionar_tarefa(tarefas, 2, "Estudar Python", "Estudar programação em Python", "2024-03-14", "2024-03-21", True)
adicionar_tarefa(tarefas, 3, "Fazer exercícios", "Fazer exercícios físicos", "2024-03-15", "2024-03-15", False)
 
# Exibir todas as tarefas de todas as listas
exibir_tarefas(tarefas)
 
# Exibir apenas a tarefa com ID 1 da lista 'lista2'
exibir_tarefas(tarefas, 1)
