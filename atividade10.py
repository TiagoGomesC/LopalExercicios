senha_certa = "676767"
tentativa = input("Digite a sua senha:")

while tentativa != senha_certa:
    print("Senha digitada nao está correta, tente de novamente!")
    tentativa = input("Digite a sua senha:")

print("O seu acesso foi liberado!")