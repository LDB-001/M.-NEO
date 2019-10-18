n=int(input("Diga a quantidade de números que você deseja saber\n"))
if n<1 or n>15:
    print("Valor inválido\n")
fibo=[0,1]
for i in range (0,n):
        fibo.append(fibo[i]+fibo[i+1])
fibo_cube=[]
for i in fibo:
    fibo_cube.append((i)**3)
print("A sequência de fibonacci de tamanho ",n," é ",fibo)
print("O valor da sequência ao cubo é ",fibo_cube)