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

def on_left_click(event):
    status_label.config(text="Clic izquierdo detectado.")

def on_right_click(event):
    status_label.config(text="Clic derecho detectado.")

def on_middle_click(event):
    status_label.config(text="Clic de scroll detectado.")

def on_mouse_move(event):
    position_label.config(text=f"Posición del mouse: x={event.x}, y={event.y}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("500x400")

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

# Vinculación de eventos del mouse con la lista de tareas
task_listbox.bind("<Button-1>", on_left_click)
task_listbox.bind("<Button-2>", on_middle_click)
task_listbox.bind("<Button-3>", on_right_click)

# Atajos de teclado
root.bind('<Return>', on_enter_key)  # Añadir tarea con la tecla "Enter"
root.bind('<c>', mark_task_completed)  # Marcar tarea como completada con la tecla "C"
root.bind('<d>', delete_task)  # Eliminar tarea con la tecla "D"
root.bind('<Escape>', on_escape_key)  # Cerrar la aplicación con la tecla "Escape"

# Label para mostrar el estado de los clics del mouse
status_label = tk.Label(root, text="Interacción con el mouse aquí.")
status_label.pack(pady=10)

# Label para mostrar la posición del mouse
position_label = tk.Label(root, text="Posición del mouse: x=0, y=0")
position_label.pack(pady=10)

# Vinculación de eventos de movimiento del mouse
root.bind("<Motion>", on_mouse_move)

task_entry.focus_set()  # Poner el foco en la entrada de texto

root.mainloop()
