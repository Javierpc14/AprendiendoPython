# crear un programa que pregunte al usuario su nombre y sus dos apellidos e imprimir por pantalla como se llama

class Caso2:
    
    def main():
        persona = Caso2()
        persona.pedir_datos()
        persona.mostrar_datos()

    if __name__ == "__main__":
        main()

    def __init__(self):
        self.nombre = ""
        self.ape1 = ""
        self.ape2 = ""

    def pedir_datos(self):
        self.nombre = input("Introduce tu nombre")
        self.ape1 = input("Introduce tu primer apellido")
        self.ape2 = input("Introduce tu segundo apellido")

    def mostrar_datos(self):
        print("Te llamas", self.nombre, self.ape1, self.ape2)
        print("Nombre:", self.nombre)
        print("Primer apellido:", self.ape1)
        print("segundo apellido:", self.ape2)