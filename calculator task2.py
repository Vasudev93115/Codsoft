import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        result_display = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20))
        result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in button_texts:
            button = tk.Button(self.root, text=text, font=("Helvetica", 20), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
