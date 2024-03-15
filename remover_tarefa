def remover_tarefa(lista,id):
  """
  Recebe a lista a manipular e o id da tarefa a remover\n
  Retorna um booleano que descreve o sucesso da operação (True/False).\n
  Função que remove uma tarefa da lista. Retorna FALSE se a lista estiver vazia ou o id não constar na lista.
  """
  if lista:
      for n in lista:
          if n["id"]==id:
              lista.remove(n)
              return True
  return False
