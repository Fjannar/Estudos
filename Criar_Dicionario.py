estudante = {
    'Nome':'Joao',
    'Matricula' : 15099,
    'data_nascimento': '28/03/2000',
    'coeficiente_academico': 8.7
}
minhLista = ['Joao', 32]
print(estudante['Nome'])
print(estudante['Matricula'])
print(estudante['data_nascimneto'])
print('coeficiente_academico')
estudante['nome'] = 'Mariana'
estudante['curso'] = ['Matematica', 'Fisica', 'Biologia']
print (estudante.keys)
del estudante ['curso']
estudante.pop('matricula')
print(list(estudante))
print(len(estudante))
print('nome' in estudante)
print('matricula' in estudante)
estudante.get('nome')
print(estudante.items)

