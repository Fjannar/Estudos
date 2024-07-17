palavra = input ('Digite uma palavra: ')
vogais = ['a' , 'e' , 'o' , 'u']
for letra in palavra:
    if letra.lower in (vogais):
        print (letra)