import tkinter as tk

def test_motricite_fine(root, main_menu):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="white")
    canvas.pack()

    # Dessiner une forme à tracer
    canvas.create_rectangle(100, 100, 300, 300, outline="blue", width=3)

    # Suivre le mouvement du curseur
    def on_mouse_move(event):
        x, y = event.x, event.y
        if 100 < x < 300 and 100 < y < 300:
            canvas.create_oval(x-2, y-2, x+2, y+2, fill="green")
        else:
            canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")

    canvas.bind("<Motion>", on_mouse_move)

    # Bouton pour revenir au menu principal
    back_button = tk.Button(root, text="Retour au menu principal", command=main_menu)
    back_button.pack(pady=20)