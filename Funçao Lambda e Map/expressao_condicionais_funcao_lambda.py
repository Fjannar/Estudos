#Funça lambda usando condicional para verificar se um numero é par ou impar
par_impar = lambda x: "par" if x % 2 == 0 else "impar"

#Exempls de uso da funçao lambda
print(par_impar(5)) # saida: impar
print(par_impar(-2)) #saida: par