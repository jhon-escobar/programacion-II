class Calculadora:
    def __init__(self):
        
        self.resultado = 0
        self.operacion = ""

    def suma(self,a,b):
        self.operacion = "Suma"
        
        self.resultado = a + b
        return self.mostrar_operacion(a,b)

    def resta(self,a,b):
        self.operacion = "Resta"
        self.resultado = a - b
        return self.mostrar_operacion(a,b)
    def _multiplicar(self,a,b):
        return a*b
    def multiplicacion(self,a ,b):
        self.operacion = "Multiplicación"
        self.resultado = self._multiplicar(a,b)
        return self.mostrar_operacion(a,b)

    def division(self,a,b):
        if b != 0:
            self.operacion = "División"
            self.resultado = a / b
        else:
            return "Error: División por cero"
        return self.mostrar_operacion(a,b)

    def mostrar_operacion(self,a,b):
        return f"{self.operacion}: {a} y {b} = {self.resultado}"

# c = Calculadora(5, 15)

# print(c.suma(), "|", c.resta(), "|", c.multiplicacion(), "|", c.division())