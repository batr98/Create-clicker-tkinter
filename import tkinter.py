import tkinter as tk

class Player:
    def __init__(self, name="Игрок"):
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1

    def reset(self):
        self.score = 0

class Level:
    def __init__(self):
        self.level = 1

    def update(self, score):
        if score >= 30:
            self.level = 4
        if score >= 20:
            self.level = 3
        elif score >= 10:
            self.level = 2
        else:
            self.level = 1
        return self.level

class Game:
    def __init__(self, root):
        self.root = root
        self.player = Player("Игрок 1")
        self.level = Level()

        self.root.title("Кликер с уровнями")
        self.root.geometry("400x400")

        self.label_name = tk.Label(root, text=f"Игрок: {self.player.name}", font=("Arial", 14))
        self.label_name.pack(pady=10)

        self.label_score = tk.Label(root, text=f"Очки: {self.player.score}", font=("Arial", 14))
        self.label_score.pack(pady=10)

        self.label_level = tk.Label(root, text=f"Уровень: {self.level.level}", font=("Arial", 14))
        self.label_level.pack(pady=10)

        self.button_click = tk.Button(root, text="Кликни меня!", font=("Arial", 16),
                                      width=15, height=2, command=self.click)
        self.button_click.pack(pady=20)

        self.button_reset = tk.Button(root, text="Сброс", font=("Arial", 12),
                                      width=10, command=self.reset_game)
        self.button_reset.pack(pady=5)

        self.level_message = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.level_message.pack(pady=10)

    def click(self):
        self.player.add_score()
        self.update_ui()

    def reset_game(self):
        self.player.reset()
        self.level = Level()
        self.update_ui()

    def update_ui(self):
        current_level = self.level.update(self.player.score)

        self.label_score.config(text=f"Очки: {self.player.score}")
        self.label_level.config(text=f"Уровень: {current_level}")

        if current_level == 1:
            self.level_message.config(text="Ты только начинаешь!")
            self.root.configure(bg="lightyellow")
        elif current_level == 2:
            self.level_message.config(text="Отлично! Ты поднялся на 2 уровень! ")
            self.root.configure(bg="lightgreen")
        elif current_level == 3:
            self.level_message.config(text="Вау! Максимальный уровень! ")
            self.root.configure(bg="lightblue")
        elif current_level == 4:
            self.level_message.config(text="Ты превзошел все ожидания! ")
            self.root.configure(bg="gold")


def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()


