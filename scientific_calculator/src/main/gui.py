import tkinter as tk
from calculator import BasicOperations, AdvancedOperations

class ScientificCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        self.entry = tk.Entry(root, width=50, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        rows = 1
        cols = 0

        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=rows, column=cols)
            cols += 1
            if cols > 3:
                cols = 0
                rows += 1

    def on_button_click(self, char):
        current = self.entry.get()
        if char == '=':
            try:
                result = str(eval(current))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + char)


def main():
    root = tk.Tk()
    app = ScientificCalculatorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
