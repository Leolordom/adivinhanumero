from random import shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação sera ")
print(lista)
