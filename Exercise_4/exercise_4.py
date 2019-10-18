x=int(input("Diga o ano: \n"))
if x>1900 and x<100000:
    if x%4==0:
        print("O ano : ",x," é um ano bissexto")
    else:
        print("O ano : ",x, " não é um ano bissexto")
else:
    print("Ano inválido")
