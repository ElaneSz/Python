def categoria(idade):
    if (idade >= 5 and idade <=7):
        print("O nadador é categoria: [ NFANTIL 'A' ]")
    if (idade >= 8 and idade <= 10):
        print("O nadador é categoria: [ NFANTIL 'B' ]")
    if (idade >= 11 and idade <= 13):
        print("O nadador é categoria: [ JUVENIL 'A' ]")
    if (idade >= 14 and idade <= 17):
        print("O nadador é categoria: [ JUVENIL 'B' ]")
    if (idade >= 18):
        print("O nadador é categoria: [ ADULTO ]")
    if (idade < 5):
        print(" [ IMPORTANTE ] - Insira idades acima de 4 anos!")
idade = int(input("Digite a idade do nadador: \n"))
categoria(idade)
