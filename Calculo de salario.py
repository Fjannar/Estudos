#Faça um Programa que pergunte quanto você ganha por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
#5% para o sindicato, faça um programa que nos dê:
#Salário bruto
#Quanto pagou ao INSS.
#Quanto pagou ao sindicato.
#O salário líquido.
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salário Liquido : R$
mes = input ("Mes:" )
nome = input ("Nome do funcionario: ")
tempoTrabalho = float(input ("Quantas horas trabalhadas esse mes?: "))
valorHora = float(input ("Qual o valor da hora trabalhada?: "))
salarioBruto = (tempoTrabalho * valorHora)
ir = (salarioBruto * 0.11) # Desconto Imposto de renda
inss = (salarioBruto * 0.08) # Desconto INSS
sindicato = (salarioBruto * 0.05 ) # Desconto Sindicato
salarioLiquido = (salarioBruto - ir - inss - sindicato)
print(nome)
print(mes)
print(f"O Tempo de horas trabalhadas é {tempoTrabalho}")
print(f"O valor da hora de trabalho é" , {valorHora})
print(f"O valor do salario bruto é" , {salarioBruto})
print(f"O desconto do imposto de renda será de" , {ir})
print(f"O desconto do INSS será de " , {inss})
print(f"O desconto do sindicato será de " , {sindicato})
print(f"O salario liquido será de " , {salarioLiquido})