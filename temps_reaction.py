import tkinter as tk
import time
import random
import statistics

class ReactionTest:
    def __init__(self, root, main_menu):
        self.root = root
        self.main_menu = main_menu
        self.reaction_times = []
        self.trials = 5
        self.current_trial = 0
        self.start_time = None

        self.setup_ui()

    def setup_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(self.root, text="Appuyez sur la barre d'espace dès que vous voyez un carré apparaître à l'écran.", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg="white", highlightthickness=0)
        self.canvas.pack()

        self.root.bind("<space>", self.start_test)

        self.back_button = tk.Button(self.root, text="Retour au menu principal", command=self.main_menu, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 14), relief="flat", padx=10, pady=5)
        self.back_button.pack(pady=20)
        self.back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def start_test(self, event):
        self.root.unbind("<space>")
        self.label.config(text="Préparez-vous...")
        self.root.after(random.randint(1000, 3000), self.show_stimulus)

    def show_stimulus(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.root.winfo_screenwidth()//2 - 50, self.root.winfo_screenheight()//2 - 50, self.root.winfo_screenwidth()//2 + 50, self.root.winfo_screenheight()//2 + 50, fill="red")
        self.start_time = time.time()
        self.root.bind("<space>", self.record_reaction)

    def record_reaction(self, event):
        reaction_time = time.time() - self.start_time
        self.reaction_times.append(reaction_time)
        self.current_trial += 1
        self.label.config(text=f"Temps de réaction: {reaction_time:.3f} secondes")
        self.root.unbind("<space>")

        if self.current_trial < self.trials:
            self.canvas.delete("all")  # Effacer le stimulus avant le nouvel essai
            self.root.after(1000, self.start_test, None)
        else:
            self.show_results()

    def show_results(self):
        self.canvas.delete("all")
        self.label.config(text="Test terminé. Voici vos résultats:")

        mean_reaction_time = statistics.mean(self.reaction_times)
        stdev_reaction_time = statistics.stdev(self.reaction_times)

        results_text = (
            f"Temps de réaction moyen: {mean_reaction_time:.3f} secondes\n"
            f"Écart-type: {stdev_reaction_time:.3f} secondes\n"
            f"Temps de réaction minimum: {min(self.reaction_times):.3f} secondes\n"
            f"Temps de réaction maximum: {max(self.reaction_times):.3f} secondes\n"
        )

        results_label = tk.Label(self.root, text=results_text, font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
        results_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.back_button.lift()  # Assurez-vous que le bouton est visible
        self.back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def test_temps_reaction(root, main_menu):
    ReactionTest(root, main_menu)