def minha_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.item():
        print(chave, valor)
minha_funcao("Curriculo", "Desenvolvedor", nome="Gabriel", idade= 27)
