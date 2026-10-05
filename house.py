import tkinter as tk

root = tk.Tk()

root.title("Simple House")

canvas = tk.Canvas(root, width=500, height=350, bg="skyblue")
canvas.pack()

# House body - rectangle
canvas.create_rectangle(150, 150, 350, 300, fill="lightyellow")

# Roof - triangle
canvas.create_polygon(
    120, 150,
    250, 60,
    380, 150,
    fill="red"
)

# Door
canvas.create_rectangle(220, 220, 280, 300, fill="brown")

# Left window
canvas.create_rectangle(170, 180, 210, 220, fill="lightblue")

# Right window
canvas.create_rectangle(290, 180, 330, 220, fill="lightblue")

# Ground
canvas.create_rectangle(0, 300, 500, 350, fill="green")

root.mainloop()