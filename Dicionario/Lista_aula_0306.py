#Lista em python
lista_elemento = ['Agua', 'Terra' , 'fogo' , 'Ar']
print (lista_elemento[0])
print (lista_elemento[1])
print (lista_elemento[2])
print (lista_elemento[3])

for lista in lista_elemento:
    print(lista)

lista_elemento.insert (3, 'lava')
print (lista_elemento)
#Metodo .remove 


# Listas:

# 1: Crie um algoritmo que, ao declararmos uma lista com o nome de três amigos, imprima:
# o nome do primeiro amigo
# o nome do segundo amigo
# o nome do terceiro amigo
lista_amigos = ['Alexandre','Samuel', 'Cunha', 'Filipe']
print (lista_amigos[0])
print (lista_amigos[1])
print (lista_amigos[2])

# 2: Dada a seguinte lista:
# animais = ["foca", "golfinho", "leão", "tartaruga"]
# Crie um algoritmo que imprima o primero e o último item da lista.
# Depois remove o primeiro e o último da lista. 
# Imprima novamente a lista para saber se os valores corretos foram removidos.
animais = ["foca", "golfinho", "leão", "tartaruga"]
print(animais [0])
print(animais [3])
animais.remove ('foca')
animais.remove ('leão')
print(animais)
# 3 -  Dada a seguinte lista:
# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
# Crie um algoritmo que ao receber essa lista, remova "aveia", "desodorante" e "maçã"
produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
produtos.remove ('aveia')
produtos.remove ('desodorante')
produtos.remove ('maçã')
# 4 - Utilizando a mesma lista do exercício anterior crie um algoritmo que insere um novo item na lista depois de todo item iniciado com a letra "a"
produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
for item in produtos:
    contador += 1
    if item[0] == 'a':
        produtos.insert (contador, 'banana')
        produtos.insert(produtos.index(item)+1,'banana')


#TUPLA
tulpaNome = ('antonio','Illo', '')
tulpaTema = ('Ilo', )