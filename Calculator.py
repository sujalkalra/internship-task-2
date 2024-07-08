import tkinter as tk
from tkinter import font as tkfont

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Beautiful Calculator")
        self.geometry("400x600")
        self.resizable()

        self.custom_font = tkfont.Font(family="Helvetica", size=36, weight="bold")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self, bg="#333")
        display_frame.pack(expand=True, fill="both")

        display = tk.Entry(display_frame, textvariable=self.result_var, font=self.custom_font, bg="#222", fg="white", bd=10, relief="sunken", justify='right')
        display.pack(expand=True, fill="both")

        # Buttons
        buttons_frame = tk.Frame(self, bg="#444")
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'CE',
            '1', '2', '3', '-', '😊',
            '0', '.', '=', '+', '😊'
        ]

        button_colors = {
            '/': "#f1c40f", '*': "#f1c40f", '-': "#e74c3c", '+': "#2ecc71",
            '=': "#3498db", 'C': "#e67e22", 'CE': "#e67e22"
        }

        row_val = 0
        col_val = 0

        for button in buttons:
            if button:
                button_command = lambda x=button: self.on_button_click(x)
                button_color = button_colors.get(button, "#bdc3c7")
                button_bg = button_color
                button_fg = "black" if button not in button_colors else "white"

                tk.Button(buttons_frame, text=button, font=self.custom_font, bg=button_bg, fg=button_fg, bd=5, relief="raised", command=button_command, highlightbackground="#888").grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        for i in range(5):
            buttons_frame.grid_columnconfigure(i, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char in '0123456789':
            new_text = current_text + char
        elif char in '+-*/':
            if current_text and current_text[-1] not in '+-*/':
                new_text = current_text + char
            else:
                new_text = current_text[:-1] + char
        elif char == '.':
            if '.' not in current_text.split()[-1]:
                new_text = current_text + char
        elif char == '=':
            try:
                new_text = str(eval(current_text))
            except:
                new_text = "Error"
        elif char == 'C':
            new_text = ''
        elif char == 'CE':
            new_text = current_text[:-1]

        self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
