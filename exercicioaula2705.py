# Exercício 1: Escreva um programa que recebe dois números como entrada e imprime o maior deles.
num = int(input('Escreva um numero: '))
num2 = int(input('Escreva outro numero: '))
if num > num2:
    print (num)
if num2 > num: 
    print (num2)
# Exercício 2: Crie um programa que recebe uma string e verifica se a primeira letra é vogal.
letra = input ('Escreva sua mensagem: ')
if  letra:
    vogais = "A,a,E,e,I,i,O,o,U,u"
    if letra[0:1] in vogais:
        print ('A primeira letra é vogal')
    else:
        print ('A frase nao contem vogal') 
# Exercício 3: Escreva um programa que solicita a idade do usuário e determina se ele é elegível para votar (18 anos ou mais).
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print ('Voce tem permisao para votar') 
# Exercício 4: Crie um programa que recebe uma string como entrada e verifica se ela começa com a letra 'A'. Imprima "Começa com A" se for verdadeiro, caso contrário, imprima "Não começa com A".
letra1 = input('Digite sua mensagem: ')
if  ('A', 'a'):
    print ('Começa com A')
else: 
    print ('nao contem nada NADA!!!!!! BY Sr: Doneziodo')
# Exercício 5: Escreva um programa que solicita ao usuário uma senha. Se a senha for "12345", imprima "Acesso concedido"; caso contrário, imprima "Acesso negado".
senha = int(input('Digite sua senha: '))
if senha == 1234:
    print('Acesso concedido')
else:
    print('Acesso negado')
# Exercício 6: Crie um programa que determina se um ano dado é bissexto. Um ano bissexto é divisível por 4, mas não é divisível por 100, a menos que também seja divisível por 400.
def eh_bissexto(ano):
    if ano % 4 == 0:  # Verifica se o ano é divisível por 4
        if ano % 100 == 0:  # Se for divisível por 100
            if ano % 400 == 0:  # E também divisível por 400
                return True  # É um ano bissexto
            else:
                return False  # Não é um ano bissexto
        else:
            return True  # Se não for divisível por 100, é um ano bissexto
    else:
        return False  # Se não for divisível por 4, não é um ano bissexto

# Exemplo de uso
ano = int(input("Digite um ano para verificar se é bissexto: "))
if eh_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

#PT2
# 1 - Crie um algoritmo que ao ser executado lê uma palavra e imprime as letras dessa palavra separadamente.
letra2 = input('Digite sua mensagem: ')
for letra2 in str:
    print (letra2)
# 2 - Crie um algoritmo que lê a lista de produtos (abaixo) e imprime seus valores separadamente:

produtos = [
    "Camiseta", "Calça jeans", "Tênis", "Mochila", "Notebook", "Fones de ouvido", "Smartphone", "Relógio", "Óculos de sol", "Garrafa de água", "Câmera", "Livros", "Mesa", "Cadeira", "Luminária de mesa", "Caderno"
]

for produtos in str:
    print (produtos)
# 3 - Crie um algoritmo que lê uma lista de produtos (acima) e imprime apenas aqueles que contenham a letra "a"
produtos = [
    "Camiseta", "Calça jeans", "Tênis", "Mochila", "Notebook", "Fones de ouvido", "Smartphone", "Relógio", "Óculos de sol", "Garrafa de água", "Câmera", "Livros", "Mesa", "Cadeira", "Luminária de mesa", "Caderno"
]
for produtos in str:
    print ('A','a')
# 4 - Crie um algoritmo que solicita 4 notas de um usuário e adiciona essas notas numa lista. Calcula a média entre as notas, se a média for igual ou maior a 7 exibe a mensagem: "Aluno aprovado", caso contrário exibe a mensagem "Aluno reprovado".
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

def main():
    notas = []
    for i in range(4):
        nota = float(input(f"Informe a {i+1}ª nota: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    verificar_aprovacao(media)

if __name__ == "__main__":
    main()


# 5 - Crie um algoritmo que ao ser executado recebe uma palavra, verifica se a palavra se inicia com uma vogal e exibe a mensagem "Começa em vogal" caso a palavra se inice em vogal ou exibe a mensagem "Começa em consoante" caso a palavra não se inicie em vogal
letra = input ('Escreva sua mensagem: ')
if  letra:
    vogais = "A,a,E,e,I,i,O,o,U,u"
    if letra[0:1] in vogais:
        print ('Começa com vogal')
    else:
        print ('Começa com conçoante') 
# 6 - Crie um algoritmo que lê duas listas (uma de nomes e outra de sobrenomes) e imprime o nome completo da pessoa..
def imprimir_nomes_completos(nomes, sobrenomes):
    if len(nomes) != len(sobrenomes):
        print("Erro: As listas de nomes e sobrenomes devem ter o mesmo tamanho.")
        return
    for nome, sobrenome in zip(nomes, sobrenomes):
        nome_completo = nome + " " + sobrenome
        print(nome_completo)

def main():
    nomes = []
    sobrenomes = []
    while True:
        nome = input("Digite um nome (ou digite 'fim' para parar): ")
        if nome.lower() == 'fim':
            break
        nomes.append(nome)
    for i in range(len(nomes)):
        sobrenome = input(f"Digite o sobrenome de {nomes[i]}: ")
        sobrenomes.append(sobrenome)

    imprimir_nomes_completos(nomes, sobrenomes)

if __name__ == "__main__":
    main()