import tkinter as tk
import random
import time

def test_memoire(root, main_menu):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Mémorisez les chiffres", font=("Helvetica", 18))
    label.pack(pady=20)

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="white")
    canvas.pack()

    numbers = [random.randint(0, 9) for _ in range(5)]
    number_labels = []

    for i, number in enumerate(numbers):
        number_label = tk.Label(canvas, text=str(number), font=("Helvetica", 48))
        number_label.place(x=100 + i * 100, y=root.winfo_screenheight() // 2)
        number_labels.append(number_label)

    def hide_numbers():
        for label in number_labels:
            label.destroy()
        entry = tk.Entry(root, font=("Helvetica", 24))
        entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        submit_button = tk.Button(root, text="Soumettre", command=lambda: check_memory(entry.get()))
        submit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        global start_time
        start_time = time.time()

    def check_memory(user_input):
        end_time = time.time()
        recall_time = end_time - start_time
        correct_count = sum(1 for a, b in zip(user_input, numbers) if a == str(b))
        errors = len(numbers) - correct_count

        if user_input == ''.join(map(str, numbers)):
            result_text = "Correct!"
            result_color = "green"
        else:
            result_text = "Incorrect!"
            result_color = "red"

        result_label = tk.Label(root, text=result_text, font=("Helvetica", 24), fg=result_color)
        result_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        stats_text = (
            f"Nombre d'éléments correctement retenus: {correct_count}/{len(numbers)}\n"
            f"Temps de rappel: {recall_time:.2f} secondes\n"
            f"Erreurs: {errors}\n"
        )
        stats_label = tk.Label(root, text=stats_text, font=("Helvetica", 18))
        stats_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.after(3000, hide_numbers)

    # Bouton pour revenir au menu principal
    back_button = tk.Button(root, text="Retour au menu principal", command=main_menu, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 14), relief="flat", padx=10, pady=5)
    back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)