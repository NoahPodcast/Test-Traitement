import tkinter as tk
import time

class CoordinationMotriceTest:
    def __init__(self, root, main_menu):
        self.root = root
        self.main_menu = main_menu
        self.start_time = None
        self.errors = 0
        self.line_coords = []
        self.setup_ui()

    def setup_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#f0f0f0")

        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg="white")
        self.canvas.pack()

        # Dessiner une ligne sinusoïdale comme trajectoire
        for x in range(0, self.root.winfo_screenwidth(), 10):
            y = self.root.winfo_screenheight() // 2 + 100 * (x % 200 - 100) / 100
            self.line_coords.append((x, y))
        for i in range(len(self.line_coords) - 1):
            self.canvas.create_line(self.line_coords[i][0], self.line_coords[i][1], self.line_coords[i+1][0], self.line_coords[i+1][1], fill="blue", width=3)

        # Créer la balle
        self.ball = self.canvas.create_oval(0, 0, 20, 20, fill="green")

        # Suivre le mouvement du curseur
        self.canvas.bind("<Motion>", self.on_mouse_move)

        # Bouton pour revenir au menu principal
        self.back_button = tk.Button(self.root, text="Retour au menu principal", command=self.main_menu, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 14), relief="flat", padx=10, pady=5)
        self.back_button.pack(pady=20)
        self.back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        # Démarrer le chronomètre
        self.start_time = time.time()

    def on_mouse_move(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.ball, x-10, y-10, x+10, y+10)

        # Vérifier les contacts avec les bords
        for (lx, ly) in self.line_coords:
            if abs(x - lx) < 10 and abs(y - ly) < 10:
                self.errors += 1
                self.canvas.itemconfig(self.ball, fill="red")
                return
        self.canvas.itemconfig(self.ball, fill="green")

        # Vérifier si l'utilisateur a atteint la fin du parcours
        if x >= self.root.winfo_screenwidth() - 10:
            self.end_test()

    def end_test(self):
        self.canvas.unbind("<Motion>")
        end_time = time.time()
        total_time = end_time - self.start_time

        # Afficher les résultats
        self.canvas.delete("all")
        results_text = (
            f"Test terminé. Voici vos résultats:\n"
            f"Temps total: {total_time:.2f} secondes\n"
            f"Nombre d'erreurs: {self.errors}\n"
        )
        results_label = tk.Label(self.root, text=results_text, font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
        results_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.back_button.lift()
        self.back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def test_coordination_motrice(root, main_menu):
    CoordinationMotriceTest(root, main_menu)