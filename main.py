import tkinter as tk
import math

def on_button_click(value):
    if value == "=":
        try:
            expression = textbox.get("1.0", tk.END).strip()
            result = eval(expression)
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, str(result))
            
        except Exception as e:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Error")
    elif value == "√":
        try:
            expression = textbox.get("1.0", tk.END).strip()
            result = math.sqrt(float(expression))
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, str(result))
            
        except Exception as e:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Error")
    elif value == "Clear":
        textbox.delete("1.0", tk.END)
    else:
        textbox.insert(tk.END, value)

root = tk.Tk()
root.title("Калькулятор")

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)
buttonFrame.pack(fill="both", expand=True)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn_sqrt = tk.Button(buttonFrame, text="√", font=("Arial", 18), command=lambda: on_button_click("√"))
btn_sqrt.grid(row=0, column=0, sticky="we")

btn_open_bracket = tk.Button(buttonFrame, text="(", font=("Arial", 18), command=lambda: on_button_click("("))
btn_open_bracket.grid(row=0, column=1, sticky="we")

btn_close_bracket = tk.Button(buttonFrame, text=")", font=("Arial", 18), command=lambda: on_button_click(")"))
btn_close_bracket.grid(row=0, column=2, sticky="we")

btn_dot = tk.Button(buttonFrame, text=".", font=("Arial", 18), command=lambda: on_button_click("."))
btn_dot.grid(row=0, column=3, sticky="we")

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18), command=lambda: on_button_click("1"))
btn1.grid(row=1, column=0, sticky="we")

btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 18), command=lambda: on_button_click("2"))
btn2.grid(row=1, column=1, sticky="we")

btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 18), command=lambda: on_button_click("3"))
btn3.grid(row=1, column=2, sticky="we")

btn_minus = tk.Button(buttonFrame, text="-", font=("Arial", 18), command=lambda: on_button_click("-"))
btn_minus.grid(row=1, column=3, sticky="we")

btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 18), command=lambda: on_button_click("4"))
btn4.grid(row=2, column=0, sticky="we")

btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 18), command=lambda: on_button_click("5"))
btn5.grid(row=2, column=1, sticky="we")

btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 18), command=lambda: on_button_click("6"))
btn6.grid(row=2, column=2, sticky="we")

btn_plus = tk.Button(buttonFrame, text="+", font=("Arial", 18), command=lambda: on_button_click("+"))
btn_plus.grid(row=2, column=3, sticky="we")

btn7 = tk.Button(buttonFrame, text="7", font=("Arial", 18), command=lambda: on_button_click("7"))
btn7.grid(row=3, column=0, sticky="we")

btn8 = tk.Button(buttonFrame, text="8", font=("Arial", 18), command=lambda: on_button_click("8"))
btn8.grid(row=3, column=1, sticky="we")

btn9 = tk.Button(buttonFrame, text="9", font=("Arial", 18), command=lambda: on_button_click("9"))
btn9.grid(row=3, column=2, sticky="we")

btn_multiply = tk.Button(buttonFrame, text="*", font=("Arial", 18), command=lambda: on_button_click("*"))
btn_multiply.grid(row=3, column=3, sticky="we")

btn_clear = tk.Button(buttonFrame, text="Clear", font=("Arial", 18), command=lambda: on_button_click("Clear"))
btn_clear.grid(row=4, column=0, sticky="we")

btn0 = tk.Button(buttonFrame, text="0", font=("Arial", 18), command=lambda: on_button_click("0"))
btn0.grid(row=4, column=1, sticky="we")


btn_equals = tk.Button(buttonFrame, text="=", font=("Arial", 18), command=lambda: on_button_click("="))
btn_equals.grid(row=4, column=2, sticky="we")

btn_divide = tk.Button(buttonFrame, text="/", font=("Arial", 18), command=lambda: on_button_click("/"))
btn_divide.grid(row=4, column=3, sticky="we")

root.mainloop()
