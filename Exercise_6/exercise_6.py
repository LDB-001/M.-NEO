print("Adicione a quantidade de números que você quer adicionar na lista 1:")
n1=int(input("Numero\n"))
lista1=[]
print("Adicione os valor da lista 1:")
for i in range (0,n1):
    número1=int(input())
    lista1.append(número1)
print("Adicione a quantidade de números que você quer adicionar na lista 2:")
n2=int(input("Numero\n"))
lista2=[]
print("Adicione os valor da lista 2:")
for i in range (0,n2):
    número2=int(input())
    lista2.append(número2)
print("Adicione a quantidade de números que você quer adicionar na lista 3:")
n3=int(input("Numero\n"))
lista3=[]
print("Adicione os valor da lista 3:")
for i in range (0,n3):
    número3=int(input())
    lista3.append(número1)
maior1=max(lista1)
maior2=max(lista2)
maior3=max(lista3)
print(maior1,maior2,maior3)
valor=(maior1*maior1+maior2*maior2+maior3*maior3)
print("O resto da divisão por mil, da soma dos quadrados do maior valor de cada lista é :", valor)