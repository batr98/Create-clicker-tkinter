import tkinter as tk
class Player:
    def __init__(self):
        self.score = 0
    def add_score(self):
        self.score +=1
class Level:
    def __init__(self):
        self.level=1
    def update(self,score):
        if score >=20:
            self.level=3
        elif score >=10:
            self.level=2
        else:
            self.level=1
        return self.level
def main():
    root = tk.Tk()
    root.title("clicker")
    root.geometry("400x300")
    label_score = tk.Label(root, text="Score: 0")
    label_score.pack(pady=20)
    button_click = tk.Button(root, text="Click", font=("Arial",16),width=15,height=3)
    button_click.pack(pady=20)
    root.mainloop()
if __name__ == "__main__":
    main()

