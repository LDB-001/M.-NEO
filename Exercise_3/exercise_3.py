n=int(input("Diga o número de numeros elevados ao quadrado \n"))
if n<20 and n>0:
    print("Os respectivos números elevados ao quadrado são: ")
    for i in range (0,n):
        print(i*i)
else:
    print ("Valor inválido")