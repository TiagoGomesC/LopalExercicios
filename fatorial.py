numero = int(input("Digite um número inteiro descobrir a fatoração "))
# criei uma variavel "numero" e uma "fatorial"
fatorial = 1

for i in range(1, numero + 1):

    fatorial = fatorial * i
print(f"O fatorial de {numero} é {fatorial}")