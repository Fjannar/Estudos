# Função para verificar se um caractere é uma vogal
def eh_vogal(caractere):
    vogais = "aeiouAEIOU"
    return caractere in vogais

# Função para extrair e mostrar as vogais de uma palavra
def mostrar_vogais(palavra):
    vogais = ""
    for letra in palavra:
        if eh_vogal(letra):
            vogais += letra
    return vogais

# Receber uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Mostrar somente as vogais da palavra
print("Vogais na palavra:", mostrar_vogais(palavra))
