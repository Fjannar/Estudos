#REVISAO WHILE: CRIE UM ALGORITIMO PARA SOLICITAR UMA SENHA AO USUARIO, SE ESSA SENHA NAO FOR IGUAL A SENHA PRE-DEFINIDA , EXIBA "SENHA INCORRETA, TENTE NOVAMENTE"
#FUNCIONAMENTO SO ENCERRA QUANDO O USUARIO ACERTA A SENHA, E ENTAO EXIBIMOS A MENSAGEM: "ACESSO CONCEDIDO"
senha = '1234'
entrada = input('Digite sua senha: ')
while entrada != senha:
    print ('Acesso negado:')
    entrada = input('Digite a senha novamente: ')
else:
    print ('Acesso concedido')