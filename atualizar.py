def atualizar_tarefa(lista,id,nome="",descricao="",data_inicio="",data_conclusao="",concluida=""):
    """
    Recebe obrigatoriamente: lista,id e um ou mais parâmentros opcionais.\n
    Parâmetros opcionais: nome,descricao,data_inicio,data_conclusao,concluida.\n
    Retorna um booleano que descreve o sucesso da operação (True/False).\n
    Função que atualiza uma tarefa da lista. Retorna FALSE se nenhuma atualização for passada como parâmetro opcional ou o id não constar na lista.
    """
    
    if nome=="" and descricao=="" and data_inicio=="" and data_conclusao=="" and concluida=="":
        return False
        
    for n in lista:
        if n["id"]==id:
            if nome!="": n["nome"]=nome
            if descricao!="": n["descricao"]=descricao
            if data_inicio!="": n["data_inicio"]=data_inicio
            if data_conclusao!="": n["data_conclusao"]=data_conclusao
            if concluida!="": n["concluida"]=concluida
            return True
    
    return False
