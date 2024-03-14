import csv
Tarefas = {
    
    "Concluidas": [],
    "Pendentes": [],
    "Urgentes": [],
    "Removidas": []
}

rows = []


caminhos = ["Concluida", "Pendente", "Urgente", "Removidas"]


arquivo = open("Tarefas.csv", newline='')


def ler_csv():

    leitor = csv.reader(arquivo)
    header = next(leitor)
    header.remove('')



    for line in reader:

        classificacao = {

            "Nome": " ",
            "Concluida": [],
            "Pendente": [],
            "Urgente": [],
            "Removida": []
        }

    for ind, valor in enumerate(line):

        if ind == 0:
            classificacao["Nome"] = valor

        else:
            classificacao["Concluida"]
#-----------

        

with open("Tarefas.csv", 'r') as f: 


    data = list(csv.reader(f, delimiter=","))



print(data)


    # csvreader = csv.reader(f)
    # header = []
    # header = next(csvreader)
    # for row in csvreader:

    #     rows.append(rows)


# print(header)
# print(rows)

















#
#with open ("Tarefas.csv", 'r') as ler_tarefas:

 #   for line in lista_tarefas_csv:

  #    lista_tarefas.readlines()





