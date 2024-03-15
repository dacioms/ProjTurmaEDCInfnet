# código para pegar as datas. formato: Thu Mar 14 11:49:36 2024.
# Serve para data de inicio e data de conclusao

#data formatada sem horas e minutos: datetime.datetime.now().strftime("%d/%m/%Y") 
 

import datetime

x = datetime.datetime.now()

print(x.strftime("%d/%m/%Y"))

# return do código acima ( 14/03/2024);

import datetime 

current_date = datetime.datetime.now()
new_date = current_date + datetime.timedelta(days=7)
print("Data daqui a 7 dias:", new_date.strftime("%d/%m/%Y")) 

# return do código acima (21/03/2024);




