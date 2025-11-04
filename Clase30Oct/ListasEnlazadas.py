import tkinter as tk
from tkinter import messagebox

class Ingrediente:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = []
    def agregar_ingrediente(self, ingrediente):
        if not ingrediente.nombre:
            return False
        for ing in self.ingredientes:
            if ing.nombre.lower() == ingrediente.nombre.lower():
                return False
        self.ingredientes.append(ingrediente)
        return True
    def eliminar_ingrediente(self, nombre_ing):
        for ing in self.ingredientes:
            if ing.nombre.lower() == nombre_ing.lower():
                self.ingredientes.remove(ing)
                return True
        return False
    def mostrar_ingredientes(self):
        if not self.ingredientes:
            return "Sin ingredientes"
        return ", ".join(str(i) for i in self.ingredientes)

class Nodo:
    def __init__(self, postre):
        self.postre = postre
        self.siguiente = None

class ListaPostres:
    def __init__(self):
        self.cabeza = None
    def insertar(self, postre):
        if self.buscar(postre.nombre):
            return False
        nuevo = Nodo(postre)
        if not self.cabeza or postre.nombre.lower() < self.cabeza.postre.nombre.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return True
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.postre.nombre.lower() < postre.nombre.lower():
            actual = actual.siguiente
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        return True
    def buscar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.postre.nombre.lower() == nombre.lower():
                return actual.postre
            actual = actual.siguiente
        return None
    def eliminar(self, nombre):
        actual = self.cabeza
        previo = None
        while actual and actual.postre.nombre.lower() != nombre.lower():
            previo = actual
            actual = actual.siguiente
        if not actual:
            return False
        if previo:
            previo.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente
        return True
    def recorrer(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual)
            actual = actual.siguiente
        return elementos
    def eliminar_repetidos(self):
        vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            nombre = actual.postre.nombre.lower()
            if nombre in vistos:
                previo.siguiente = actual.siguiente
            else:
                vistos.add(nombre)
                previo = actual
            actual = actual.siguiente

