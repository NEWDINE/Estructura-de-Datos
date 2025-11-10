import tkinter as tk
from tkinter import ttk, messagebox
import math
import itertools
import uuid

# ---------- Estructuras internas: Vertice y Arista ----------
class Vertice:
    def __init__(self, id_, obj=None, x=0, y=0):
        self.id = id_            # identificador único (int)
        self.obj = obj           # objeto almacenable
        self.x = x               # posición para visualización
        self.y = y
        self.canvas_nodes = {}   # referencias gráficas (oval, text)

class Arista:
    def __init__(self, id_, v1, v2, obj=None, dirigida=False):
        self.id = id_            # identificador único
        self.v1 = v1             # id vertice origen (int)
        self.v2 = v2             # id vertice destino (int)
        self.obj = obj
        self.dirigida = dirigida # bool
        self.canvas_items = []   # ids gráficos en canvas

# ---------- Clase Grafo con todas las operaciones solicitadas ----------
class Grafo:
    def __init__(self):
        self._vertices = {}   # id -> Vertice
        self._aristas = {}    # id -> Arista
        self._next_vid = 1
        self._next_eid = 1

    # --- Operaciones generales ---
    def numVertices(self):
        return len(self._vertices)

    def numAristas(self):
        return len(self._aristas)

    def vertices(self):
        return list(self._vertices.keys())

    def aristas(self):
        return list(self._aristas.keys())

    def grado(self, v):
        # grado en grafo no dirigido considera aristas no dirigidas + in/out si dirigida (sum total)
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        g = 0
        for e in self._aristas.values():
            if e.v1 == v or e.v2 == v:
                g += 1
        return g

    def verticesAdyacentes(self, v):
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        vecinos = set()
        for e in self._aristas.values():
            if e.v1 == v:
                vecinos.add(e.v2)
            elif e.v2 == v:
                vecinos.add(e.v1)
        return list(vecinos)

    def aristasIncidentes(self, v):
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        res = []
        for eid, e in self._aristas.items():
            if e.v1 == v or e.v2 == v:
                res.append(eid)
        return res

    def verticesFinales(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        return [ar.v1, ar.v2]

    def opuesto(self, v, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        if ar.v1 == v:
            return ar.v2
        if ar.v2 == v:
            return ar.v1
        raise ValueError("El vértice no pertenece a la arista")

    def esAdyacente(self, v, w):
        # adyacente si existe arista entre v y w (cualquiera de las dos orientaciones)
        for e in self._aristas.values():
            if (e.v1 == v and e.v2 == w) or (e.v1 == w and e.v2 == v):
                return True
        return False

    # --- Operaciones con aristas dirigidas ---
    def aristasDirigidas(self):
        return [eid for eid, e in self._aristas.items() if e.dirigida]

    def aristasNodirigidas(self):
        return [eid for eid, e in self._aristas.items() if not e.dirigida]

    def gradoEnt(self, v):
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        return sum(1 for e in self._aristas.values() if e.dirigida and e.v2 == v)

    def gradoSalida(self, v):
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        return sum(1 for e in self._aristas.values() if e.dirigida and e.v1 == v)

    def aristasIncidentesEnt(self, v):
        return [eid for eid, e in self._aristas.items() if e.dirigida and e.v2 == v]

    def aristasIncidentesSal(self, v):
        return [eid for eid, e in self._aristas.items() if e.dirigida and e.v1 == v]

    def verticesAdyacentesEnt(self, v):
        # vértices que entran a v (orígenes de aristas dirigidas hacia v)
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        return list({e.v1 for e in self._aristas.values() if e.dirigida and e.v2 == v})

    def verticesAdyacentesSal(self, v):
        # vértices destino desde v (salida)
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        return list({e.v2 for e in self._aristas.values() if e.dirigida and e.v1 == v})

    def destino(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        if not ar.dirigida:
            raise ValueError("Arista no es dirigida")
        return ar.v2

    def origen(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        if not ar.dirigida:
            raise ValueError("Arista no es dirigida")
        return ar.v1

    def esDirigida(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        return self._aristas[e].dirigida

    # --- Operaciones para actualizar grafos ---
    def insertaVertice(self, obj=None, x=0, y=0):
        vid = self._next_vid
        self._next_vid += 1
        v = Vertice(vid, obj=obj, x=x, y=y)
        self._vertices[vid] = v
        return vid

    def eliminaVertice(self, v):
        if v not in self._vertices:
            raise KeyError("Vertice no existe")
        # eliminar aristas incidentes
        to_delete = [eid for eid, e in self._aristas.items() if e.v1 == v or e.v2 == v]
        for eid in to_delete:
            del self._aristas[eid]
        del self._vertices[v]

    def insertaArista(self, v, w, obj=None):
        return self._inserta_arista_generica(v, w, obj=obj, dirigida=False)

    def insertaAristaDirigida(self, v, w, obj=None):
        return self._inserta_arista_generica(v, w, obj=obj, dirigida=True)

    def _inserta_arista_generica(self, v, w, obj=None, dirigida=False):
        if v not in self._vertices or w not in self._vertices:
            raise KeyError("Vertice origen o destino no existe")
        # permitir multiaristas (no impide duplicados)
        eid = self._next_eid
        self._next_eid += 1
        a = Arista(eid, v, w, obj=obj, dirigida=dirigida)
        self._aristas[eid] = a
        return eid

    def eliminaArista(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        del self._aristas[e]

    def convierteNoDirigida(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        self._aristas[e].dirigida = False

    def invierteDireccion(self, e):
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        ar.v1, ar.v2 = ar.v2, ar.v1

    def asignaDireccionDesde(self, e, v):
        # hace que la arista e sea dirigida saliendo de v (v debe ser extremo)
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        if v != ar.v1 and v != ar.v2:
            raise ValueError("El vértice no es extremo de la arista")
        ar.dirigida = True
        if v == ar.v2:
            # queremos que salga de v, así que invertimos
            ar.v1, ar.v2 = ar.v2, ar.v1

    def asignaDireccionA(self, e, v):
        # hace que la arista e sea dirigida hacia v (v debe ser extremo)
        if e not in self._aristas:
            raise KeyError("Arista no existe")
        ar = self._aristas[e]
        if v != ar.v1 and v != ar.v2:
            raise ValueError("El vértice no es extremo de la arista")
        ar.dirigida = True
        if v == ar.v1:
            # queremos que llegue a v, por lo que invertimos para que v sea v2
            ar.v1, ar.v2 = ar.v2, ar.v1

    # utilitarios
    def get_vertice(self, v):
        return self._vertices.get(v)

    def get_arista(self, e):
        return self._aristas.get(e)

    def tipoGrafo(self):
        # decide si el grafo es: "No dirigido", "Dirigido", "Mixto"
        any_dir = any(e.dirigida for e in self._aristas.values())
        any_nodir = any(not e.dirigida for e in self._aristas.values())
        if any_dir and not any_nodir:
            return "Dirigido"
        if any_nodir and not any_dir:
            return "No dirigido"
        if not any_dir and not any_nodir:
            return "Vacío"
        return "Mixto"

# ---------- Interfaz Tkinter para visualizar e interactuar ----------
class GrafoApp:
    RADIUS = 20

    def __init__(self, root):
        self.root = root
        root.title("Grafo - Visualizador (Tkinter)")

        self.grafo = Grafo()

        # layout: canvas a la izquierda, panel de controles a la derecha
        self.frame_left = tk.Frame(root)
        self.frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame_left, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.canvas_click)

        self.frame_right = tk.Frame(root, width=300)
        self.frame_right.pack(side=tk.RIGHT, fill=tk.Y)

        # Variables de control
        self.mode = tk.StringVar(value="select")  # select, add_vertex, add_edge, del_vertex, del_edge
        self.edge_dir = tk.BooleanVar(value=False)
        self.selected_vertex = None
        self.temp_edge_from = None

        self.create_controls()
        self.redraw_all()

    def create_controls(self):
        lbl = tk.Label(self.frame_right, text="Modo", font=("Arial", 12, "bold"))
        lbl.pack(pady=6)

        modes = [("Seleccionar", "select"), ("Agregar vértice", "add_vertex"),
                 ("Crear arista", "add_edge"), ("Eliminar vértice", "del_vertex"),
                 ("Eliminar arista", "del_edge"), ("Mover vértice", "move")]
        for text, val in modes:
            rb = tk.Radiobutton(self.frame_right, text=text, variable=self.mode, value=val)
            rb.pack(anchor="w")

        cb = tk.Checkbutton(self.frame_right, text="Dirigida (para nueva arista)", variable=self.edge_dir)
        cb.pack(anchor="w", pady=4)

        sep = ttk.Separator(self.frame_right, orient="horizontal")
        sep.pack(fill=tk.X, pady=6)

        btn_info = tk.Button(self.frame_right, text="Información del grafo", command=self.show_info)
        btn_info.pack(fill=tk.X, padx=6, pady=4)

        btn_clear = tk.Button(self.frame_right, text="Limpiar todo", command=self.clear_all)
        btn_clear.pack(fill=tk.X, padx=6, pady=4)

        btn_layout = tk.Button(self.frame_right, text="Auto-distribuir (círculo)", command=self.autolayout_circle)
        btn_layout.pack(fill=tk.X, padx=6, pady=4)

        btn_save = tk.Button(self.frame_right, text="Exportar lista (console)", command=self.export_console)
        btn_save.pack(fill=tk.X, padx=6, pady=4)

        sep2 = ttk.Separator(self.frame_right, orient="horizontal")
        sep2.pack(fill=tk.X, pady=6)

        lbl2 = tk.Label(self.frame_right, text="Acciones rápidas", font=("Arial", 11))
        lbl2.pack(pady=4)

        btn_degree = tk.Button(self.frame_right, text="Grado vértice seleccionado", command=self.show_degree_selected)
        btn_degree.pack(fill=tk.X, padx=6, pady=2)

        btn_neighbors = tk.Button(self.frame_right, text="Vecinos vértice seleccionado", command=self.show_neighbors_selected)
        btn_neighbors.pack(fill=tk.X, padx=6, pady=2)

        self.info_text = tk.Text(self.frame_right, height=12, width=36, wrap="word")
        self.info_text.pack(padx=6, pady=6)

        # Bindings for moving nodes
        self.canvas.bind("<B1-Motion>", self.canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.canvas_release)

    # ---------- UI actions ----------
    def canvas_click(self, event):
        mode = self.mode.get()
        x, y = event.x, event.y

        if mode == "add_vertex":
            vid = self.grafo.insertaVertice(obj=None, x=x, y=y)
            vert = self.grafo.get_vertice(vid)
            vert.x = x; vert.y = y
            self.redraw_all()
            self.info("Se agregó vértice id=%d" % vid)

        elif mode == "select":
            vid = self._vertex_at_pos(x, y)
            if vid:
                self.selected_vertex = vid
                self.info("Vértice seleccionado: %s" % vid)
            else:
                self.selected_vertex = None
                self.info("Ningún vértice seleccionado")

        elif mode == "add_edge":
            vid = self._vertex_at_pos(x, y)
            if not vid:
                self.info("Haz clic sobre un vértice para crear la arista.")
                return
            if self.temp_edge_from is None:
                self.temp_edge_from = vid
                self.info(f"Partir arista desde {vid}. Ahora clic en vértice destino.")
            else:
                v_from = self.temp_edge_from
                v_to = vid
                dirigida = self.edge_dir.get()
                try:
                    eid = self.grafo.insertaAristaDirigida(v_from, v_to) if dirigida else self.grafo.insertaArista(v_from, v_to)
                    self.info(f"Arista creada id={eid} ({'dirigida' if dirigida else 'no dirigida'}) {v_from} -> {v_to}")
                except Exception as ex:
                    self.info("Error al crear arista: " + str(ex))
                self.temp_edge_from = None
                self.redraw_all()

        elif mode == "del_vertex":
            vid = self._vertex_at_pos(x, y)
            if vid:
                try:
                    self.grafo.eliminaVertice(vid)
                    self.info(f"Vértice {vid} eliminado (y sus aristas incidentes).")
                    self.redraw_all()
                except Exception as ex:
                    self.info("Error: " + str(ex))
            else:
                self.info("Haz clic sobre un vértice para eliminarlo.")

        elif mode == "del_edge":
            # selecciona origen y destino en orden
            vid = self._vertex_at_pos(x, y)
            if not vid:
                self.info("Haz clic sobre un vértice (origen/destino).")
                return
            if self.temp_edge_from is None:
                self.temp_edge_from = vid
                self.info(f"Seleccionado origen {vid}. Ahora clic en destino de la arista a eliminar.")
            else:
                v_from = self.temp_edge_from
                v_to = vid
                # buscar aristas entre v_from y v_to (dirigida primero)
                found = None
                for eid, e in list(self.grafo._aristas.items()):
                    if e.v1 == v_from and e.v2 == v_to:
                        found = eid; break
                if found is None:
                    # si hay no dirigida entre ambos
                    for eid, e in list(self.grafo._aristas.items()):
                        if (not e.dirigida) and ((e.v1 == v_from and e.v2 == v_to) or (e.v1 == v_to and e.v2 == v_from)):
                            found = eid; break
                if found is None:
                    self.info("No se encontró arista entre %s y %s" % (v_from, v_to))
                else:
                    self.grafo.eliminaArista(found)
                    self.info(f"Arista {found} eliminada.")
                    self.redraw_all()
                self.temp_edge_from = None

        elif mode == "move":
            vid = self._vertex_at_pos(x, y)
            if vid:
                self.selected_vertex = vid
            else:
                self.selected_vertex = None

    def canvas_drag(self, event):
        if self.mode.get() != "move":
            return
        if self.selected_vertex is None:
            return
        # mover vértice
        v = self.grafo.get_vertice(self.selected_vertex)
        v.x = event.x; v.y = event.y
        self.redraw_all()

    def canvas_release(self, event):
        # terminar mover
        if self.mode.get() == "move":
            self.selected_vertex = None

    # ---------- Dibujo ----------
    def redraw_all(self):
        self.canvas.delete("all")
        # dibujar aristas primero
        for eid, e in self.grafo._aristas.items():
            v1 = self.grafo.get_vertice(e.v1)
            v2 = self.grafo.get_vertice(e.v2)
            if v1 is None or v2 is None:
                continue
            self._draw_edge(eid, v1.x, v1.y, v2.x, v2.y, e.dirigida)
        # dibujar vértices
        for vid, v in self.grafo._vertices.items():
            self._draw_vertex(vid, v.x, v.y)
        # actualizar info del panel
        self.update_info_panel()

    def _draw_vertex(self, vid, x, y):
        r = self.RADIUS
        oval = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#f0f0ff", outline="#444")
        txt = self.canvas.create_text(x, y, text=str(vid))
        # store ref
        v = self.grafo.get_vertice(vid)
        v.canvas_nodes['oval'] = oval
        v.canvas_nodes['text'] = txt

    def _draw_edge(self, eid, x1, y1, x2, y2, dirigida=False):
        # calcula línea desde borde a borde del círculo
        r = self.RADIUS
        dx = x2 - x1; dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist == 0:
            # la misma posición: dibujar un lazo
            x = x1; y = y1
            arc = self.canvas.create_arc(x-2*r, y-2*r, x+2*r, y+2*r, start=20, extent=300, style=tk.ARC)
            self.canvas.create_text(x+2*r, y-2*r, text=str(eid))
            return
        ux = dx / dist; uy = dy / dist
        startx = x1 + ux * r
        starty = y1 + uy * r
        endx = x2 - ux * r
        endy = y2 - uy * r
        line = self.canvas.create_line(startx, starty, endx, endy, width=2, arrow=tk.LAST if dirigida else tk.NONE, smooth=True)
        # opcional: etiqueta con id de arista en el centro
        mx = (startx + endx) / 2
        my = (starty + endy) / 2
        lbl = self.canvas.create_text(mx, my-10, text=str(eid), font=("Arial", 8))
        # store items
        ar = self.grafo.get_arista(eid)
        if ar:
            ar.canvas_items = [line, lbl]

    # ---------- util ----------
    def _vertex_at_pos(self, x, y):
        # devuelve id del vértice cuyo círculo contiene (x,y), si hay varios devuelve el primero
        for vid, v in self.grafo._vertices.items():
            dx = x - v.x; dy = y - v.y
            if dx*dx + dy*dy <= self.RADIUS*self.RADIUS:
                return vid
        return None

    def info(self, text):
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, text)

    def update_info_panel(self):
        tipo = self.grafo.tipoGrafo()
        info = f"Grafo: {tipo}\nVértices: {self.grafo.numVertices()}\nAristas: {self.grafo.numAristas()}\n\n"
        info += "Vertices IDs: " + ", ".join(map(str, self.grafo.vertices())) + "\n"
        info += "Aristas IDs: " + ", ".join(map(str, self.grafo.aristas())) + "\n"
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, info)

    # ---------- botones ----------
    def show_info(self):
        tipo = self.grafo.tipoGrafo()
        text = f"Tipo de grafo: {tipo}\nVertices: {self.grafo.numVertices()}\nAristas: {self.grafo.numAristas()}\n\n"
        text += "Lista de vértices y posiciones:\n"
        for vid, v in self.grafo._vertices.items():
            text += f"  {vid}: ({v.x},{v.y})\n"
        text += "\nAristas:\n"
        for eid, e in self.grafo._aristas.items():
            text += f"  {eid}: {e.v1} -> {e.v2} {'(dirigida)' if e.dirigida else '(no dirigida)'}\n"
        messagebox.showinfo("Información del grafo", text)

    def clear_all(self):
        if messagebox.askyesno("Confirmar", "¿Borrar grafo completo?"):
            self.grafo = Grafo()
            self.redraw_all()

    def autolayout_circle(self):
        n = self.grafo.numVertices()
        if n == 0:
            return
        cx = int(self.canvas.winfo_width()/2)
        cy = int(self.canvas.winfo_height()/2)
        R = min(cx, cy) - 80
        if R < 60: R = 200
        for i, vid in enumerate(self.grafo.vertices()):
            ang = 2*math.pi*i/n
            v = self.grafo.get_vertice(vid)
            v.x = cx + R*math.cos(ang)
            v.y = cy + R*math.sin(ang)
        self.redraw_all()

    def export_console(self):
        print("Vertices:")
        for vid, v in self.grafo._vertices.items():
            print(f"  {vid}: pos=({v.x},{v.y}) obj={v.obj}")
        print("Aristas:")
        for eid, e in self.grafo._aristas.items():
            print(f"  {eid}: {e.v1} -> {e.v2} {'dir' if e.dirigida else 'no-dir'} obj={e.obj}")
        messagebox.showinfo("Exportar", "Lista de vértices y aristas impresa en consola.")

    def show_degree_selected(self):
        if self.selected_vertex is None:
            self.info("Selecciona un vértice (modo seleccionar).")
            return
        try:
            g = self.grafo.grado(self.selected_vertex)
            ent = self.grafo.gradoEnt(self.selected_vertex)
            sal = self.grafo.gradoSalida(self.selected_vertex)
            self.info(f"Vértice {self.selected_vertex}\nGrado total: {g}\nGrado entrada: {ent}\nGrado salida: {sal}")
        except Exception as ex:
            self.info("Error: " + str(ex))

    def show_neighbors_selected(self):
        if self.selected_vertex is None:
            self.info("Selecciona un vértice (modo seleccionar).")
            return
        try:
            vecinos = self.grafo.verticesAdyacentes(self.selected_vertex)
            ent = self.grafo.verticesAdyacentesEnt(self.selected_vertex)
            sal = self.grafo.verticesAdyacentesSal(self.selected_vertex)
            self.info(f"Vértices adyacentes a {self.selected_vertex}:\nTodos: {vecinos}\nEntrantes: {ent}\nSalientes: {sal}")
        except Exception as ex:
            self.info("Error: " + str(ex))


# ---------- ejecutar aplicación ----------
def main():
    root = tk.Tk()
    app = GrafoApp(root)
    root.geometry("1150x650")
    root.mainloop()

if __name__ == "__main__":
    main()