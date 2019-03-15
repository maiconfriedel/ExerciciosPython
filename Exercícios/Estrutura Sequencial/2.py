from number import Number

num = Number()

numero = input("Digite um número")

if num.isnumber(numero):
    print("O número informado foi: " + numero)
else:
    print("Não foi informado um número válido")

