n=int(input("Diga o número de concorrentes: \n"))
print("Coloque os Scores: \n")
lst_scores=[]
for i in range (0,n):
    scores=[int(input())]
    lst_scores.append(scores)
print(lst_scores)
print("Diga respectivamente os nomes dos concorrentes")
lst_nomes=[]
for i in range (0,n):
    nomes=[str(input())]
    lst_nomes.append(nomes)
maior=[0]
for i in range (0,n):
    if lst_scores[i]>maior:
        maior=lst_scores[i]
        position=i
print(maior,position)
print("Quem tem a maior pontuação é :",lst_nomes[position]," com um score de : ", maior)