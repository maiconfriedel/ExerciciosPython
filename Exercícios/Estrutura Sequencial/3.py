#https://wiki.python.org.br/EstruturaSequencial
from number import Number

num = Number()

value1 = input("Informe o número 1")
value2 = input("Informe o número 2")

if num.isnumber(value1):
    if num.isnumber(value2):
        print("A soma é: " + str(int(value1) + int(value2)))
    else:
        print("O valor 2 não é um número válido")
else:
    print("O valor 1 não é um número válido")