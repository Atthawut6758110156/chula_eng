import tkinter as tk
import random

# List of flashcards: each card has the Thai letter and its pronunciation/name.
flashcards = [
    {"letter": "ก", "name": "gor kai"},
    {"letter": "ข", "name": "kho khai"},
    {"letter": "ค", "name": "kho khon"},
    {"letter": "จ", "name": "jor jaan"},
    # Add more flashcards as needed.
]

class FlashCardGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Thai Consonant Flashcards")

        # Canvas to display the card.
        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack(pady=20)

        # Display text on the card.
        self.card_text = self.canvas.create_text(200, 150, text="", font=("Arial", 50))

        # Frame for buttons.
        button_frame = tk.Frame(master)
        button_frame.pack()

        # Button to flip the card.
        self.flip_button = tk.Button(button_frame, text="Flip", command=self.flip_card, width=10)
        self.flip_button.grid(row=0, column=0, padx=10)

        # Button to go to the next card.
        self.next_button = tk.Button(button_frame, text="Next Card", command=self.next_card, width=10)
        self.next_button.grid(row=0, column=1, padx=10)

        # Initialize game state.
        self.current_card = {}
        self.is_flipped = False
        self.next_card()

    def next_card(self):
        # Randomly select a flashcard and reset the card state.
        self.current_card = random.choice(flashcards)
        self.is_flipped = False
        self.canvas.itemconfig(self.card_text, text=self.current_card["letter"])

    def flip_card(self):
        # If the card isn't flipped yet, flip it to show the name.
        if not self.is_flipped:
            self.canvas.itemconfig(self.card_text, text=self.current_card["name"])
            self.is_flipped = True

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashCardGame(root)
    root.mainloop()
                                                                                                                                                                                                                                                   