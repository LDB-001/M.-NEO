def get_n():
    print("De o numero de alunos")
    n=int(input())
    return n

def test_n(n):
    if n<2 or n>10:
        return False
    else:
        return True    

def get_marks():

    parameters = input("Nome e notas").split()
    name = parameters.pop(0)
    marks = []

    for i in parameters:
        marks.append = int(i)
    return name, marks



def test_marks(name,marks,listnames):
    for i in listnames:
        if(name == i):
            return False
    
    for mark in marks
        if()




def media(marks):
    for i in marks:
        media=0+i
        return media

def main():
    get_marks()

    '''
    n = 0
    while(not test_n(n)):
        n = get_n()
'''
if __name__ == '__main__':
    main()

    '''n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()'''