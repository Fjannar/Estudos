contador = 0
soma = 0
print("Digite números inteiros. Digite 0 para terminar.")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    contador += 1
    soma += numero
if contador > 0:
    media = soma / contador
else:
    media = 0
print(f"Quantidade de números digitados: {contador}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media}")