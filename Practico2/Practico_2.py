# Solicitar al usuario su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Clasificar la edad y mostrar el mensaje correspondiente
if edad < 13:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
else:  # Esto cubre la edad de 65 años o más
    print("Eres un adulto mayor.")

