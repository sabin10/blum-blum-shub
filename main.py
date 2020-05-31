from tkinter import *
import sympy
import random
"""
ALGORITHM
"""
x = 3*10**10
y = 4*10**10
seed = random.randint(1, 1e10)

def next_prime(num):
    next_prime_num = sympy.nextprime(num)
    while next_prime_num % 4 != 3:
        next_prime_num = sympy.nextprime(next_prime_num)
    return next_prime_num


p = next_prime(x)
q = next_prime(y)
M = p * q

def start_blum_blum_shub(MB):
    global x
    bytes = MB * 1024
    output = ""
    for _ in range(bytes):
        x = x * x % M
        last_significant_bit = x % 2  # 1 if odd, 0 if even
        output += str(last_significant_bit)
    # write to file
    file = open('output', 'w')
    file.write(output)
    file.close()


"""
INTERFACE
"""

root = Tk()
root.title('Blum blum shub')

description_label = Label(root, text='Pseudo-random number generator using Blum Blum Shub').pack()
entry_label = Label(root, text='Enter number of MB').pack()
input_string = StringVar(root)
text_entry = Entry(root, textvariable=input_string).pack()

def get_input_number():
    return input_string.get()

def generate():
    mb_int = int(get_input_number())
    start_blum_blum_shub(mb_int)


generate_btn = Button(root, text='Generate', command=generate).pack()

root.mainloop()
