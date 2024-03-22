
lista = [1, "","31319310310313","13","13","131031301","301","313","10313910391031313","13019310391093"]
lista_geral_tarefas = []


with open ("Tarefas.csv", 'w') as lista_tarefas:

  def salvar(lista): 
  
    for line in lista:

      lista_tarefas.writelines(line + "\n")


# Acesso, inserção, remoção, alteração de dados.



with open("Tarefas.csv", 'r', encoding= "utf-8") as ler_tarefas:
  def ler():
    for line in lista:
      lista_tarefas.writelines(line + "\n")
      






