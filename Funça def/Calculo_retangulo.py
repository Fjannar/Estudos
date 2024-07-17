
#Crie um programa que define uma função:
#calcular_area_retangulo 
#recebe dois argumentos, comprimento e largura de um retângulo
# e retorna a area desse retângulo. 
# Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada.
#A = b * h
#A = area
#b = base
#h = altura

def obter_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Valor invalido, insira um valor valido")

def calculo_retangulo():
    B = obter_numero("Digite o valor da base do retangulo: ")
    H = obter_numero("Digite o valor da altura do retangulo: ")
    A = B * H
    print (f"{A:.3f}")
calculo_retangulo()