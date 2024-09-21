
#Usara um loop while
#Usara um loop for


import random

#Coloque o cursor na próxima linha após a segunda declaração print(). Depois, insira uma declaração que gere um número aleatório entre 1 e 10 usando a função randint() do módulo random.

number = random.randint(1,10)

#Verifique se o usuário adivinhou o número criando uma variável chamada isGuessRight

isGuessRight = False


#Para lidar com a lógica do jogo, crie um loop while

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))



#Exibição das regras do jogo

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Importação de random e escrita de um loop while


