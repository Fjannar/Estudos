#Escreva uma função que determine se um número é par ou ímpar.
def par_impar():
    num = int(input("Digite um numero"))
    if num%2 == 0:
        print(f"o numero {num} é par")
    else:
        print(f"o numero {num} é impar")
par_impar()