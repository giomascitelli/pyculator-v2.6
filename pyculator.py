import tkinter as tk
import math
import random
from graphsgen import generate_graph # Import graphs generator with matplotlib
from numinfo import * # Import information about numbers that are used throughout this code
from tkinter import ttk
from PIL import Image, ImageTk


# Factorial operation function
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

# Fibonnaci sequence function
def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


# Defining the operations that will happen when the buttons are clicked

# Sum button function
def option1():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} + {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('addition', result, num1, num2, root)
    
# Sub button function    
def option2():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} - {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('subtraction', result, num1, num2, root)
    
# Multiply button function    
def option3():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} * {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('multiplication', result, num1, num2, root)

# Divide button function    
def option4():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} / {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('division', result, num1, num2, root)

# Power button function    
def option5():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1**num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} ^ {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('exponentiation', result, num1, num2, root)
        
# Square root button function
def option6():
    num1 = float(entry1.get())
    result = math.sqrt(num1)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\nsqrt({num1}) = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')    
    
# Percentage button function
def option7():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = (num1 * num2) / 100
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num2}% of {num1} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled') 
    generate_graph('percentage', result, num1, num2, root)

# Modulo button function
def option8():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 % num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\nthe remainder of {num1} / {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('modulus', result, num1, num2, root)
 
# Fibonacci sequence button function
def option9():
    num1 = int(entry1.get())
    result = fibonacci(num1)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\nthe fibonacci sequence with {num1} as the limit = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    
# Factorial number button function    
def option10():
    num1 = int(entry1.get())
    result = factorial(num1)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1}! = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')

     
# RNG button function
def option11():
    result = random.randint(0, 500)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')



# Pyculator's GUI
root = tk.Tk()
root.title("pyculator")
root.geometry("500x535")
root.config(bg="#E6E6E6")
root.resizable(False, False)

frame = tk.Frame(root)
frame.grid(row=8, column=0, padx=20, pady=10, sticky="ew")

# Load image
image = Image.open("logo.png")
image = image.resize((295, 80), Image.Resampling.LANCZOS)  # Resize the image as per your requirement
photo = ImageTk.PhotoImage(image)

# Create a label for the image
image_label = tk.Label(root, image=photo, bg="#E6E6E6")
image_label.image = photo  # keep a reference
image_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create labels
label1 = tk.Label(root, text="", bg="#E6E6E6")
label1.grid(row=0, column=0, columnspan=4, padx=20, pady=(70,10))

# Create functions that handle the placeholder text on the input fields
def on_entry_click(event):
    """Function to handle click event on entry widgets"""
    widget = event.widget
    if widget.get() == 'enter number 1' or widget.get() == 'enter number 2':
        widget.delete(0, "end")
        widget.config(fg='black')

def on_focus_out(event):
    """Function to handle focus out event on entry widgets"""
    widget = event.widget
    if widget.get() == '':
        widget.insert(0, 'enter number 1' if widget == entry1 else 'enter number 2')
        widget.config(fg='gray')

        
# Create input fields
entry1 = tk.Entry(root, fg='gray')
entry1.insert(0, 'enter number 1')
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focus_out)
entry1.grid(row=1, column=0, columnspan=4, padx=20, pady=5)

entry2 = tk.Entry(root, fg='gray')
entry2.insert(0, 'enter number 2')
entry2.bind("<FocusIn>", on_entry_click)
entry2.bind("<FocusOut>", on_focus_out)
entry2.grid(row=2, column=0, columnspan=4, padx=20, pady=5)


# Create buttons
button1 = tk.Button(root, text="add", command=option1, bg="#F2F2F2", width=10)
button1.grid(row=3, column=0, padx=20, pady=10)

button2 = tk.Button(root, text="subtract", command=option2, bg="#F2F2F2", width=10)
button2.grid(row=3, column=1, padx=20, pady=10)

button3 = tk.Button(root, text="multiply", command=option3, bg="#F2F2F2", width=10)
button3.grid(row=3, column=2, padx=20, pady=10)

button4 = tk.Button(root, text="divide", command=option4, bg="#F2F2F2", width=10)
button4.grid(row=3, column=3, padx=20, pady=10)

button5 = tk.Button(root, text="power", command=option5, bg="#F2F2F2", width=10)
button5.grid(row=4, column=0, padx=20, pady=10)

button6 = tk.Button(root, text="square root", command=option6, bg="#F2F2F2", width=10)
button6.grid(row=4, column=1, padx=20, pady=10)

button7 = tk.Button(root, text="percentage", command=option7, bg="#F2F2F2", width=10)
button7.grid(row=4, column=2, padx=20, pady=10)

button8 = tk.Button(root, text="modulo", command=option8, bg="#F2F2F2", width=10)
button8.grid(row=4, column=3, padx=20, pady=10)

button9 = tk.Button(root, text="fibonacci", command=option9, bg="#F2F2F2", width=10)
button9.grid(row=5, column=1, padx=20, pady=10)

button10 = tk.Button(root, text="factorial", command=option10, bg="#F2F2F2", width=10)
button10.grid(row=5, column=2, padx=20, pady=10)

button11 = tk.Button(root, text="random number", command=option11, bg="#F2F2F2", width=15)
button11.grid(row=6, column=0, padx=20, pady=10, sticky="ew", columnspan=4)


# Create the text where the results are output
text = tk.Text(root, height=10, wrap='word',state='disabled', bg='#dedede')
text.grid(row=9, column=0, sticky="nsew", columnspan=4)

vsb = ttk.Scrollbar(root, orient="vertical", command=text.yview)
vsb.grid(row=9, column=4, sticky="ns")

text.configure(width=50, yscrollcommand=vsb.set)

text.tag_configure("center", justify="center")

text.bind_all("<MouseWheel>", lambda event: text.yview_scroll(-1 * int(event.delta/120), "units"))

# GUI main loop function
root.mainloop()

