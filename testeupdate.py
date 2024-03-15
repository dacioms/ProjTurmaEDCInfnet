import csv

with open("Tarefas.csv", "r") as reescrever_tarefas:
    dicio = csv.DictReader(reescrever_tarefas)
    
    reescreve = []
    