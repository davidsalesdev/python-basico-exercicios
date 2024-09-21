#Usará tipos de dados numéricos
#Usará tipos de dados string
#Usará o tipo de dados lista
#Usará um loop for
#Usará a função print()


#criação de uma lista com tipos mistos

myMixedTypeList =[45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#Use uma declaração de loop for para ver a lista e escrever o tipo de dado de cada item

for item in myMixedTypeList:
    print("{} is of the data type{}".format(item, type(item)))
