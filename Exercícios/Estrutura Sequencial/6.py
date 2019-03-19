#https://wiki.python.org.br/EstruturaSequencial
from number import Number

num = Number()

raio = input("Informe o raio do círculo: ")

if num.isnumber(raio):
    area = 3.14 * (int(raio) ** 2)
    print("Um círculo de raio " + str(raio) + " tem " + str(area) + " de area!")
else:
    print("Você não informou um número válido")