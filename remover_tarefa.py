def remover_tarefa(lista,id):
    """
    Recebe obrigatoriamente: lista,id.\n
    Retorna a lista com a lista atualizada ou sem alterações se a  operação falhar.\n
    Função que remove uma tarefa da lista.
    """
    if lista:
        for n in lista:
            if int(n["id"])==int(id):
                lista.remove(n)
                return lista
    return lista