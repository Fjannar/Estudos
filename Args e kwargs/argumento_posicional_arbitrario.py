def somar_numeros(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

#chamando a funçao com diferentes numeros de argumentos
print(somar_numeros(1,2,3)) #imprimira a soma dos numeros dentro do parenteses
print(somar_numeros(10,20,30,40,50)) #imprimira a soma dos numeros dentro do parenteses


def somar (*args):
    resultado = 0
    for num in args:
        resultado += num
        return resultado
print(somar(1,2,3)) #imprimi a soma dos numeros dentro do parenteses
