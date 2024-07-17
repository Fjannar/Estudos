# 1 - Crie uma variável e exiba o valor dessa variável no terminal.
num = int(input('Digite um numero: '))
print (num)

# 2 - Crie uma variável do tipo inteiro e exiba o tipo da variável no terminal
num2 = int(100)
print (type(num2))
# 3 - Crie uma variavel para o nome e uma para o sobrenome de uma pessoa e exiba o nome completo no terminal.
nome = input('Digite seu nome: ')
sobre_nome = input('Digite seu sobrenome: ')
print (nome + sobre_nome)
# 4 - Crie um programa que recebe dois valores e imprime no terminal a soma dos valores informados.
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite outro numero: '))
print (num3 + num4)
# 5 - Crie um programa que recebe dois valores e imprime no terminal a divisão dos valores informados.
num5 = int(input('Digite um numero: '))
num6 = int(input('Digite outro numero: '))
print (num5 / num6 )
# 6-  Crie um programa que recebe três numeros, calcula a média dos três valores e exibe a média no terminal com a mensagem: 'A média dos valores informados é: ' juntamente com o valor da média.
x = int(input("Digite o primiero valor:"))
y = int(input("Digite o segundo valor:"))
z = int(input("Digite o terceiro valor:"))
media = (x+y+z)/3
print (f"A media dos tres valors{x},{y},{z} é", media)
# 7 - Crie um programa que exibe o seguinte menu ao usuário:
# Bem vindo à Calculadora (seguido nome do usuário)
# Qual operação você deseja realizar:
# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão 
# 5 - Sair.
# O programa deve ler a opção escolhida pelo usuário e independente da opção escolhida exibir a mensagem:
# Excelente escolha, encerrando o programa... 
nome = ("Digite seu nome")
print("Bem vindo a Calculadora", nome)
print("Qual operação deseja fazer?")
print("1 = soma\n 2 = Subtração\n 3 = Multiplicação\n 4 = Divisao\n 5 = Sair\n")

escolha = int(input("Digite sua escolha: "))
soma = (x+y)
subtracao = (x-y)
multiplicacao = (x*y)
divisao = (x/y)
x = int(input("Digite o primeiro valor:"))
y = int(input("Digite o segundo valor: "))
if escolha == 1:
    print ("Excelente escolha")
    print (soma)
elif escolha == 2:
    print ("Excelente escolha")
    print(subtracao)
elif escolha == 3:
    print ("Excelente escolha")
    print (multiplicacao)
elif escolha == 4:
    print ("Excelente escolha")
    print (divisao)
else:
    print("Voce saiu da calculadora")