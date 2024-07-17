# 6 - Escreva um programa que itere sobre o dicionário estudante e imprima cada chave e seu valor correspondente.
estudante = {
    'nome' : 'Gabriel',
    'idade' : 20,
    'cursos' : ['Python','HTML','CSS','C#'],
    'nota' : '10',
}
for chave, valor in estudante.items():
    print(f'{chave.capitalize()}: {valor}')
    