x=int(input("Diga o número de elementos q estarão na lista; \n"))
y=int(input("Diga o valor para fazer a operação: \n"))
lista=[]
final=[]
print("Valores dos números da lista: \n")
for i in range(0,x):
    valores=input()
    lista.append(valores)
for i in range(0,x):
    for k in range(i+1,x):
        w=[lista[i],lista[k]]
        final.append(w)
print(final)
    