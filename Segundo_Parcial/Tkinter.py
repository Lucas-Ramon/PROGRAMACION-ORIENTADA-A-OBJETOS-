import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")

        # Frame para la lista de eventos
        self.eventos_frame = ttk.Frame(root)
        self.eventos_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.eventos_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para la entrada de datos
        self.entrada_frame = ttk.Frame(root)
        self.entrada_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.entrada_frame, text="Fecha:").grid(row=0, column=0, sticky=tk.W)
        self.fecha_entry = tkcalendar.DateEntry(self.entrada_frame)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.entrada_frame, text="Hora:").grid(row=1, column=0, sticky=tk.W)
        self.hora_entry = ttk.Entry(self.entrada_frame)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.entrada_frame, text="Descripción:").grid(row=2, column=0, sticky=tk.W)
        self.descripcion_entry = ttk.Entry(self.entrada_frame)
        self.descripcion_entry.grid(row=2, column=1)

        # Frame para los botones
        self.botones_frame = ttk.Frame(root)
        self.botones_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Button(self.botones_frame, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT)
        ttk.Button(self.botones_frame, text="Eliminar Evento", command=self.eliminar_evento).pack(side=tk.LEFT)
        ttk.Button(self.botones_frame, text="Salir", command=root.quit).pack(side=tk.LEFT)

        self.eventos = []

    def agregar_evento(self):
        fecha = self.fecha_entry.get_date()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.eventos.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})
            self.actualizar_lista()
            self.limpiar_entradas()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el evento seleccionado?"):
                item = seleccion[0]
                index = int(item[1:]) - 1
                del self.eventos[index]
                self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Seleccione un evento para eliminar.")

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for evento in self.eventos:
            self.tree.insert("", tk.END, values=(evento["fecha"], evento["hora"], evento["descripcion"]))

    def limpiar_entradas(self):
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()