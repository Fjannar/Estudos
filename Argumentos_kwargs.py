def mostrar_info(**Kwargs):
    for chave, valor in Kwargs.items():
        print(f"{chave}:{valor}")

mostrar_info(nome = "Gabriel", idade = 27 , cidade = "Belo Horizonte") #imprime info in parenteses
mostrar_info(curso = "python", nivel = "iniciante", plataforma = "presencial")
