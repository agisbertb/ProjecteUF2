import tkinter as tk
import random

root = tk.Tk()
root.title("Juego del ahorcado")

word_list = ["hola", "adios", "python", "programacion", "juego"]
word = random.choice(word_list)

guesses_left = 6
guessed_letters = set()

def update_word_display():
    # Crea una cadena de guiones con la misma longitud que la palabra elegida
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    word_label.config(text=displayed_word)

def check_guess():
    global guesses_left
    letter = guess.get()[0]
    guess.set("")  # Borra el widget de entrada después de que se ingresa una letra
    if letter in guessed_letters:
        return
    guessed_letters.add(letter)
    if letter in word:
        update_word_display()
        if "-" not in word_label.cget("text"):
            result_label.config(text="¡Ganaste!")
    else:
        guesses_left -= 1
        if guesses_left == 0:
            result_label.config(text="¡Perdiste!")
        else:
            guesses_left_label.config(text=f"Intentos restantes: {guesses_left}")
            guessed_letters_label.config(text=f"Letras adivinadas: {', '.join(sorted(guessed_letters))}")

guess = tk.StringVar()
entry = tk.Entry(root, textvariable=guess)
entry.pack()

guess_button = tk.Button(root, text="Adivinar", command=check_guess)
guess_button.pack()

word_label = tk.Label(root, text="")
word_label.pack()

guesses_left_label = tk.Label(root, text=f"Intentos restantes: {guesses_left}")
guesses_left_label.pack()

guessed_letters_label = tk.Label(root, text=f"Letras adivinadas: {', '.join(sorted(guessed_letters))}")
guessed_letters_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

update_word_display()

root.mainloop()
