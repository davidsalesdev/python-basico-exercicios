#Definição de uma lista

#Nesta atividade, você editará um script Python para armazenar uma coleção ou lista de nomes de frutas.

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))


print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Alteração dos valores da lista

#Os valores de uma lista podem ser alterados. Nesta atividade, você mudará cherry para orange.

myFruitList[2] = "orange"

print(myFruitList)

#Exercício 2: apresentação do tipo de dado tupla
#Definição de uma tupla
#A tupla é como uma lista, mas não é possível alterá-la. Chamamos de imutáveis os tipos de dados que não podem ser alterados após sua criação. Para definir uma tupla, você usa parênteses em vez de colchetes ([])


myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))


#Acesso a uma tupla pela posição

#Como uma lista, os itens de uma tupla também podem ser acessados por posição
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Definição de um dicionário

#Um dicionário é uma lista com posições nomeadas (chaves). Imagine que sua lista mostra a fruta favorita das pessoas


myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

#Use a função print() para escrever o dicionário no shell:
print(myFavoriteFruitDictionary)

#Use a função type() para escrever o tipo de dado no shell:
print(type(myFavoriteFruitDictionary))


#Acesso a um dicionário pelo nome
#Nesta atividade, em vez de usar números, use o nome das pessoas para obter a fruta favorita delas.
#Para acessar a fruta favorita de Akua, insira o seguinte código:

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

