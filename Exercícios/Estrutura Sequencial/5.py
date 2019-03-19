#https://wiki.python.org.br/EstruturaSequencial
from number import Number

num = Number()

metros = input("Informe um valor em metros ")

if num.isnumber(metros):
    print(metros + " metro(s) são " + str(int(metros) * 60) + " centímetros")
else:
    print("Você não informou um número válido!")