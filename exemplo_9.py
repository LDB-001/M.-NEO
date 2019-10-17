n=int(input("Diga a o número de linhas|colunas da dimensão do jogo: \n"))
if n==0 or n>100:
    print("Valor inválido para n")
print("Diga onde voce deseja colocar o 'goal':\n ")
goal_l=int(input("Número da linha:\n"))
if goal_l==0 or goal_l>n:
    print("Valor inválido")
goal_c=int(input("Número da coluna: \n"))
if goal_c==0 or goal_c>n:
    print("Valor inválido")
print("Diga onde você de seja começar \n")
start_l=int(input("Número da liha:\n"))
if start_l==0 or start_l>n:
    print("Valor inválido")
start_c=int(input("Número da coluna: \n"))
if start_c==0 or start_c>n:
    print("Valor inválido")
result_line=goal_l-start_l
result_colun=goal_c-start_c
moves=result_colun+result_line
print("O número mínimo de jogadas é de: ", moves) 
