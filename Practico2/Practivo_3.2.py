from datetime import date

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han ingresado ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print("La cantidad ingresada debe ser positiva.")

    def retirar_dinero(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes o cantidad no válida.")

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")


class CuentaJoven(CuentaBancaria):
    def __init__(self, titular, numero_cuenta, limite_extraccion=400000):
        saldo_inicial = 80000000  # Saldo inicial fijo para CuentaJoven
        if limite_extraccion > 400000:
            limite_extraccion = 400000  # Límite máximo de extracción permitido
            print("El límite de extracción para CuentaJoven ha sido establecido en $400,000.")
        super().__init__(titular, numero_cuenta, saldo_inicial)
        self.limite_extraccion = limite_extraccion
        self.ultimo_retiro_fecha = None
        self.ultimo_retiro_monto = 0

    def retirar_dinero(self, cantidad):
        # Obtener la fecha de hoy
        hoy = date.today()

        # Verificar si el retiro se realizó hoy y si ya se alcanzó el límite de extracción diario
        if self.ultimo_retiro_fecha == hoy and self.ultimo_retiro_monto >= self.limite_extraccion:
            print(f"Ya has alcanzado el límite de extracción de ${self.limite_extraccion} para hoy.")
            return

        # Limitar la cantidad retirada al límite de extracción si es necesario
        if cantidad > self.limite_extraccion:
            print(f"No se puede retirar más de ${self.limite_extraccion} por operación.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            self.ultimo_retiro_fecha = hoy
            self.ultimo_retiro_monto = cantidad
            print(f"Se han retirado ${cantidad}. Saldo actual: ${self.saldo}")


# Crear una cuenta interactiva sin preguntar el saldo inicial o el límite de extracción
titular = input("Ingrese el nombre del titular: ")
numero_cuenta = input("Ingrese el número de cuenta: ")
tipo_cuenta = input("Ingrese el tipo de cuenta ('normal' o 'joven'): ").lower()

if tipo_cuenta == 'joven':
    cuenta = CuentaJoven(titular, numero_cuenta)
else:
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cuenta = CuentaBancaria(titular, numero_cuenta, saldo_inicial)

# Ciclo de operaciones
while True:
    print("\nOpciones:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.ingresar_dinero(cantidad)
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar_dinero(cantidad)
    elif opcion == '3':
        cuenta.mostrar_saldo()
    elif opcion == '4':
        print("Gracias por utilizar el servicio bancario.")
        break
    else:
        print("Opción no válida, por favor intente nuevamente.")
