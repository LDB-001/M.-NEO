n=int(input("Diga o npumero de Atletas :\n"))
raking=[]
higth=[]
age=[]
print("Diga a posição de cada candidato: \n")
for i in range (0,n):
    pos=input()
    ranking.append(pos)
print("Diga os valores das respectivas alturas:\n")
for i in range (0,n):
    alt=input()
    higth.append(alt)
print("Diga o valor das respectivas idades dos membros: \n")
for i in range (0,n):
    idade=input()
    age.append(idade)
x=input("Diga qual o critério que deve ser classificado (Altura=1 Idade=2) \n")
