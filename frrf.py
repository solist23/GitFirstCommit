import tkinter as tk

def change_background():
    canvas.config(bg="gray")

root = tk.Tk()
root.title("Фигуры на Python")

root.geometry("400x300")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

circle = canvas.create_oval(50, 50, 150, 150, fill="red")

rectangle = canvas.create_rectangle(200, 50, 350, 150, fill="blue")

button = tk.Button(root, text="Изменить фон", command=change_background)
button.pack(pady=10)

root.mainloop()