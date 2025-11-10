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
ventana.title("Mapa Interactivo - Grafo de México")
ventana.geometry("950x700")

# Crear figura con Basemap
fig, ax = plt.subplots(figsize=(8, 7))
m = Basemap(projection="merc", llcrnrlon=-118, llcrnrlat=14, urcrnrlon=-86, urcrnrlat=33, resolution="i", ax=ax)
m.drawmapboundary(fill_color="#A6CAE0")
m.fillcontinents(color="#FFF3E0", lake_color="#A6CAE0")
m.drawcountries(linewidth=1)
m.drawstates(linewidth=0.5)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# -------------------------------
# Crear grafo y posiciones
# -------------------------------
grafo = nx.Graph()
posiciones = {}
costos = {}

# -------------------------------
# Funciones principales
# -------------------------------
def agregar_estado(nombre, lat, lon):
    if nombre in grafo.nodes:
        return
    x, y = m(lon, lat)
    grafo.add_node(nombre)
    posiciones[nombre] = (x, y)
    dibujar_grafo()

def conectar_estados(origen, destino, costo):
    grafo.add_edge(origen, destino, peso=costo)
    costos[(origen, destino)] = costo
    dibujar_grafo()

def dibujar_grafo():
    ax.clear()
    m.drawmapboundary(fill_color="#A6CAE0")
    m.fillcontinents(color="#FFF3E0", lake_color="#A6CAE0")
    m.drawcountries(linewidth=1)
    m.drawstates(linewidth=0.5)
    nx.draw(grafo, posiciones, with_labels=True, node_color="#A5D6A7", node_size=1800, font_size=9, ax=ax)
    etiquetas = nx.get_edge_attributes(grafo, 'peso')
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas, font_color='blue', ax=ax)
    canvas.draw()

# -------------------------------
# Cargar ejemplo con 7 estados
# -------------------------------
def ejemplo_mexico():
    grafo.clear()
    posiciones.clear()
    ax.clear()
    m.drawmapboundary(fill_color="#A6CAE0")
    m.fillcontinents(color="#FFF3E0", lake_color="#A6CAE0")
    m.drawcountries(linewidth=1)
    m.drawstates(linewidth=0.5)

    estados = {
        "Yucatán": (20.97, -89.62),
        "Campeche": (19.83, -90.53),
        "Quintana Roo": (19.57, -88.05),
        "Tabasco": (17.99, -92.93),
        "Chiapas": (16.75, -93.12),
        "Oaxaca": (17.06, -96.72),
        "Veracruz": (19.17, -96.13)
    }

    for e, (lat, lon) in estados.items():
        agregar_estado(e, lat, lon)

    conexiones = {
        ("Yucatán", "Campeche"): 300,
        ("Yucatán", "Quintana Roo"): 400,
        ("Campeche", "Tabasco"): 350,
        ("Tabasco", "Chiapas"): 250,
        ("Chiapas", "Oaxaca"): 300,
        ("Oaxaca", "Veracruz"): 400,
        ("Veracruz", "Tabasco"): 500,
        ("Campeche", "Chiapas"): 700,
        ("Quintana Roo", "Tabasco"): 600,
        ("Oaxaca", "Campeche"): 650,
        ("Veracruz", "Campeche"): 800
    }

    for (a, b), c in conexiones.items():
        conectar_estados(a, b, c)

    dibujar_grafo()

# -------------------------------
# Recorridos solicitados
# -------------------------------
def recorrido_sin_repetir():
    try:
        recorrido = list(nx.dfs_preorder_nodes(grafo, source="Yucatán"))
        costo_total = sum(grafo[recorrido[i]][recorrido[i+1]]['peso'] for i in range(len(recorrido)-1))
        messagebox.showinfo("Recorrido sin repetir", f"Ruta: {' → '.join(recorrido)}\nCosto total: {costo_total} km")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def recorrido_repetido():
    recorrido = ["Yucatán", "Campeche", "Tabasco", "Chiapas", "Oaxaca", "Veracruz", "Campeche", "Yucatán"]
    costo_total = 0
    for i in range(len(recorrido)-1):
        if grafo.has_edge(recorrido[i], recorrido[i+1]):
            costo_total += grafo[recorrido[i]][recorrido[i+1]]['peso']
    messagebox.showinfo("Recorrido con repetición", f"Ruta: {' → '.join(recorrido)}\nCosto total: {costo_total} km")

# -------------------------------
# Botones de control
# -------------------------------
frame = tk.Frame(ventana)
frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

tk.Button(frame, text="Ejemplo México", command=ejemplo_mexico, bg="#1976D2", fg="white", height=2).pack(pady=5, fill=tk.X)
tk.Button(frame, text="Recorrido sin repetir", command=recorrido_sin_repetir, bg="#388E3C", fg="white", height=2).pack(pady=5, fill=tk.X)
tk.Button(frame, text="Recorrido con repetición", command=recorrido_repetido, bg="#F57C00", fg="white", height=2).pack(pady=5, fill=tk.X)
tk.Button(frame, text="Salir", command=ventana.destroy, bg="#D32F2F", fg="white", height=2).pack(pady=10, fill=tk.X)

ventana.mainloop()
