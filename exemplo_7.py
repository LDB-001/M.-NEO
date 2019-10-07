n=int(input("Diga quatos números haverá na lista: \n"))
x=int(input("Diga quantos valores haverá nas listas de comparação A e B\n"))
print("Os valores para a lista: ")
lista=[]
for i in range (0,n):
    numeros=int(input())
    lista.append(numeros)
lista__A=[]
lista__B=[]
print("Valores para a lista A: \n")
for i in range (0,x):
    a=int(input())
    lista__A.append(a)
print("Valores para a lista B: \n")
for i in range (0,x):
    b=int(input())
    lista__B.append(b)
happy=0
for i in range (0,x):
    if lista__A[i] in lista:
        happy=happy+1
    elif lista__B[i] in lista:
        happy=happy-1
print("O valor de Happy é : ",happy)