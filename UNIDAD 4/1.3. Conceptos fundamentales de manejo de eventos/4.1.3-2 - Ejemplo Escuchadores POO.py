import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Lista de Tareas')
        self.master.geometry('400x300')

        # Etiqueta y campo de entrada para la tarea
        self.task_label = tk.Label(master, text='Nueva Tarea:')
        self.task_label.pack(pady=5)
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=5)

        # Botones para añadir, completar y eliminar tareas
        self.add_button = tk.Button(master, text='Añadir Tarea', command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(master, text='Marcar como Completada', command=self.mark_as_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(master, text='Eliminar Tarea', command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(master, width=40, height=10)
        self.task_listbox.pack(pady=10)

        # Evento para añadir tareas con la tecla Enter
        self.task_entry.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese una tarea.")

    def mark_as_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"{task} ✔")
        except IndexError:
            messagebox.showwarning("Selección no válida", "Por favor seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selección no válida", "Por favor seleccione una tarea para eliminar.")

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
