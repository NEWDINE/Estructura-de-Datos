import numpy as np
import time as time

inicio = time.time()

num_alumnos  = 1000000
num_materias = 6


rng = np.random.default_rng() 
matriz = rng.integers(0, 101, size=(num_alumnos, num_materias))


w_alumno = max(len(f"Alumno{num_alumnos}"), len("Alumno")) + 2
w_col    = max(len(f"Materia{num_materias}"), 3) + 2


print(f"{'':<{w_alumno}}", end="")
for j in range(num_materias):
    print(f"{'Materia'+str(j+1):>{w_col}}", end="")
print()


for i in range(num_alumnos):
    print(f"{'Alumno'+str(i+1):<{w_alumno}}", end="")
    for j in range(num_materias):
        print(f"{int(matriz[i, j]):>{w_col}}", end="")
    print()


al = int(input(f"\nAlumno a buscar (1..{num_alumnos}): "))
ma = int(input(f"Materia a buscar (1..{num_materias}): "))

if 1 <= al <= num_alumnos and 1 <= ma <= num_materias:
    cal = int(matriz[al - 1, ma - 1])
    print(f"\nCalificación de Alumno{al} en Materia{ma}: {cal}")
else:
    print("\nFuera de rango.")

fin = time.time()
print(f"\nTiempo total de ejecución: {fin - inicio:.6f} segundos")