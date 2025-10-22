#pedir al usuario los nombres de 4 alumnos con sus notas y mostrar la nota media de la clase y un listado de lso alumnos

class Caso5:

    def __init__(self):
        self.nom1 = ""
        self.nom2 = ""
        self.nom3 = ""
        self.nom4 = ""

        self.nota1 = 0.0
        self.nota2 = 0.0
        self.nota3 = 0.0
        self.nota4 = 0.0
        self.media = 0.0

    def pedir_datos(self):
        self.nom1 = input("Introduce el nombre del alumno 1: ")
        self.nota1 = float(input("Introduce la nota del alumno 1: "))

        self.nom2 = input("Introduce el nombre del alumno 2: ")
        self.nota2 = float(input("Introduce la nota del alumno 2: "))

        self.nom3 = input("Introduce el nombre del alumno 3: ")
        self.nota3 = float(input("Introduce la nota del alumno 3: "))

        self.nom4 = input("Introduce el nombre del alumno 4: ")
        self.nota4 = float(input("Introduce la nota del alumno 4: "))

    def calcular_media(self):
        self.media = ((self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4)

    def mostrar_datos(self):
        print("La nota media de la clase es: ",self.media)
        print("El listado de la clase es:\n"
        "Alumno 1:",self.nom1,", nota:",self.nota1, "\n"
        "Alumno 2:",self.nom2,", nota:",self.nota2, "\n"
        "Alumno 3:",self.nom3,", nota:",self.nota3, "\n"
        "Alumno 4:",self.nom4,", nota:",self.nota4)
    
def main():
    caso5 = Caso5()
    caso5.pedir_datos()
    caso5.calcular_media()
    caso5.mostrar_datos()

if __name__ == "__main__":
    main()
