# 35 - Crie um algoritmo que recebe três números e compare cada desses números e imprima: 
# Para o menor número a mensagem: "<numero1> é o menor entre os números fornecidos"
# Para o número intermediário: "<numero2> está entre <numero1> e <numero3>"
# Para o maior número: "<numero3> é o maior entre os números"
num = int(input('Escreva um numero: '))
num2 = int(input('Escreva outro numer: '))
num3 = int(input('Escreva mais um numero: '))
maior = num
if num2 > maior:
    maior = num2
    if num3 > maior:
        maior = num3
        medio = num2
        menor = num
        print(f'maior numero é {maior}')
        print(f'{medio} está entre {maior} e {menor}')
        print(f'o numero {menor} é o menor numero')
elif num3 > num:
    medio = num3
    menor = num
    print (f'maior numero é {maior}')
    print (f'{medio} esta entre {maior} e {menor}')
    print (f'o numero {menor} é o menor numero')
elif num3 > maior:
    maior = num3
    medio = num
    menor = num2
    print (f'maior numero é {maior}')
    print (f'{medio} esta entre {maior} e {menor}')
    print (f'o numero {menor} é o menor numero')
elif num2 > num3:
    medio = num2
    menor = num
    print (f'maior numero é {maior}')
    print (f'{medio} esta entre {maior} e {menor}')
    print (f'o numero {menor} é o menor numero')
else:
    print(' ha ingualdade entre os elementos')