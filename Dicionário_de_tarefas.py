from csv import writer

# Lista de tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa(id_tarefa, nome, descricao, data_inicio, data_conclusao, concluida):
    tarefa = {
        "id": id_tarefa,
        "nome": nome,
        "descricao": descricao,
        "data_inicio": data_inicio,
        "data_conclusao": data_conclusao,
        "concluida": concluida
    }

    tarefas.append(tarefa)

def adicionar_arquivo(tarefas):

    with open('teste.csv', 'w') as tabela:

        obj_incluir = writer(tabela)

        for tarefa in tarefas: 
            obj_incluir.writerow(tarefa.values())    

# Função para exibir todas as tarefas
def exibir_tarefas(id_tarefa = None):
    if id_tarefa is not None:
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                print(f"ID: {tarefa['id']}")
                print(f"Nome: {tarefa['nome']}")
                print(f"Descrição: {tarefa['descricao']}")
                print(f"Data de Início: {tarefa['data_inicio']}")
                print(f"Data de Conclusão: {tarefa['data_conclusao']}")
                print(f"Concluída: {'Sim' if tarefa['concluida'] else 'Não'}")
                print()
                return
        print("Tarefa não encontrada")

    else:
        for tarefa in tarefas:
            print(f"ID: {tarefa['id']}")
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Data de Início: {tarefa['data_inicio']}")
            print(f"Data de Conclusão: {tarefa['data_conclusao']}")
            print(f"Concluída: {'Sim' if tarefa['concluida'] else 'Não'}")
            print()

# Adicionar algumas tarefas de exemplo
adicionar_tarefa(1, "Fazer compras", "Comprar comida e produtos de limpeza", "2024-03-14", "2024-03-15", False)
adicionar_tarefa(2, "Estudar Python", "Estudar programação em Python", "2024-03-14", "2024-03-21", False)
adicionar_tarefa(3, "Fazer exercícios", "Fazer exercícios físicos", "2024-03-15", "2024-03-15", True)

# Adiciona a lista de tarefas ao arquivo csv
adicionar_arquivo(tarefas)

# Exibir todas as tarefas
exibir_tarefas()

exibir_tarefas(1)
