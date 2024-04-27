# Criar um programa para verificar se um número é PAR ou ÍMPAR e imprimir no terminal: 
# "O valor informado é par" (se o valor for par) ou
# "O valor informado é ímpar" (se o valor for ímpar)
num = int(input("Digite um numero"))
if  num%2 == 0: 
    print (f'o numero {num},é par')
else: 
    print (f"o numero {num}, é impar")