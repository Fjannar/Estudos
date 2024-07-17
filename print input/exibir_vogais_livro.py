vogais = ['a','e','i','o','u']
palavra = 'abacaxi'
for letra in palavra:
    if letra in vogais:
        print(letra)
for letra in palavra:
    if letra not in vogais:
        print(letra)