import random
numero_aleatorio = random.randint(1, 10)
tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")
while tentativas < 3:
    try:
        palpite = int(input("Digite o seu palpite: "))
        if palpite == numero_aleatorio:
            print("Parabéns! Você acertou o número.")
            break
        else:
            print("Número errado. Tente novamente!")
            tentativas += 1
    except ValueError:
        print("Por favor, digite um número válido.")

else:
    print("Você esgotou todas as suas tentativas. O número correto era {}.".format(numero_aleatorio))
