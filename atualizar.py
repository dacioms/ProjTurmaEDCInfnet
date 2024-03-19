def atualizar_tarefa(lista,id,nome="",descricao="",data_inicio="",data_conclusao="",concluida=""):
    """
    Recebe obrigatoriamente: lista,id e um ou mais parâmentros opcionais.\n
    Parâmetros opcionais: nome,descricao,status,prazo_final,urgencia.\n
    Retorna a lista com a tarefa atualizada ou sem alterações se a  operação falhar.\n
    Função que atualiza uma tarefa da lista.\n
    """
    
    if nome=="" and descricao=="" and data_inicio=="" and data_conclusao=="" and concluida=="":
        return lista
        
    for n in lista:
        if int(n["id"])==int(id):
            if nome!="": n["nome"]=nome
            if descricao!="": n["descricao"]=descricao
            if data_inicio!="": n["data_inicio"]=data_inicio
            if data_conclusao!="": n["data_conclusao"]=data_conclusao
            if concluida!="": n["concluida"]=concluida
            return lista    
    return lista
