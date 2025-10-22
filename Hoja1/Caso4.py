#Pedir al usuario que introduzca los grados celsious por pantalla y se tiene que convertir ese valor a farenheit


# x grados centigrados son y grados farenheit
# 0 grados celsius = 32 farenheit
# formula F = (C * (9 / 5)) + 32

class Caso4:

    def __init__(self):
        self.gradosC = 0.0
        self.gradosF = 0.0

    def pedir_datos(self):
        self.gradosC = float(input("Introuduce los grados Celsius"))

    def realizar_operacion(self):
        self.gradosF = (self.gradosC * (9 / 5)) + 32

    def imprimir_datos(self):
        print("La conversion es: " , self.gradosC, "ºC y ", self.gradosF, " ºF")

def main():
        caso4 = Caso4()
        caso4.pedir_datos()
        caso4.realizar_operacion()
        caso4.imprimir_datos()

if __name__ == "__main__":
    main()
