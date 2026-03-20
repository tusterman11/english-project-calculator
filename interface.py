
import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator - TKINTER")
        self.master.geometry("430x500")
        self.master.configure(bg="#E4E4E4")
        self.create_widgets()
        for i in range(6):
            self.master.rowconfigure(i, weight=1)

        for i in range(4):
            self.master.columnconfigure(i, weight=1)

        
        self.expression = ""


        


    def create_buttons(self):
        buttons = [
            ('%', 1, 0), ('x²', 1, 1), ('AC', 1, 2), ('C', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('.', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3)
        ]
   
        for text, row, col in buttons:
            button_config = {
                'text': text,
                'font': ("Consolas", 18),
                'height': 2,
                'width': 5,
                'bg': "#FFFFFF",
                'relief': tk.RAISED,
                'command': lambda t=text: self.on_button_click(t)
            }

            if text in ('AC', 'C'):
                button_config['bg'] = "#B80C0C"
                button_config['fg'] = "#FFFFFF"
                
            if text in ('='):
                button_config['bg'] = "#2860FC"
                button_config['fg'] ="#FFFFFF"  

            button = tk.Button(self.master, **button_config)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def create_widgets(self):  
        self.display_var = tk.StringVar()

        self.display = tk.Entry(
            self.master,
            textvariable=self.display_var,
            font=("Arial", 24),
            bd=8,
            bg="#E4E4E4",
            relief=tk.SUNKEN,
            state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def on_button_click(self, text):
        if text == 'AC':
            self.expression = ""
            self.display_var.set(self.expression)
        elif text == 'C':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression)
        elif text == '=':
            try:
                from logic import evaluate_expression
                result = evaluate_expression(self.expression)
                self.display_var.set(str(result))
                self.expression = str(result)
            except Exception as e:
                self.display_var.set("Error")
                self.expression = ""
        else:
            self.expression += text
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()        