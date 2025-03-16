import tkinter as tk
from tkinter import messagebox


# Función para agregar información a la lista
def agregar():
    # Obtener el texto ingresado en el campo de texto
    texto = entry.get()

    # Verificar que el campo no esté vacío
    if texto:
        # Insertar el texto en la lista
        lista.insert(tk.END, texto)
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese algo para agregar.")


# Función para limpiar la información
def limpiar():
    entry.delete(0, tk.END)  # Limpiar el campo de texto
    lista.delete(0, tk.END)  # Limpiar la lista


# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Gestión de Información")

# Crear el marco principal
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Etiqueta descriptiva
label = tk.Label(frame, text="Ingrese información para agregar:")
label.grid(row=0, column=0, padx=5, pady=5)

# Campo de texto para la entrada de datos
entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5, pady=5)

# Botón para agregar información
btn_agregar = tk.Button(frame, text="Agregar", command=agregar)
btn_agregar.grid(row=1, column=0, columnspan=2, pady=10)

# Lista para mostrar los datos agregados
lista = tk.Listbox(frame, width=40, height=10)
lista.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Botón para limpiar los datos
btn_limpiar = tk.Button(frame, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
