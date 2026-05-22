import time
num1 = int(input("Coloque o primeiro número: "))
num2 = int(input("Coloque o segundo número: "))
num3 = int(input("Coloque o terceiro número: "))
numeros = [num1, num2, num3]
maior = numeros[0]
# Precisei usar o "maior que (>)"
if numeros[1] > maior:
     maior = numeros[1]
if numeros[2] > maior:
     
     maior = numeros[2]

menor = numeros[0]

if numeros[1] < menor:
    menor = numeros[1]

if numeros[2] < menor:

    menor = numeros[2]

    ---------
    
print("O sistema esta preparando a sequencia...")
time.sleep(3)
print(f"o seu maior número é: {maior}")
print(f"o seu menor número é: {menor}")