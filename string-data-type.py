myString = "This is a string"


print(type(myString))

print(myString + "is of the data type" + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


#Exercício 3: uso de strings de entrada

name = input("What your name? ")
print(name)

# Exercício 4: formatação de strings de saída
#Quando o script deseja comunicar alguma informação de volta ao usuário, esta é chamada de saída. Você usou a função print() para escrever a saída no shell. Você criará uma pesquisa e enviará as informações coletadas de volta para o usuário.

color  = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

#Você usou a função print() com apenas uma variável, mas também pode usá-la com diferentes variáveis, para formatar uma string. Insira o seguinte código:
print("{}, you like a {} {}!".format(name,color,animal))