class App:
    def __init__(self, root):
        self.lista = ListaPostres()
        self.root = root
        self.root.title("Lista Enlazada de Postres 🍰")
        self.root.geometry("1250x640")
        self.root.config(bg="#f5f5dc")

        tk.Label(root, text="Nombre del Postre:", font=("Arial", 12), bg="#f5f5dc").pack()
        self.entrada_postre = tk.Entry(root, font=("Arial", 12), width=25)
        self.entrada_postre.pack(pady=5)

        frame_botones = tk.Frame(root, bg="#f5f5dc")
        frame_botones.pack(pady=5)

        tk.Button(frame_botones, text="Dar de Alta Postre", bg="#ffb347", command=self.agregar_postre).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Dar de Baja Postre", bg="#f08080", command=self.eliminar_postre).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Agregar Ingrediente", bg="#98fb98", command=self.agregar_ingrediente).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Eliminar Ingrediente", bg="#ff7f50", command=self.eliminar_ingrediente).grid(row=0, column=3, padx=5)
        tk.Button(frame_botones, text="Ver Ingredientes", bg="#f0e68c", command=self.ver_ingredientes).grid(row=0, column=4, padx=5)
        tk.Button(frame_botones, text="Eliminar Repetidos", bg="#afeeee", command=self.eliminar_repetidos).grid(row=0, column=5, padx=5)
        tk.Button(frame_botones, text="Recorrer Lista", bg="#dda0dd", command=self.dibujar).grid(row=0, column=6, padx=5)

        self.canvas = tk.Canvas(root, bg="white", width=1200, height=400)
        self.canvas.pack(pady=10)

    def agregar_postre(self):
        nombre = self.entrada_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese un nombre de postre.")
            return
        if not self.lista.insertar(Postre(nombre)):
            messagebox.showwarning("Duplicado", f"El postre '{nombre}' ya existe.")
            return
        messagebox.showinfo("Éxito", f"'{nombre}' agregado correctamente.")
        self.entrada_postre.delete(0, tk.END)
        self.dibujar()

    def eliminar_postre(self):
        nombre = self.entrada_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese el nombre del postre a eliminar.")
            return
        if self.lista.eliminar(nombre):
            messagebox.showinfo("Éxito", f"'{nombre}' eliminado correctamente.")
        else:
            messagebox.showwarning("Error", f"No se encontró '{nombre}'.")
        self.entrada_postre.delete(0, tk.END)
        self.dibujar()

    def agregar_ingrediente(self):
        nombre_postre = self.entrada_postre.get().strip()
        postre = self.lista.buscar(nombre_postre)
        if not postre:
            messagebox.showwarning("Error", f"No existe el postre '{nombre_postre}'.")
            return
        ventana = tk.Toplevel(self.root)
        ventana.title(f"Agregar ingrediente a {nombre_postre}")
        ventana.geometry("300x200")
        ventana.config(bg="#fff8dc")
        tk.Label(ventana, text="Nombre del ingrediente:", bg="#fff8dc").pack(pady=5)
        e_ing = tk.Entry(ventana)
        e_ing.pack(pady=5)
        def guardar():
            n_ing = e_ing.get().strip()
            if not n_ing:
                messagebox.showwarning("Error", "Ingrese un nombre de ingrediente.")
                return
            if postre.agregar_ingrediente(Ingrediente(n_ing)):
                messagebox.showinfo("Éxito", f"Ingrediente '{n_ing}' agregado a {postre.nombre}.")
            else:
                messagebox.showwarning("Duplicado", f"'{n_ing}' ya existe en {postre.nombre}.")
            ventana.destroy()
            self.dibujar()
        tk.Button(ventana, text="Guardar", bg="#90ee90", command=guardar).pack(pady=10)

    def eliminar_ingrediente(self):
        nombre_postre = self.entrada_postre.get().strip()
        postre = self.lista.buscar(nombre_postre)
        if not postre:
            messagebox.showwarning("Error", f"No existe el postre '{nombre_postre}'.")
            return
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Ingrediente")
        ventana.geometry("300x200")
        ventana.config(bg="#ffe4e1")
        tk.Label(ventana, text="Ingrediente a eliminar:", bg="#ffe4e1").pack(pady=5)
        e_ing = tk.Entry(ventana)
        e_ing.pack(pady=5)
        def eliminar():
            n_ing = e_ing.get().strip()
            if not n_ing:
                messagebox.showwarning("Error", "Ingrese un nombre de ingrediente.")
                return
            if postre.eliminar_ingrediente(n_ing):
                messagebox.showinfo("Eliminado", f"'{n_ing}' eliminado de {postre.nombre}.")
            else:
                messagebox.showwarning("No encontrado", f"No existe '{n_ing}' en {postre.nombre}.")
            ventana.destroy()
            self.dibujar()
        tk.Button(ventana, text="Eliminar", bg="#ff6347", command=eliminar).pack(pady=10)

    def ver_ingredientes(self):
        nombre = self.entrada_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese el nombre del postre.")
            return
        postre = self.lista.buscar(nombre)
        if not postre:
            messagebox.showwarning("Error", f"No existe el postre '{nombre}'.")
            return
        ingredientes = postre.mostrar_ingredientes()
        messagebox.showinfo("Ingredientes", f"{postre.nombre}:\n\n{ingredientes}")

    def eliminar_repetidos(self):
        if not self.lista.cabeza:
            messagebox.showwarning("Error", "La lista está vacía.")
            return
        self.lista.eliminar_repetidos()
        actual = self.lista.cabeza
        while actual:
            actual.postre.ingredientes = list({i.nombre.lower(): i for i in actual.postre.ingredientes}.values())
            actual = actual.siguiente
        messagebox.showinfo("Limpieza completada", "Se eliminaron los postres y ingredientes duplicados.")
        self.dibujar()

    def dibujar(self):
        self.canvas.delete("all")
        nodos = self.lista.recorrer()
        if not nodos:
            self.canvas.create_text(600, 200, text="Lista vacía", font=("Arial", 14, "italic"), fill="gray")
            return
        x, y = 100, 180
        for i, nodo in enumerate(nodos):
            p = nodo.postre
            dir_a = hex(id(nodo))
            dir_s = hex(id(nodo.siguiente)) if nodo.siguiente else "None"
            self.canvas.create_rectangle(x, y, x+240, y+100, fill="#ffebcd", outline="black")
            self.canvas.create_text(x+120, y+20, text=p.nombre, font=("Arial", 10, "bold"))
            self.canvas.create_text(x+120, y+50, text=p.mostrar_ingredientes(), font=("Arial", 8))
            self.canvas.create_text(x+120, y+80, text=f"{dir_a} → {dir_s}", font=("Arial", 7), fill="blue")
            if i < len(nodos)-1:
                self.canvas.create_line(x+240, y+50, x+280, y+50, arrow=tk.LAST, width=2)
            x += 280

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
