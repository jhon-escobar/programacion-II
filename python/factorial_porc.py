
def calcular_factorial(numero):
    if numero < 0:
        return "¡Error! El factorial no está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

while True:
    num = int(input("Ingrese un número entero no negativo: "))
    resultado = calcular_factorial(num)
    print(f"El factorial de {num} es {resultado}")
git
