import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import time

class PilaVisual:
    def __init__(self, ventana):
        self.items = []
        self.ventana = ventana
        self.canvas = tk.Canvas(ventana, width=300, height=500, bg="#1e1e2f", highlightthickness=0)
        self.canvas.pack(pady=20)

    def dibujar(self):
        self.canvas.delete("all")
        x1, y1, x2, y2 = 80, 50, 220, 100  # espacio para la cima (arriba)

        for i, item in enumerate(reversed(self.items)):
            # Dibujar el bloque
            self.canvas.create_rectangle(
                x1, y1, x2, y2, 
                fill="#4db6ac", outline="white", width=2
            )
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, 
                                    text=str(item), fill="white", font=("Segoe UI", 12, "bold"))
            
            # Dibujar indicador de cima SOLO en el primer bloque
            if i == 0:
                self.canvas.create_text(x2 + 30, (y1 + y2) / 2, 
                                        text="↑ CIMA", fill="red", font=("Segoe UI", 11, "bold"))

            y1 += 60
            y2 += 60

    def animar_apilar(self, elemento):
        if elemento:
            self.items.append(elemento)
            for _ in range(5):  # animación ligera
                self.dibujar()
                self.canvas.update()
                time.sleep(0.03)

    def animar_desapilar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            self.dibujar()
            self.canvas.update()
            messagebox.showinfo("Desapilado", f"✗ Se eliminó: {elemento}")
            return elemento
        else:
            messagebox.showwarning("Pila vacía", "No hay elementos en la pila")
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return "Pila vacía"

    def esta_vacia(self):
        return len(self.items) == 0

def main():
    ventana = tk.Tk()
    ventana.title("Simulación de Pila")
    ventana.geometry("350x600")
    ventana.configure(bg="#121212")

    style = ttk.Style()
    style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)

    pila = PilaVisual(ventana)

    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=15)

    btn_apilar = ttk.Button(frame_botones, text="Apilar", width=14, 
                            command=lambda: pila.animar_apilar(simpledialog.askstring("Apilar", "Ingresa el elemento:")))
    btn_apilar.grid(row=0, column=0, padx=10, pady=5)

    btn_desapilar = ttk.Button(frame_botones, text="Desapilar", width=14, command=pila.animar_desapilar)
    btn_desapilar.grid(row=0, column=1, padx=10, pady=5)

    btn_cima = ttk.Button(frame_botones, text="Ver cima", width=14, 
                          command=lambda: messagebox.showinfo("Cima", f"Elemento en cima: {pila.cima()}"))
    btn_cima.grid(row=1, column=0, padx=10, pady=5)

    btn_salir = ttk.Button(frame_botones, text="Salir", width=14, command=ventana.quit)
    btn_salir.grid(row=1, column=1, padx=10, pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    main()
