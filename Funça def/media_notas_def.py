# Crie um programa que solicita ao usuário que insira três notas e, 
# em seguida, calcule a média dessas notas
# usando uma função. A função deve receber as três
# notas como argumentos e retornar a média. Por fim, o
# programa deve imprimir a média calculada.

def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Digite um numero valido: ")


def notas ():
    x = int(input("Digite a prmiera nota:"))
    y = int(input("Digite a segunda nota: "))
    z = int(input("Digite a terceira nota: "))
    media = (x + y + z )/3
    print(f"{media:.3f}")
notas()
