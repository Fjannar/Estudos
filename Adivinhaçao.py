from random import randint
segredo = randint (1,10)
tentativa = 3
palpite = int (input('tente adivinhar o numero:'))
while tentativa != segredo:
    tentativa = int(input('tente adivinhar o numero secreto: '))
    tentativa -=1 
    if palpite > segredo:
        print ('o segredo é menor')
    if palpite < segredo:
        print (' O segredo é maior')
    if palpite == segredo:
        print ('Parabens voce conseguil descobrir o segredo')
    print (f'voce ainda tem {tentativa}: ')