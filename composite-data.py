
  
#Usará tipos de dados numéricos
#Usará tipos de dados string
#Usará o tipo de dados dicionário
#Usará o tipo de dados lista
#Usará um loop for
#Usará a função print()
#Usará a declaração if
#Usará a declaração else
#Usará a declaração import

import csv
import copy

#defina um dicionário que funcionará como o tipo composto para a leitura dos dados tabulares:
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Você usará um loop for para percorrer as chaves iniciais e valores do dicionário

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

#    a função items() pertence ao tipo de dado dictionary. A função items() diz ao loop for para atravessar a coleção pertencente ao tipo de dado dictionary.

    #Defina uma lista vazia para armazenar o inventário de carros que você lerá em breve:


myInventoryList = []



#Você conhecerá a declaração de sintaxe with open, que mantém um arquivo aberto enquanto você lê seus dados. Ela fecha automaticamente o arquivo CSV quando o código dentro do bloco with termina de ser executado.

#Você também aprenderá uma nova maneira de formatar uma string. Em vez de usar aspas duplas e .format para passar as variáveis, você pode usar uma aspas simples e escrever as variáveis entre os símbolos “{}”.

#Finalmente, csv.reader() é uma função que você usa da biblioteca csv que foi importada com a declaração import csv.

#A maior parte do resto do código deve ser conhecida.



with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

#Embora o código pareça muito grande para processar, ele contém principalmente declarações que você viu em laboratórios anteriores. Você tem um loop for com uma declaração if-else seguida por uma declaração print() no final.

currentVehicle = copy.deepcopy(myVehicle)

#Exibição do inventário de carros

#Você terminará o script Python imprimindo o inventário de carros pela variável myInventoryList.

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")