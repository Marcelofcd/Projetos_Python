from collections import Counter
nome = input()
nome = nome.lower()
nome = nome.strip()
print (nome)
for letra in nome:
    counter = Counter(nome)
print (counter)