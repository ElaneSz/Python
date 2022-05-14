def triangulo(x,y,z):
    if (x < (y+z) or y < (x+z) or z < (x+y)):
        if (x == y and y == z):
            print("Triângulo Equilátero")
        elif (x==y and x!=z or y==z and y!=x or x!=y and z==x):
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
x = float(input("Digite o valor de 'x': \n"))
y = float(input("Digite o valor de 'y': \n"))
z = float(input("Digite o valor de 'z': \n"))
triangulo(x,y,z)
