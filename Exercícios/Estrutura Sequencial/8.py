#https://wiki.python.org.br/EstruturaSequencial
from number import Number

num = Number()

valor_por_hora = input("Informe o valor por hora trabalhada ")    
horas_trabalhadas = input("Informe quantas horas você trabalha por mês ")

if num.isnumber(valor_por_hora):
    if num.isnumber(horas_trabalhadas):
        valor_total = float(valor_por_hora) * float(horas_trabalhadas)
        print("Você ganha " + str(valor_total) + " por mês!")
    else:
        print("Você não informou horas válidas")
else: 
    print("Você não informou um valor por hora válido")