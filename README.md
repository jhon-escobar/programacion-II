# programacion-II

tecba

# Practica Nro 1 Calculadora Orientada a Objetos

En esta práctica se implementa una calculadora en Python que permite realizar operaciones aritméticas básicas como suma, resta, multiplicación y división.

Del mismo modo, se implementa una calculadora de factorial que aplica principios de herencia y polimorfismo.

## Preparación del entorno y ejecución

### 1. Clonar el repositorio:

```git
git clone https://github.com/yefeza/pg2-practica1.git
cd pg2-practica1
```

### 2. Crear un entorno virtual:

`python -m venv env`

### 3. Activar el entorno virtual:

#### En Windows:

`.\env\Scripts\activate`

#### En Linux o Mac:

`source env/bin/activate`

#### Ejecutar el script:

`python main.py`

#### Desactivar el entorno virtual:

`deactivate`

## Implementacion Calculadora Estandar

Este módulo implementa una calculadora estándar que permite realizar operaciones aritméticas básicas como suma, resta, multiplicación y división. El modo de funcionamiento es el siguiente:

```python
from calculadora_poo import Calculadora

calculadora_1 = Calculadora()

print(calculadora_1.sumar(2, 5))
print(calculadora_1.restar(10, 9))
print(calculadora_1.multiplicar(5, 9))
print(calculadora_1.dividir(150, 6))
```

## Implementacion Calculadora Factorial

Este módulo implementa una calculadora factorial que hereda de la clase Calculadora. Permite calcular el factorial de un número entero positivo. El modo de funcionamiento es el siguiente:

```python
from calculadora_poo import CalculadoraFactorial
calculadora_factorial = CalculadoraFactorial(numero=5)
print(calculadora_factorial.calcular())
```

---

**_abstraccion, enacpsulamiento, herencia y Polimorfismo_**

## Abstraccion

Este módulo implementa una calculadora estándar que permite realizar operaciones aritméticas básicas como suma, resta, multiplicación y división. El modo de funcionamiento es el siguiente:

```python
from ejercicio1 import Calculadora
from calculadora_factorial import CalculadoraFactorial
c = Calculadora ()
print(c.suma(45,25))
print(c.resta(46,45))
print(c.multiplicacion(75,85))
print(c.division(1546,13553))
cfact = CalculadoraFactorial(5)
print(cfact.Calculador())

```

---

## Implentacion

```Python
from ejercicio1 import Calculadora
from calculadora_factorial import CalculadoraFactorial

```

#### salida

```
Suma: 45 y 25 = 70
Resta: 46 y 45 = 1
Multiplicación: 75 y 85 = 6375
División: 1546 y 13553 = 0.11407068545709437
factorial: 5 = 120,
```

---

## Herencia

La herencia es una característica de los lenguajes de programación orientada a objetos que permite reutilizar código. Consiste en definir clases basadas en otras clases existentes.

```Python
from ejercicio1 import Calculadora
class CalculadoraFactorial(Calculadora):
    def __init__(self,numero):
        self.numero = numero
        super().__init__()

    def Calculador(self):
        self.operacion = "factorial"
        factorial = 1
        cont = 1
        while cont <= int(self.numero):
            factorial = self._multiplicar(factorial, cont)
            cont += 1

        self._resultado =factorial
        return self._mostrar_operacion()

    def _mostrar_operacion(self):
       return f"{self.operacion}: {self.numero} = {self._resultado}, "
```

---

# Polymorfismo

Es la capacidad de los objetos para adoptar diferentes formas. Esto permite que los objetos de una clase derivada sean tratados como objetos de una clase base.

```python
 def mostrar_operacion(self,a,b):
        return f"{self.operacion}: {a} y {b} = {self.resultado}"

```
