"""Exercise 1"""
def main():
    """Save marks for up to 10 users and outputs the average
       percentage marks obtained by a student"""
    lst_nomes = []
    number_names = int(input("relate o número de nomes\n"))

    if number_names >= 1 or number_names <= 10:
        print("Ensira os nomes dos alunos \n")
        for i in range(0, number_names):
            nomes = str(input())
            lst_nomes.append(nomes)
            print("Restam ", number_names-(i+1), " nomes")
    else:
        print("Esse valor não é compatível\n")

    print("Diga as respectivas 3 notas dos alunos anteriormente citados\n")
    lst_notas = []

    for i in range(0, number_names):
        notas = [float(input()), float(input()), float(input())]
        lst_notas.append(notas)
        print("Notas do aluno: ", i+1)

    saida = 1
    while saida != 0:
        student_name = str(input("Qual aluno você deseja saber a média ? \n"))
        if student_name in lst_nomes:
            pos = lst_nomes.index(student_name)
            for i in range(0, 3):
                media = sum(lst_notas[pos])/3
            print("A média do aluno é: ", media)
            saida = input("Se de sejar sair coloque 0, caso queira realizar a "\
                          "média de outro aluno adicione qualquer numero diferente de 0\n")
        else:
            print("Esse nome não está na lista")
            saida = input("Se de sejar sair coloque 0, caso queira realizar a "\
                          "média de outro aluno adicione qualquer numero diferente de 0\n")
        break

if __name__ == "__main__":
    main()
