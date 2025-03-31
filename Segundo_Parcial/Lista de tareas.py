import tkinter as tk
from tkinter import ttk

class AplicacionListaTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Tareas")

        self.tareas = []

        # Campo de entrada para nuevas tareas
        self.entrada_tarea = ttk.Entry(ventana, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botones
        self.boton_agregar = ttk.Button(ventana, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=1, padx=5, pady=10)

        self.boton_completar = ttk.Button(ventana, text="Marcar como Completada", command=self.marcar_como_completada)
        self.boton_completar.grid(row=1, column=1, padx=5, pady=5)

        self.boton_eliminar = ttk.Button(ventana, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

        # Lista de tareas
        self.lista_tareas = ttk.Treeview(ventana, columns=("Tarea", "Estado"), show="headings")
        self.lista_tareas.heading("Tarea", text="Tarea")
        self.lista_tareas.heading("Estado", text="Estado")
        self.lista_tareas.grid(row=1, column=0, rowspan=3, padx=10, pady=5)

        # Manejo de eventos
        self.entrada_tarea.bind("<Return>", lambda event: self.agregar_tarea())
        self.lista_tareas.bind("<Double-1>", lambda event: self.marcar_como_completada())

        # Actualizar la lista de tareas
        self.actualizar_lista_tareas()

    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append({"tarea": tarea, "estado": "Pendiente"})
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista_tareas()

    def marcar_como_completada(self):
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = int(seleccion[0][1:], 16) - 1
            self.tareas[indice]["estado"] = "Completada"
            self.actualizar_lista_tareas()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = int(seleccion[0][1:], 16) - 1
            del self.tareas[indice]
            self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        # Limpiar la lista de tareas
        for item in self.lista_tareas.get_children():
            self.lista_tareas.delete(item)

        # Insertar las tareas actualizadas
        for tarea in self.tareas:
            self.lista_tareas.insert("", tk.END, values=(tarea["tarea"], tarea["estado"]))

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionListaTareas(ventana)
    ventana.mainloop()