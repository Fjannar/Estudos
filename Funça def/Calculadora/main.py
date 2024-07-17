import operacoes

def menu():
    print("Bem vindo a calculadora")
    print("Qual operaçao deseja fazer?")
    print("1 = Soma, 2 = Subtraçao, 3 = Multiplicaçao, 4 = Divisao, 5 = Potencia, 6= Sair")

menu()
escolha = int(input("Digite sua escolha: "))


if escolha in [1,2,3,4,5]:
    x = int(input("Digite o primeiro valor:"))
    y = int(input("Digite o segundo valor: "))
    if escolha == 1:
        print ("Resultado:", operacoes.soma(x,y))
    elif escolha == 2:
        print ("Resultado:", operacoes.subtracao(x,y))
    elif escolha == 3:
        print ("Resultado:", operacoes.multiplicacao(x ,y))
    elif escolha == 4:
        print("Resultado:", operacoes.divisao(x,y))
    elif escolha == 5:
        print("Resultado:", operacoes.potencia(x,y))
else:
    print("Voce saiu da calculadora:")
