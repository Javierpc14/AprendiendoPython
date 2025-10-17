# Pedir al usuario que introduzca 3 numeros A, B y C, multiplicar B * C y dividirlo entre A

class Caso3:
    
    def __init__(self):
        self.numA = 0
        self.numB = 0
        self.numC = 0
        self.resultado = 0

    def pedir_datos(self):
        self.numA = int(input("Introduce el primer numero (A) "))
        self.numB = int(input("Introduce el segundo numero (B) "))
        self.numC = int(input("Introduce el tercer numero (C) "))
    
    def operacion(self):
        self.resultado = (self.numA * self.numB) / self.numC
    
    def mostrar_datos(self):
        print("El resultado es: ", self.resultado)

def main():
    caso3 = Caso3()
    caso3.pedir_datos()
    caso3.operacion()
    caso3.mostrar_datos()

if __name__ == "__main__":
    main()
