numero = int(input("Digite um numero inteiro "))

primo = True

for i in range(2, numero):
#usei o operador booleano pra ter o resto da divisão (numero % i)"
# comparação == "0"
  if numero % i == 0:
    primo = False

if primo == True:
  print("O número digitado é primo")
  numero = int(input("Digite um numero inteiro "))

primo = True

for i in range(2, numero):
  if numero % i == 0:
    primo = False
    
if primo == True:
    print("O número digitado é primo")
else:
    print("O numero digitado não é primo")