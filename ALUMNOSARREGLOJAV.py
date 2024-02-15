import random
import tkinter as tk
from tkinter import ttk

class Alumno:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre

alumnos = [
    Alumno("Alumno {}".format(i), [0] * 6) for i in range(1, 101)
]

materias = [Materia("Materia {}".format(i)) for i in range(1, 7)]

for alumno in alumnos:
    for i in range(6):
        alumno.calificaciones[i] = random.randint(1, 100)

def display_calificaciones_alumnos():
    root = tk.Tk()
    root.title("Calificaciones de Alumnos")
    tree = ttk.Treeview(root)
    tree["columns"]=tuple([""]+["Materia {}".format(i) for i in range(1,7)])
    tree.heading("#0", text="Alumnos")
    for i in range(1,7):
        tree.heading("#{}".format(i), text="Materia {}".format(i))
    for alumno in alumnos:
        tree.insert("", tk.END, text=alumno.nombre, values=tuple([alumno.nombre]+alumno.calificaciones))
    tree.pack()
    root.mainloop()

def display_calificaciones_materias():
    root = tk.Tk()
    root.title("Calificaciones de Materias")
    tree = ttk.Treeview(root)
    tree["columns"]=tuple([""]+[alumno.nombre for alumno in alumnos])
    tree.heading("#0", text="Materias")
    for alumno in alumnos:
        tree.heading("#{}".format(alumnos.index(alumno)+1), text=alumno.nombre)
    for materia in materias:
        calificaciones_materia = []
        for alumno in alumnos:
            calificaciones_materia.append(alumno.calificaciones[materias.index(materia)])
        tree.insert("", tk.END, text=materia.nombre, values=tuple([""]+calificaciones_materia))
    tree.pack()
    root.mainloop()

def buscar_calificacion():
    while True:
        alumno_buscar = input("Ingrese el número de alumno que desea buscar (1-100), o 'exit' para salir: ")
        if alumno_buscar.lower() == 'exit':
            break
        try:
            num_alumno = int(alumno_buscar)
            if num_alumno < 1 or num_alumno > 100:
                print("Número de alumno fuera de rango. Por favor, ingrese un número entre 1 y 100.")
                continue
            alumno = alumnos[num_alumno - 1]
            materia_buscar = input("Ingrese el número de materia que desea buscar (1-6): ")
            num_materia = int(materia_buscar)
            if num_materia < 1 or num_materia > 6:
                print("Número de materia fuera de rango. Por favor, ingrese un número entre 1 y 6.")
                continue
            calificacion = alumno.calificaciones[num_materia - 1]
            print(f"\nAlumno: {alumno.nombre}")
            print(f"Materia: Materia {num_materia}")
            print(f"Calificación: {calificacion}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido o 'exit' para salir.")

display_calificaciones_alumnos()
display_calificaciones_materias()
buscar_calificacion()
