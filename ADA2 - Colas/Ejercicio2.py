class Cola:
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []
        self.contador = 0

    def encolar(self):
        self.contador += 1
        self.items.append(self.contador)
        print(f"Cliente {self.contador} agregado a la cola de {self.nombre}.")

    def atender(self):
        if self.items:
            cliente = self.items.pop(0)
            print(f"Atendiendo cliente {cliente} del servicio {self.nombre}.")
        else:
            print(f"No hay clientes en la cola de {self.nombre}.")

    def __str__(self):
        return f"{self.nombre}: {self.items}"


servicios = {
    "1": Cola("Autos"),
    "2": Cola("Salud"),
    "3": Cola("Vida")
}

print("=== SISTEMA DE COLAS — COMPAÑÍA DE SEGUROS ===\n")
print("Servicios disponibles:")
print("  1 → Seguros de Autos")
print("  2 → Seguros de Salud")
print("  3 → Seguros de Vida")
print("\nComandos:")
print("  C<num> → Llega un cliente (ejemplo: C1)")
print("  A<num> → Atender cliente (ejemplo: A1)")
print("  S → Salir del sistema\n")

while True:
    accion = input("Ingrese acción: ").upper()
    if accion == "S":
        print("\nSaliendo del sistema... Gracias.")
        break
    elif accion.startswith("C"):
        num = accion[1:]
        if num in servicios:
            servicios[num].encolar()
        else:
            print("Servicio no válido.")
    elif accion.startswith("A"):
        num = accion[1:]
        if num in servicios:
            servicios[num].atender()
        else:
            print("Servicio no válido.")
    else:
        print("Comando no reconocido.")

    print("\nEstado actual de las colas:")
    for s in servicios.values():
        print(s)
    print()
