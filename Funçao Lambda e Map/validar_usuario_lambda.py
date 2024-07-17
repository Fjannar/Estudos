#Funçao lambda usando condicional para classificar informaçoes em tres categorias de menssagens.
valida_usuarios = lambda user: "Erro: usuarui precisa ser definido" if user == "" else ("usuario nao pode ter menos de 4 digitos" if len (user)<4 else "usuario definido com sucesso!")

#Exemplos de uso da funçao lambda
print(valida_usuarios(""))
print(valida_usuarios("Ze"))
print(valida_usuarios("Jose"))
