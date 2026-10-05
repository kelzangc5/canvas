import tkinter as tk

root = tk.Tk()
root.title("Oggy House")

canvas = tk.Canvas(root, width=800, height=500, bg="skyblue")
canvas.pack()


# -------------------------
# BACKGROUND
# -------------------------

# Sun
canvas.create_oval(650, 40, 720, 110, fill="yellow", outline="orange")

# Ground
canvas.create_rectangle(0, 380, 800, 500, fill="green", outline="green")


# -------------------------
# HOUSE
# -------------------------

# House body
canvas.create_rectangle(
    250, 180, 600, 380,
    fill="lightyellow",
    outline="black"
)

# Roof
canvas.create_polygon(
    210, 180,
    425, 60,
    640, 180,
    fill="red",
    outline="black"
)

# Door
canvas.create_rectangle(
    390, 270, 460, 380,
    fill="brown",
    outline="black"
)

# Door knob
canvas.create_oval(
    445, 325, 453, 333,
    fill="yellow"
)

# Left window
canvas.create_rectangle(
    285, 220, 360, 285,
    fill="lightblue",
    outline="black"
)

# Window cross
canvas.create_line(322, 220, 322, 285, width=3)
canvas.create_line(285, 252, 360, 252, width=3)

# Right window
canvas.create_rectangle(
    490, 220, 565, 285,
    fill="lightblue",
    outline="black"
)

# Window cross
canvas.create_line(527, 220, 527, 285, width=3)
canvas.create_line(490, 252, 565, 252, width=3)


# -------------------------
# DOGHOUSE
# -------------------------

# Doghouse body
canvas.create_rectangle(
    80, 310, 190, 380,
    fill="orange",
    outline="black"
)

# Doghouse roof
canvas.create_polygon(
    65, 310,
    135, 255,
    205, 310,
    fill="brown",
    outline="black"
)

# Doghouse entrance
canvas.create_oval(
    110, 330, 160, 380,
    fill="black"
)


# -------------------------
# OGGY
# -------------------------

# Starting position
oggy_x = 40


def draw_oggy(x):
    # Body
    canvas.create_oval(
        x, 315,
        x + 55, 390,
        fill="blue",
        outline="black",
        tags="oggy"
    )

    # Head
    canvas.create_oval(
        x + 5, 265,
        x + 60, 325,
        fill="blue",
        outline="black",
        tags="oggy"
    )

    # Ears
    canvas.create_oval(
        x, 275,
        x + 15, 295,
        fill="blue",
        outline="black",
        tags="oggy"
    )

    canvas.create_oval(
        x + 50, 275,
        x + 65, 295,
        fill="blue",
        outline="black",
        tags="oggy"
    )

    # Eyes
    canvas.create_oval(
        x + 15, 280,
        x + 27, 295,
        fill="white",
        outline="black",
        tags="oggy"
    )

    canvas.create_oval(
        x + 38, 280,
        x + 50, 295,
        fill="white",
        outline="black",
        tags="oggy"
    )

    # Pupils
    canvas.create_oval(
        x + 19, 284,
        x + 24, 290,
        fill="black",
        tags="oggy"
    )

    canvas.create_oval(
        x + 42, 284,
        x + 47, 290,
        fill="black",
        tags="oggy"
    )

    # Nose
    canvas.create_oval(
        x + 28, 297,
        x + 38, 305,
        fill="black",
        tags="oggy"
    )

    # Smile
    canvas.create_arc(
        x + 20, 295,
        x + 48, 315,
        start=200,
        extent=140,
        style="arc",
        width=2,
        tags="oggy"
    )

    # Legs
    canvas.create_line(
        x + 15, 375,
        x + 10, 405,
        width=6,
        tags="oggy"
    )

    canvas.create_line(
        x + 40, 375,
        x + 45, 405,
        width=6,
        tags="oggy"
    )

    # Arms
    canvas.create_line(
        x + 5, 335,
        x - 15, 355,
        width=6,
        tags="oggy"
    )

    canvas.create_line(
        x + 50, 335,
        x + 70, 355,
        width=6,
        tags="oggy"
    )


# Draw Oggy
draw_oggy(oggy_x)


# -------------------------
# OGGY MOVING ANIMATION
# -------------------------

def move_oggy():
    global oggy_x

    # Delete the old Oggy
    canvas.delete("oggy")

    # Move Oggy to the right
    oggy_x += 5

    # If Oggy reaches the edge,
    # start again from the left
    if oggy_x > 800:
        oggy_x = -70

    # Draw Oggy at the new position
    draw_oggy(oggy_x)

    # Repeat every 50 milliseconds
    root.after(50, move_oggy)


# Start animation
move_oggy()


root.mainloop()