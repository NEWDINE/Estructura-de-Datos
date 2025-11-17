import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -------------------------------
# Ventana principal
# -------------------------------
ventana = tk.Tk()
ventana.title("Mapa Interactivo de México - Rutas entre Estados")
ventana.geometry("1000x700")
ventana.configure(bg="#FFD6E0")  # Rosita pastel 💗

# Crear figura con Basemap
fig, ax = plt.subplots(figsize=(7, 6))
m = Basemap(projection="merc",
            llcrnrlon=-118, llcrnrlat=14,
            urcrnrlon=-86, urcrnrlat=33,
            resolution="i", ax=ax)

m.drawmapboundary(fill_color="#E3F2FD")
m.fillcontinents(color="#FFE0F0", lake_color="#E3F2FD")
m.drawcountries(linewidth=1, color="#B56576")
m.drawstates(linewidth=0.8, color="#B56576")
m.drawcoastlines(linewidth=0.8, color="#B56576")

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# -------------------------------
# Crear grafo y datos base
# -------------------------------
grafo = nx.Graph()
posiciones = {}
costos = {
    ("CDMX", "Puebla"): 100,
    ("CDMX", "Morelos"): 80,
    ("CDMX", "Edo. México"): 60,
    ("Puebla", "Veracruz"): 150,
    ("Oaxaca", "Veracruz"): 250,
    ("Oaxaca", "Guerrero"): 180,
    ("Guerrero", "Morelos"): 120,
}

estados = {
    "CDMX": (19.43, -99.13),
    "Edo. México": (19.35, -99.75),
    "Puebla": (19.04, -98.20),
    "Veracruz": (19.17, -96.13),
    "Oaxaca": (17.06, -96.72),
    "Guerrero": (17.55, -99.50),
    "Morelos": (18.68, -99.10)
}

# -------------------------------
# Funciones
# -------------------------------
def dibujar_mapa(conexiones=None):
    ax.clear()
    m.drawmapboundary(fill_color="#E3F2FD")
    m.fillcontinents(color="#FFE0F0", lake_color="#E3F2FD")
    m.drawcountries(linewidth=1, color="#B56576")
    m.drawstates(linewidth=0.8, color="#B56576")
    m.drawcoastlines(linewidth=0.8, color="#B56576")

    # Dibuja los estados seleccionados
    for estado, (lat, lon) in estados.items():
        x, y = m(lon, lat)
        grafo.add_node(estado)
        posiciones[estado] = (x, y)
        color = "#F8BBD0" if seleccionados.get(estado, False) else "#FCE4EC"
        m.plot(lon, lat, 'o', markersize=10, color=color, markeredgecolor="#880E4F")
        plt.text(x, y, estado, fontsize=9, ha='left', color="#880E4F", fontweight="bold")

    # Dibuja las conexiones seleccionadas
    if conexiones:
        for (a, b) in conexiones:
            lat1, lon1 = estados[a]
            lat2, lon2 = estados[b]
            x1, y1 = m(lon1, lat1)
            x2, y2 = m(lon2, lat2)
            plt.plot([x1, x2], [y1, y2], color="#EC407A", linewidth=2)
            midx, midy = (x1+x2)/2, (y1+y2)/2
            plt.text(midx, midy, f"${costos[(a, b)]}", fontsize=8, color="#AD1457")

    canvas.draw()


def calcular_recorrido():
    seleccion = [e for e, var in seleccionados.items() if var.get()]
    if len(seleccion) < 2:
        messagebox.showwarning("Atención", "Selecciona al menos dos estados.")
        return

    total = 0
    conexiones_usadas = []
    for i in range(len(seleccion)-1):
        a, b = seleccion[i], seleccion[i+1]
        if (a, b) in costos:
            total += costos[(a, b)]
            conexiones_usadas.append((a, b))
        elif (b, a) in costos:
            total += costos[(b, a)]
            conexiones_usadas.append((b, a))
        else:
            messagebox.showinfo("Sin conexión", f"No hay ruta directa entre {a} y {b}")

    dibujar_mapa(conexiones_usadas)
    messagebox.showinfo("Resultado", f"Recorrido: {' → '.join(seleccion)}\nCosto total: ${total}")


# -------------------------------
# Panel derecho (selección)
# -------------------------------
frame = tk.Frame(ventana, bg="#FFD6E0")
frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

tk.Label(frame, text="Selecciona los estados a visitar", bg="#FFD6E0",
         fg="#880E4F", font=("Arial", 13, "bold")).pack(pady=10)

seleccionados = {}
for estado in estados.keys():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame, text=estado, variable=var,
                         bg="#FFD6E0", fg="#6A1B3B",
                         font=("Arial", 11))
    chk.pack(anchor="w")
    seleccionados[estado] = var

tk.Button(frame, text="Calcular recorrido", command=calcular_recorrido,
          bg="#F8BBD0", fg="#6A1B3B", font=("Arial", 12, "bold")).pack(pady=10, fill="x")

tk.Button(frame, text="Limpiar", command=lambda: dibujar_mapa(),
          bg="#F48FB1", fg="white", font=("Arial", 12, "bold")).pack(pady=10, fill="x")

tk.Button(frame, text="Salir", command=ventana.destroy,
          bg="#C2185B", fg="white", font=("Arial", 12, "bold")).pack(pady=10, fill="x")

# Mostrar mapa inicial
dibujar_mapa()

ventana.mainloop()