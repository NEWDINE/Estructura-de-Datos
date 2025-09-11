# Sistema de Farmacia Delta Corps - POO

class Medicamento:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = cantidad * self.precio
            return total
        else:
            print("No hay suficiente stock disponible.")
            return 0

    def modificar(self, nombre=None, precio=None, stock=None):
        if nombre:
            self.nombre = nombre
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

class Inventario:
    def __init__(self):
        self.medicamentos = {}

    def agregar_medicamento(self, medicamento):
        self.medicamentos[medicamento.nombre] = medicamento
        print(f"Medicamento {medicamento.nombre} agregado al inventario.")

    def modificar_medicamento(self, nombre):
        if nombre in self.medicamentos:
            med = self.medicamentos[nombre]
            print(f"Modificando {nombre}:")
            nuevo_nombre = input("Nuevo nombre (dejar vacío si no cambia): ")
            nuevo_precio = input("Nuevo precio (dejar vacío si no cambia): ")
            nuevo_stock = input("Nuevo stock (dejar vacío si no cambia): ")
            med.modificar(
                nombre=nuevo_nombre if nuevo_nombre else None,
                precio=float(nuevo_precio) if nuevo_precio else None,
                stock=int(nuevo_stock) if nuevo_stock else None
            )
            if nuevo_nombre:
                self.medicamentos[nuevo_nombre] = self.medicamentos.pop(nombre)
            print("Medicamento modificado correctamente.")
        else:
            print("Medicamento no encontrado.")

    def mostrar_inventario(self):
        print("\n--- Inventario de Medicamentos ---")
        if not self.medicamentos:
            print("No hay medicamentos registrados.")
        for med in self.medicamentos.values():
            print(f"{med.nombre} - Precio: ${med.precio} - Stock: {med.stock}")

    def vender_medicamento(self, nombre, cantidad):
        if nombre in self.medicamentos:
            return self.medicamentos[nombre].vender(cantidad)
        else:
            print("Medicamento no encontrado.")
            return 0

class Farmacia:
    def __init__(self):
        self.inventario = Inventario()
        self.ventas_medicamentos = []
        self.consultas = []

    # Ventas de medicamentos
    def vender_medicamento(self, nombre, cantidad):
        total = self.inventario.vender_medicamento(nombre, cantidad)
        if total > 0:
            ticket = {"nombre": nombre, "cantidad": cantidad, "total": total}
            self.ventas_medicamentos.append(ticket)
            print(f"Venta registrada: {cantidad} x {nombre} = ${total}")
            print(f"Ticket generado: {ticket}")

    # Consultas médicas
    def registrar_consulta(self, cliente, motivo):
        ticket = {"cliente": cliente, "motivo": motivo}
        self.consultas.append(ticket)
        print(f"Consulta registrada para {cliente}, motivo: {motivo}")
        print(f"Ticket de consulta: {ticket}")

    # Ver tickets de ventas
    def mostrar_tickets_ventas(self):
        print("\n--- Tickets de Ventas de Medicamentos ---")
        if not self.ventas_medicamentos:
            print("No hay tickets de ventas.")
            return
        for i, ticket in enumerate(self.ventas_medicamentos, 1):
            print(f"{i}. {ticket['cantidad']} x {ticket['nombre']} = ${ticket['total']}")

    # Ver tickets de consultas
    def mostrar_tickets_consultas(self):
        print("\n--- Tickets de Consultas Médicas ---")
        if not self.consultas:
            print("No hay tickets de consultas.")
            return
        for i, ticket in enumerate(self.consultas, 1):
            print(f"{i}. Cliente: {ticket['cliente']}, Motivo: {ticket['motivo']}")

    # Reporte de ventas y consultas
    def mostrar_reporte(self):
        print("\n--- Reporte de Medicamentos Vendidos ---")
        total_general = 0
        if not self.ventas_medicamentos:
            print("No se han registrado ventas de medicamentos.")
        for venta in self.ventas_medicamentos:
            print(f"{venta['cantidad']} x {venta['nombre']} = ${venta['total']}")
            total_general += venta['total']
        print(f"Total vendido en medicamentos: ${total_general}")

        print("\n--- Reporte de Consultas Médicas ---")
        if not self.consultas:
            print("No se han registrado consultas médicas.")
        for consulta in self.consultas:
            print(f"Cliente: {consulta['cliente']}, Motivo: {consulta['motivo']}")

def main():
    farmacia = Farmacia()

    # Opcional: agregar medicamentos iniciales
    farmacia.inventario.agregar_medicamento(Medicamento("Paracetamol", 20, 50))
    farmacia.inventario.agregar_medicamento(Medicamento("Ibuprofeno", 35, 30))
    farmacia.inventario.agregar_medicamento(Medicamento("Amoxicilina", 50, 20))

    while True:
        print("\n--- Menú Sistema Farmacia Delta Corps ---")
        print("1. Inventario")
        print("2. Ventas de medicamentos")
        print("3. Consultas médicas")
        print("4. Tickets")
        print("5. Reporte de ventas y consultas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Inventario ---")
            print("1. Agregar medicamento")
            print("2. Modificar medicamento")
            print("3. Ver lista de medicamentos")
            sub_opcion = input("Seleccione opción: ")
            if sub_opcion == "1":
                nombre = input("Nombre del medicamento: ")
                precio = float(input("Precio: "))
                stock = int(input("Cantidad en stock: "))
                farmacia.inventario.agregar_medicamento(Medicamento(nombre, precio, stock))
            elif sub_opcion == "2":
                nombre = input("Ingrese el nombre del medicamento a modificar: ")
                farmacia.inventario.modificar_medicamento(nombre)
            elif sub_opcion == "3":
                farmacia.inventario.mostrar_inventario()
            else:
                print("Opción inválida.")
        elif opcion == "2":
            nombre = input("Nombre del medicamento a vender: ")
            cantidad = int(input("Cantidad: "))
            farmacia.vender_medicamento(nombre, cantidad)
        elif opcion == "3":
            cliente = input("Nombre del cliente: ")
            motivo = input("Motivo de la consulta: ")
            farmacia.registrar_consulta(cliente, motivo)
        elif opcion == "4":
            print("\n1. Ver tickets de ventas")
            print("2. Ver tickets de consultas")
            sub_opcion = input("Seleccione opción: ")
            if sub_opcion == "1":
                farmacia.mostrar_tickets_ventas()
            elif sub_opcion == "2":
                farmacia.mostrar_tickets_consultas()
            else:
                print("Opción inválida.")
        elif opcion == "5":
            farmacia.mostrar_reporte()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":

    main()
