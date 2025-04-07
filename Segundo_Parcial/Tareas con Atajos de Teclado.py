import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Función para eliminar tarea
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Función para marcar tarea como completada
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        # Agregar "Completada" al final de la tarea para diferenciarla
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, task + " (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear la caja de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Crear los botones
add_button = tk.Button(root, text="Añadir tarea", width=20, command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como completada", width=20, command=mark_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar tarea", width=20, command=delete_task)
delete_button.pack(pady=5)

# Crear la lista de tareas
listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Asignar atajos de teclado
root.bind("<Return>", lambda event: add_task())  # "Enter" para añadir tarea
root.bind("<Delete>", lambda event: delete_task())  # "Delete" para eliminar tarea
root.bind("<c>", lambda event: mark_completed())  # "C" para marcar como completada
root.bind("<Escape>", lambda event: close_app())  # "Escape" para cerrar la aplicación

# Iniciar el bucle principal de la interfaz
root.mainloop()
