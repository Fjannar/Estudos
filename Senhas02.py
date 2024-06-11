#Exercício 1:Continuação do algoritmo de verificação de senhas.
#Porém agora existem três senhas válidas armazenadas numa lista,
#se o usuário digitar alguma das senhas válidas,
#deve ser exibido a mensagem: "Acesso concedido",
#caso contrário: "Senha incorreta, tente novamente"
lista = [111, 222, 333, 444]
entrada = input('Digite uma senha: ')
while entrada != lista:
    print ('Acesso negado, tente novamente')
    entrada = input('Digite uma senha: ')
    if entrada == lista:
        print ('Acesso concedido')