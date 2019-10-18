n=int(input("Diga o número de Atletas :\n"))
candidatos=[]
print("Insira o nome, colocação, altura e idade do competidor, respectivamente.")
for i in range (0,n):
    cand=[input("Nome: "),input("Colocação: "),input("Altura: "),input("Idade: ")]
    candidatos.append(cand)
x=str(input("Como você gostaria de classificar os membros? (altura | idade )\n"))
ordenar=[]
if x=="altura":
    ordenar=sorted(candidatos,key=lambda candidatos: candidatos[2])
    print(ordenar)
if x=="idade":
    ordenar=sorted(candidatos,key=lambda candidatos: candidatos[3])
    print(" A lista ordenada por ",x, "em ordem crescente é ",ordenar)
