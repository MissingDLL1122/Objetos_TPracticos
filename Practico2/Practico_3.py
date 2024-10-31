class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando. ¡Guau, guau!")

    def jugar(self):
        print(f"{self.nombre} quiere jugar.")

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Crear un objeto de la clase Perro
mi_perro = Perro("Fido", 3, "Labrador")

# Utilizar los métodos del objeto
mi_perro.ladrar()
mi_perro.jugar()
mi_perro.comer()

# Obtener y mostrar la edad del perro
print(f"La edad de {mi_perro.nombre} es {mi_perro.edad} años.")
