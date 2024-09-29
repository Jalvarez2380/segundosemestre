import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def mark_task_completed(event=None):
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(index, f"[COMPLETADA] {task}")
    except IndexError:
        pass

def delete_task(event=None):
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        pass

def on_enter_key(event):
    add_task()

def on_escape_key(event):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x300")

# Campo de entrada para agregar nuevas tareas
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

# Botón para añadir tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

# Lista para mostrar las tareas
task_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
task_listbox.pack(pady=10, expand=True, fill=tk.BOTH)

# Botón para marcar tareas como completadas
complete_button = tk.Button(root, text="Marcar Como Completada", command=mark_task_completed)
complete_button.pack(pady=5)

# Botón para eliminar tareas
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Atajos de teclado
root.bind('<Return>', on_enter_key)  # Añadir tarea con la tecla "Enter"
root.bind('<c>', mark_task_completed)  # Marcar tarea como completada con la tecla "C"
root.bind('<d>', delete_task)  # Eliminar tarea con la tecla "D"
root.bind('<Escape>', on_escape_key)  # Cerrar la aplicación con la tecla "Escape"

task_entry.focus_set()  # Poner el foco en la entrada de texto

root.mainloop()
