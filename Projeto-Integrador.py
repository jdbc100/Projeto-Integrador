import random

print("Olá! \nEste é um jogo de avidinhação. \nEu gerarei um número aleatório e você terá 5 chances de acertar. \nA cada tentativa, eu darei uma dica se o número que você escolheu é maior ou menor do que o número aleatório.")
print("Let´s go!")

numero = (random.randint(0,100)) #'numero' é a variável que recebe o número aleatório
c = 0 #'c' é o contador

while c < 5:
    c += 1
    palpite = int(input(f"Digite seu {c} ª palpite: ")) #'n' é a variável que recebe o paltite
    if palpite == numero:
        print("Parabéns, você acertou!")
        break
    elif palpite > numero:
        print(palpite, "é maior que o número secreto")
    elif palpite < numero:
        print(palpite, "é menor que o número secreto")
    print()
else:
    print("Você falhou... tente novamente")
