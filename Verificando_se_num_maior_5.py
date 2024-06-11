#Exercicio livro num 6
num = int
input (int("Escreva um numero"))
if num > 5:
    print("numero maior que 5")
else:
    print("numero nao é maior que 5")
#Exercicio livro num 7
num1 = input('digite o numero: ')
num2 = input ('digite o outro numero: ')
if num2 < num1: 
    print (f'{num2} maior que{num1}' )
else:
    print (f'{num1} maior que {num2}')

#Exercicio livro num 8
num = input('digite o numero: ')
num1 = input ('digite o outro numero: ')
if num > num1: 
    print (f'{num} menor que{num1}' )
else:
    print (f'{num1} menor que {num}')

#Exercicio livro num 9
senha = ('kaue1234')
input ('Digite uma senha')
if senha == ('admin1234'):
    print ('Bem vindo administrador')
else: print ('Voce não é um usuario administrador')

#Exercicio livro num 10
#Mercadinho
num = int
saldo = 17
if saldo > 0:
    print ('Saldo positivo =')
    print ('Voce ganhou 15% de desconto')
elif saldo < 0:
    print ('Saldo negativo =')
    print ('Voce ganhou 5% de desconto')
else:
    print ('Seu saldo esta zerado!')
    print ('Voce ganhou R$ 15,00 de credito')

# exercicio do livro num 11
#Determinando a faixa etaria
idade = 0
input ('Digite sua idade')
if idade <= 12:
    print ('Criança')
elif idade <= 19:
    print ('Adolescente')
elif idade <= 64:
    print ('Adulto')
else:
    print ('idoso')

#Exercicio do livro num 12
#Classificaçao de nota escolar
nota = 0
input ('Digite sua nota')
if nota <= 4:
    print ('Reprovado')
elif nota <= 6:
    print ('Recupareçao')
elif nota <=10:
    print ('Aprovado')

#Exercicio do livro num 13
#Calculando IMC
peso = float (input('Digite seu peso'))
altura = float (input('Digite sua altura'))
imc = peso/(altura* altura)
if imc < 18.5:
    print ('Abaixo do peso')
elif imc == 18.5:
    print ('peso normal')
elif imc > 25.0:
    print ('sobrepeso')
elif imc > 30.0:
    print ('Obesidade')

#Exercicio 14
#Decisao de compra
preco = float (input('Digite o valor do produto'))
if preco < 5.00:
    print ('Barato')
elif preco <= 10.00:
    print ('Razoavel')
elif preco <= 25.00:
    print ('Sobrepeso')
elif preco > 100.00:
    print ('Caro')

#Exercicio 15
#Vogal ou numero?