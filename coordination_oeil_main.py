import tkinter as tk
import random

def test_coordination_oeil_main(root, main_menu):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Cliquez sur les cercles rouges", font=("Helvetica", 18))
    label.pack(pady=20)

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="white")
    canvas.pack()

    def create_circles():
        for _ in range(10):
            x = random.randint(50, root.winfo_screenwidth() - 50)
            y = random.randint(50, root.winfo_screenheight() - 50)
            canvas.create_oval(x-25, y-25, x+25, y+25, fill="red", tags="target")

    def on_click(event):
        item = canvas.find_closest(event.x, event.y)
        if "target" in canvas.gettags(item):
            canvas.delete(item)

    canvas.bind("<Button-1>", on_click)
    create_circles()

    # Bouton pour revenir au menu principal
    back_button = tk.Button(root, text="Retour au menu principal", command=main_menu)
    back_button.pack(pady=20)