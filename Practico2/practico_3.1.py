class Coche:
    def __init__(self, marca, modelo, año, color, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0  # Inicia con una velocidad de 0

    def acelerar(self, cantidad):
        # Incrementa la velocidad actual, pero no puede superar la velocidad máxima
        nueva_velocidad = self.velocidad_actual + cantidad
        if nueva_velocidad > self.velocidad_max:
            self.velocidad_actual = self.velocidad_max
            print(f"El coche ha alcanzado su velocidad máxima de {self.velocidad_max} km/h.")
        else:
            self.velocidad_actual = nueva_velocidad
            print(f"El coche ha acelerado a {self.velocidad_actual} km/h.")

    def frenar(self):
        # Establece la velocidad actual a 0
        self.velocidad_actual = 0
        print("El coche ha frenado y ahora está detenido.")

    def mostrar_info(self):
        # Muestra la información del coche
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Velocidad Máxima: {self.velocidad_max} km/h")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2020, "Rojo", 180)

# Simular un viaje
mi_coche.mostrar_info()
mi_coche.acelerar(60)
mi_coche.acelerar(80)
mi_coche.acelerar(50)  # Esto debería alcanzar o superar la velocidad máxima
mi_coche.frenar()
mi_coche.mostrar_info()  # Ver información final
