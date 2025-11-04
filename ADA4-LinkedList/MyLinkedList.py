class Node:
    contador_id = 1

    def __init__(self, valor):
        self.id = Node.contador_id
        Node.contador_id += 1
        self.valor = valor
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def vacia(self):
        return self.head is None

    def agregar(self, valor):
        nuevo = Node(valor)
        if self.vacia():
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    def buscar_por_id(self, id):
        actual = self.head
        while actual:
            if actual.id == id:
                return actual
            actual = actual.next
        return None

    def eliminar_por_id(self, id):
        if self.vacia():
            return False
        if self.head.id == id:
            self.head = self.head.next
            self.size -= 1
            return True
        actual = self.head
        while actual.next and actual.next.id != id:
            actual = actual.next
        if actual.next:
            actual.next = actual.next.next
            self.size -= 1
            return True
        return False

    def actualizar(self, id, nuevo_valor):
        nodo = self.buscar_por_id(id)
        if nodo:
            nodo.valor = nuevo_valor
            return True
        return False

    def mostrar(self):
        if self.vacia():
            print("Lista vacía.")
            return
        actual = self.head
        print(f"{'ID':<5} | {'VALOR':<10}")
        print("-" * 18)
        while actual:
            print(f"{actual.id:<5} | {str(actual.valor):<10}")
            actual = actual.next

    def longitud(self):
        return self.size
