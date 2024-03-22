def remover_tarefa(lista,id):
    """
    Recebe obrigatoriamente: lista de dicionarios,id.\n
    Retorna a lista com a lista atualizada ou sem alterações se a  operação falhar.\n
    Função que remove uma tarefa da lista.
    """
    # lista =[]    
    if lista:
        for index, n in enumerate(lista):
            if int(n["id"])==int(id):
                print(n)
                lista.pop(int(index)-1)
                return lista
    return lista