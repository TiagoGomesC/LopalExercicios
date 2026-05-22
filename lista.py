Lista = [5, 7, 2, 9, 4, 1, 3]
print(f"O tamanho da lista é:", len(Lista))
# len pra conseguir ter noção do tamanho da lista

print(f"O maior valor da lista é:", max(Lista))
# max variavel pra ter o maior valor da lista

print(f"O menor valor da lista é:", min(Lista))
# min (minimo)

print(f"A soma dos elementos da lista é:", sum(Lista))
Lista.sort()
# sort usei pra organizar a lsita

print("A ordem crescente é:", Lista)
Lista.sort(reverse=True)
# "reverse=True" usei pra organizar a lista de forma decrescente

print("A ordem decrescente é:", Lista)