
    #Usará a declaração if
    #Usará a declaração else
    #Usará a declaração elif



#Use a função input() para obter informações do usuário:

userReply = input("Do you need to ship a package? (Enter yes or no) ")



#Use a declaração if para imprimir uma resposta.

#As instruções de uma declaração if são recuadas em relação à declaração if. Em outras linguagens de programação, os colchetes são frequentemente usados para indicar o início e o fim de um bloco lógico, mas o Python usa espaçamento


if userReply == "yes":
    print("We can help you ship that package!")

else:
    print("Please come back when you need to ship a package. Thank you.")

    #Observação: o símbolo == é um operador comparativo. Ele significa é igual a.yes

#Exercício 2: uso da declaração else


#Para administrar a condição de que o usuário não quer enviar um pacote, use a declaração else:


#Exercício 3: uso da declaração elif
#Neste exercício, você melhorará o script Python oferecendo ao usuário serviços adicionais. Quando você tem várias condições, é possível usar a declaração elif, que é a abreviação de else-if.

    #Observação: a declaração elif sempre vem depois de uma declaração if e antes da declaração else.


userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
