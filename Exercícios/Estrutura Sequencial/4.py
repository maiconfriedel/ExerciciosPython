#https://wiki.python.org.br/EstruturaSequencial
from number import Number

num = Number()

value1 = input("Informe a nota 1 ")
value2 = input("Informe a nota 2 ")
value3 = input("Informe a nota 3 ")
value4 = input("Informe a nota 4 ")


if not num.isnumber(value1) or not num.isnumber(value2) or not num.isnumber(value3) or not num.isnumber(value4):
    print("Uma das notas informadas não é valida")
else: 
    print("A média é: " + str((int(value1) + int(value2) + int(value3) + int(value4))/4))