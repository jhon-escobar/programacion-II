# print("ingrese el numero")
# def factorial_numero(num):
# fact=1
# num = int(input())
# for i in range(1, num+1):
#     fact*=i
#     return fact
# print("el factorial de " ,num, "es", fact)
# return
# def calcular_factorial(numero):
#     if numero < 0:
#         return "¡Error! El factorial no está definido para números negativos."
#     elif numero == 0:
#         return 1
#     else:
#         factorial = 1
#         for i in range(1, numero + 1):
#             factorial *= i
#         return factorial

# if __name__ == "__main__":
#     num = int(input("Ingrese un número entero no negativo: "))
#     resultado = calcular_factorial(num)
#     print(f"El factorial de {num} es {resultado}")
# def calcular_factorial(numero):
#     if numero < 0:
#         return "¡Error! El factorial no está definido para números negativos."
#     elif numero == 0:
#         return 1
#     else:
#         factorial = 1
#         for i in range(1, numero + 1):
#             factorial *= i
#         return factorial

# while True:
#     num = int(input("Ingrese un número entero no negativo: "))
#     resultado = calcular_factorial(num)
#     print(f"El factorial de {num} es {resultado}")

#     continuar = input("¿Desea calcular el factorial de otro número? (s/n): ")
#     if continuar.lower() != "s":
#         break
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

