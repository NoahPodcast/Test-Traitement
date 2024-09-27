import tkinter as tk
import random
import time

class AttentionConcentrationTest:
    def __init__(self, root, main_menu):
        self.root = root
        self.main_menu = main_menu
        self.stimuli_missed = 0
        self.reaction_times = []
        self.math_problems = []
        self.correct_answers = 0
        self.total_problems = 5
        self.current_problem = 0
        self.start_time = None

        self.setup_ui()

    def setup_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(self.root, text="Cliquez sur les cercles rouges et résolvez les problèmes mathématiques", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg="white")
        self.canvas.pack()

        self.problem_label = tk.Label(self.root, text="", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
        self.problem_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.create_circles()
        self.next_problem()

        self.back_button = tk.Button(self.root, text="Retour au menu principal", command=self.main_menu, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 14), relief="flat", padx=10, pady=5)
        self.back_button.pack(pady=20)
        self.back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def create_circles(self):
        for _ in range(10):
            x = random.randint(50, self.root.winfo_screenwidth() - 50)
            y = random.randint(50, self.root.winfo_screenheight() - 50)
            self.canvas.create_oval(x-25, y-25, x+25, y+25, fill="red", tags="target")

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if "target" in self.canvas.gettags(item):
            self.canvas.delete(item)
            reaction_time = time.time() - self.start_time
            self.reaction_times.append(reaction_time)
            self.start_time = time.time()

    def next_problem(self):
        if self.current_problem < self.total_problems:
            self.current_problem += 1
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            self.math_problems.append((a, b))
            self.problem_label.config(text=f"Résolvez : {a} + {b} = ?")
            self.answer_entry.delete(0, tk.END)
            self.start_time = time.time()
        else:
            self.end_test()

    def check_answer(self, event):
        if self.current_problem <= self.total_problems:
            a, b = self.math_problems[self.current_problem - 1]
            try:
                answer = int(self.answer_entry.get())
                if answer == a + b:
                    self.correct_answers += 1
            except ValueError:
                pass
            self.next_problem()

    def end_test(self):
        self.canvas.unbind("<Button-1>")
        self.answer_entry.unbind("<Return>")
        self.canvas.delete("all")
        self.problem_label.config(text="")

        results_text = (
            f"Test terminé. Voici vos résultats:\n"
            f"Nombre de stimuli ratés: {10 - len(self.reaction_times)}\n"
            f"Temps de réaction moyen: {sum(self.reaction_times)/len(self.reaction_times):.2f} secondes\n"
            f"Taux de succès des problèmes mathématiques: {self.correct_answers}/{self.total_problems}\n"
        )

        results_label = tk.Label(self.root, text=results_text, font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
        results_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.back_button.lift()
        self.back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def test_attention_concentration(root, main_menu):
    AttentionConcentrationTest(root, main_menu)