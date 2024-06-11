#Se a senha for validada com sucesso um menu deverá se exibido ao usuario
#A pessoa tem 3 tentativas para acertar, caso nao consiga o sistema se encerra
#Esse menu deve conter as seguintes opçoes:
#1 Cadastro novo aluno
#1.2- Asinformaçoes de cadastro sao: Matricula, (nao pode ser repestido), Nome, idade, turma
# 2- ver alunos cadastrados
# 3- sair
tentativas = 0
while True:
    senhas_validas = ['111', '222', '333']
    if tentativas > 2:
        print ('Excedeu suas tentativas, Acesso negado')
        break
    input_senha = input('Digite sua senha: ')
    if input_senha in senhas_validas:
        print('Acesso concedido')
    else:
        print('Senha incorreta')
        tentativas +=1
    while True:
        print ('Bem vindo ao sistema ao de cadastro do aluno')
        print ('1- Cadastrar novo estudante')
        print ('2- Ver alunos cadastrados')
        print ('3- Sair')
        opcoes = int(input('Escolha opçao de 1 a 3: '))
        if opcoes == 1:
            cadastro = input ('Digite cadastro do aluno: ')
            matricula = input('Digite matricula: ')
            nome = input ('Digite o nome do Aluno: ')
            cpf_senha = int(input('digite CPF do aluno: ' ))
            idade = int(input('Digite idade do aluno: '))
        if opcoes == 2:
            int(input('Digite o CPF do aluno'))
            print ([nome],[matricula],[cpf_senha],[idade])
        if opcoes == 3: 
            print('Sair')
            break