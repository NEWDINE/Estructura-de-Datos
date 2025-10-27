class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer:", self.customer)
        print("     Quantity:", self.qtty)
        print("     ------------")


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def size_(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return info

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print("   Size:", self.size)
        node = self.top
        count = 1
        while node:
            print("   ** Element", count)
            if isinstance(node.info, Order):
                node.info.print()
            node = node.next
            count += 1
        print("******************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size:
            return None
        node = self.top
        count = 1
        while node:
            if count == pos:
                return node.info
            node = node.next
            count += 1
        return None


if __name__ == "__main__":
    queue = LinkedQueue()
    o1 = Order(20, "Cliente1")
    o2 = Order(30, "Cliente2")
    o3 = Order(40, "Cliente3")
    o4 = Order(50, "Cliente4")

    print("\n=== ENQUEUE PEDIDOS ===")
    queue.enqueue(o1)
    queue.enqueue(o2)
    queue.enqueue(o3)
    queue.enqueue(o4)
    queue.print_info()

    print("\n=== FRONT ===")
    front = queue.front()
    if front:
        front.print()

    print("\n=== DEQUEUE ===")
    queue.dequeue()
    queue.print_info()

    print("\n=== GET NTH (3er elemento) ===")
    nth = queue.get_nth(3)
    if nth:
        nth.print()
    else:
        print("Posición inválida.")
