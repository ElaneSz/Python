def ideal(sexo):
    if (sexo == "F"):
        peso1 = (62.1*altura)-44.7
        print("Seu peso ideal é:",peso1)
    if (sexo == "M"):
        peso2 = (72.7*altura)-58
        print("Seu peso ideal é:",peso2)
altura = float(input("Digite sua altura: \n"))
print("==========Digite seu sexo==========")
sexo = (input("F para FEMININO ou M para MASCULINO: \n"))
ideal(sexo)
