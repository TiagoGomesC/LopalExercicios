n = int(input("Digite as letras do nome que você quer ter:"))
# A lógica da programação
a = 0
b = 1
# O cont eu usei pra comecar
cont = 0
print("A sua sequencia fibonacci é:")

#o loop das letras vem agora com o while
while cont < n:
  print(a)
  proximo = a + b
  a = b
  b = proximo
  cont = cont + 1 