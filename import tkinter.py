import tkinter as tk
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