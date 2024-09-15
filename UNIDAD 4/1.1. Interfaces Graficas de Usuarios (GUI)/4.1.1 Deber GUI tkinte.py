import tkinter as tk
from tkinter import simpledialog, messagebox


class SimpleGUIApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Data Entry App")
        master.geometry("350x200")

        # Adding a simple Menu
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Adding File submenu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Add Entry", command=self.add_entry)
        self.file_menu.add_command(label="Clear Entries", command=self.clear_entries)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        # GUI components
        self.label = tk.Label(master, text="Enter Data:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Add", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_entries)
        self.clear_button.pack(pady=5)

        self.data_display = tk.Listbox(master)
        self.data_display.pack(fill=tk.BOTH, expand=True, pady=10)

    def add_entry(self):
        data = self.entry.get()
        if data:
            self.data_display.insert(tk.END, data)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Info", "Please enter some data before adding.")

    def clear_entries(self):
        self.data_display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUIApp(root)
    root.mainloop()
