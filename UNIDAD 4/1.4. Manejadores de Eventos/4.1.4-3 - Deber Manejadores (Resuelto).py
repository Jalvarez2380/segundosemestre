import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x350")

        # Campo de entrada para agregar nuevas tareas
        self.task_entry = tk.Entry(root, width=35, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Lista para mostrar las tareas
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, expand=True, fill=tk.BOTH)

        # Botón para marcar como completada
        self.mark_task_button = tk.Button(root, text="Marcar como Completada", command=self.mark_task)
        self.mark_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Atajos de teclado
        root.bind('<Return>', self.add_task)  # Tecla 'Enter' para añadir tarea
        root.bind('<c>', lambda e: self.mark_task())  # Tecla 'C' para marcar como completada
        root.bind('<d>', lambda e: self.delete_task())  # Tecla 'D' para eliminar tarea
        root.bind('<Escape>', lambda e: root.quit())  # Tecla 'Escape' para cerrar la aplicación

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def mark_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)
            self.tasks_listbox.delete(index)
            self.tasks_listbox.insert(index, f"[COMPLETADA] {task}")
        except IndexError:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para marcar.")

    def delete_task(self, event=None):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
