# 		Caso 2
# 		
# 		Realizar un programa que pida un número entero entre 1 y 10, ambos incluidos. Debe seguir pidiéndose mientras el número no esté en dicho intervalo.  
# 
# 		Después se debe mostrar por pantalla el número introducido, pero en formato texto.  
# 
# 		Si el número introducido es 1 → La salida será: uno Si el número introducido es 2 → La salida será: dos ...... 

class Caso2:

    def __init__(self):
        self.num = 0
        self.en_intervalo = True
    
    def pedir_datos(self):
        while self.en_intervalo:
            if(self.num <= 0 or self.num>= 10):
                self.num = int(input("Introduce un numero del 1 al 10: "))
            else:
                self.en_intervalo = False

    def mostrar_datos(self):
        match self.num:
            case 1:
                print("Uno")
                self.en_intervalo = False
            case 2:
                print("Dos")
                self.en_intervalo = False
            case 3:
                print("Tres")
                self.en_intervalo = False
            case 4:
                print("Cuatro")
                self.en_intervalo = False
            case 5:
                print("Cinco")
                self.en_intervalo = False
            case 6:
                print("Seis")
                self.en_intervalo = False
            case 7:
                print("Siete")
                self.en_intervalo = False
            case 8:
                print("Ocho")
                self.en_intervalo = False
            case 9:
                print("Nueve")
                self.en_intervalo = False
            case 10:
                print("Diez")
                self.en_intervalo = False
            case _:
                print("Numero fuera del rango (debe ser entre 1 y 10)")

def main():
    caso2 = Caso2()
    caso2.pedir_datos()
    caso2.mostrar_datos()

if __name__ == "__main__":
    main()

