velocidade = float(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 20.00
    print(f"Você foi multado! O valor da multa é de R${multa:.2f} por exceder {excesso} km/h acima do limite.")
else:
    print("Você está dentro do limite de velocidade.")
