def maior_valor():
    x = int(input("Digite primeiro numero: "))
    y = int(input("Digite segundo numero: "))
    if x > y:
        print(f"o numero {x} é maior que o numero {y}")
    elif x < y:
        print(f"o numero {y} é maior que o numero {x}")
    else:
        print(f"Os numeros {x} e {y} sao iguais")
maior_valor()