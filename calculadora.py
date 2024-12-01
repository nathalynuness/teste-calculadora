def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "Erro: Divisão por zero"

# Entrada de dados
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

# Escolher operação
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print(somar(a, b))
elif operacao == "-":
    print(subtrair(a, b))
elif operacao == "*":
    print(multiplicar(a, b))
elif operacao == "/":
    print(dividir(a, b))
else:
    print("Operação inválida")