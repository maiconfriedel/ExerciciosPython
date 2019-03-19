#https://wiki.python.org.br/EstruturaSequencial
from number import Number

num = Number()

largura = input("Informe a largura do quadrado ")

if num.isnumber(largura):
    area = int(largura) ** 2
    print("A área do quadrado informado é de: " + str(area) + " e o dobro desse valor é: " + str(area * 2))
else:
    print("Você não informou um número válido!")