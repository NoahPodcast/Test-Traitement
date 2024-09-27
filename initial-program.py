import tkinter as tk
import importlib

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Tests de Capacités Cognitives et Motrices")

# Obtenir les dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Ajuster la taille de la fenêtre principale
root.geometry(f"{screen_width}x{screen_height}")

# Couleurs par défaut
bg_color = "#f0f0f0"
btn_color = "#4CAF50"
btn_text_color = "#ffffff"
text_color = "#333333"

# Fonction pour basculer entre le mode clair et le mode sombre
def toggle_dark_mode():
    global bg_color, btn_color, btn_text_color, text_color
    if bg_color == "#f0f0f0":
        bg_color = "#333333"
        btn_color = "#555555"
        btn_text_color = "#ffffff"
        text_color = "#f0f0f0"
    else:
        bg_color = "#f0f0f0"
        btn_color = "#4CAF50"
        btn_text_color = "#ffffff"
        text_color = "#333333"
    update_ui()

# Fonction pour mettre à jour l'interface utilisateur
def update_ui():
    root.configure(bg=bg_color)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(bg=bg_color, fg=text_color)
        elif isinstance(widget, tk.Button):
            widget.configure(bg=btn_color, fg=btn_text_color)

# Fonction pour charger et exécuter un module de test
def run_test(module_name, function_name):
    module = importlib.import_module(module_name)
    test_function = getattr(module, function_name)
    test_function(root, main_menu)

# Menu principal
def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=bg_color)

    title = tk.Label(root, text="Tests de Capacités Cognitives et Motrices", font=("Helvetica", 24, "bold"), bg=bg_color, fg=text_color)
    title.pack(pady=20)

    options = [
        ("Test de coordination motrice", lambda: run_test('coordination_motrice', 'test_coordination_motrice')),
        ("Test de temps de réaction", lambda: run_test('temps_reaction', 'test_temps_reaction')),
        ("Test d'attention et de concentration", lambda: run_test('attention_concentration', 'test_attention_concentration')),
        ("Test de mémoire", lambda: run_test('memoire', 'test_memoire')),
        ("Test de coordination œil-main", lambda: run_test('coordination_oeil_main', 'test_coordination_oeil_main')),
        ("Test de motricité fine", lambda: run_test('motricite_fine', 'test_motricite_fine')),
        ("Activer le mode sombre", toggle_dark_mode),
        ("Quitter", root.quit)
    ]

    for text, command in options:
        button = tk.Button(root, text=text, font=("Helvetica", 18), command=command, bg=btn_color, fg=btn_text_color, relief="flat", padx=10, pady=5)
        button.pack(pady=10)

if __name__ == "__main__":
    main_menu()
    root.mainloop()