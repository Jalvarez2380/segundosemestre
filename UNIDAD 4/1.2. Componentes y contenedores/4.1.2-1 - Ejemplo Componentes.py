import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar: pip install tkcalendar

# Función para agregar un nuevo evento a la lista
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        treeview.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)
    else:
        messagebox.showwarning("Selección vacía", "Por favor, selecciona un evento para eliminar.")

# Función para el menú de salida
def salir():
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("700x500")  # Ajusta la ventana para acomodar todos los componentes

# Panel para Controles de Entrada con borde, fondo y título
panel_entrada = tk.Frame(root, borderwidth=2, relief="groove", bg="light gray")
panel_entrada.pack(padx=10, pady=5, fill=tk.X)
titulo_entrada = tk.Label(panel_entrada, text="Agregar Nuevo Evento", bg="light gray")
titulo_entrada.pack(side=tk.TOP, fill=tk.X)

# Campo de fecha
tk.Label(panel_entrada, text="Fecha:", bg="light gray").pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
entry_fecha = DateEntry(panel_entrada, date_pattern='y-mm-dd', width=12)
entry_fecha.pack(side=tk.TOP, fill=tk.X, padx=5)

# Campo de hora
tk.Label(panel_entrada, text="Hora:", bg="light gray").pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
entry_hora = tk.Entry(panel_entrada)
entry_hora.pack(side=tk.TOP, fill=tk.X, padx=5)

# Campo de descripción
tk.Label(panel_entrada, text="Descripción:", bg="light gray").pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
entry_descripcion = tk.Entry(panel_entrada)
entry_descripcion.pack(side=tk.TOP, fill=tk.X, padx=5)

# Botones para agregar y eliminar eventos
panel_botones = tk.Frame(root, borderwidth=2, relief="groove", bg="light blue")
panel_botones.pack(padx=10, pady=5, fill=tk.X)
btn_agregar = tk.Button(panel_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side=tk.LEFT, padx=10, pady=10)

btn_eliminar = tk.Button(panel_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(side=tk.LEFT, padx=10, pady=10)

btn_salir = tk.Button(panel_botones, text="Salir", command=salir)
btn_salir.pack(side=tk.LEFT, padx=10, pady=10)

# Panel para lista de eventos (TreeView)
panel_lista = tk.Frame(root, borderwidth=2, relief="groove", bg="light green")
panel_lista.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
titulo_lista = tk.Label(panel_lista, text="Lista de Eventos Programados", bg="light green")
titulo_lista.pack(side=tk.TOP, fill=tk.X)

# TreeView para mostrar los eventos
treeview = ttk.Treeview(panel_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")
treeview.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Menú
barra_menu = Menu(root)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=barra_menu)

# Ejecutar la aplicación
root.mainloop()
