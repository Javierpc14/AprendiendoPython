
# Caso 1
# 		Realizar un programa que pida un número entero entre 1 y 10, ambos
# 		incluidos.
# 		Después se debe mostrar por pantalla el número introducido, pero en formato
# 		texto.
# 		Si el número introducido es 1 → La salida será: uno
# 		Si el número introducido es 2 → La salida será: dos
# 		......
# 		Si el número introducido es 10 → La salida será: diez
# 		Si el número introducido no está entre 1 y 10 → La salida será: número no
# 		válido

class Caso1:

    def __init__(self):
        self.num_entero = 0

    def pedir_datos(self):
        self.num_entero = int(input("Introduce un numero entero del 1 al 10: "))

    def mostrar_datos(self):
        match self.num_entero:
            case 1:
                print("Uno")
            case 2:
                print("Dos")
            case 3:
                print("Tres")
            case 4:
                print("Cuatro")
            case 5:
                print("Cinco")
            case 6:
                print("Seis")
            case 7:
                print("Siete")
            case 8:
                print("Ocho")
            case 9:
                print("Nueve")
            case 10:
                print("Diez")
            case _:
                print("Numero fuera del rango (debe ser entre 1 y 10)")
    
def main():
    caso1 = Caso1()
    caso1.pedir_datos()
    caso1.mostrar_datos()

if __name__ == "__main__":
    main()

