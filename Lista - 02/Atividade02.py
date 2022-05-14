def nota(n1, n2, n3, x):
    if (x == "a"):
        c = (n1 + n2 + n3) / 3
        print("A média aritmética do aluno foi: ", c)
    elif (x == "p"):
        y = (n1 * 5 + n2 * 3 + n3 * 2) / 10
        print("A média ponderada do aluno foi: ", y)
n1 = float(input("Digite a n1: \n"))
n2 = float(input("Digite a n2: \n"))
n3 = float(input("Digite a n3: \n"))
x = input("Digite uma 'a' ou 'p': \n")    
nota(n1,n2,n3,x)
