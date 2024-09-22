import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingrese una tarea.")

def mark_as_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"{task} ✔")
    except IndexError:
        messagebox.showwarning("Selección no válida", "Por favor seleccione una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selección no válida", "Por favor seleccione una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("300x300")

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=25)
task_entry.pack(pady=10)

# Botones para añadir, completar y eliminar tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", command=mark_as_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=25, height=10)
task_listbox.pack(pady=10)

# Permitir añadir tareas con la tecla Enter
task_entry.bind("<Return>", lambda event: add_task())

# Iniciar el bucle principal de la GUI
root.mainloop()
