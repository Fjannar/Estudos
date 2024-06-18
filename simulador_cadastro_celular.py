senha_cadastrada = "1234"
tentativas_restantes = 3


while tentativas_restantes > 0:
    senha_digitada = input("Insira a senha: ")
    
    if senha_digitada == senha_cadastrada:
        print("Bem-vindo.")
        break

    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem {tentativas_restantes} tentativas restantes.")
        else:
            print("Telefone bloqueado.")

if tentativas_restantes == 0:
    print("Telefone bloqueado. Entre em contato com o suporte.")
