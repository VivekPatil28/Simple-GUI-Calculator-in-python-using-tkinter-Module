import string as ch
from tkinter import *
from tkinter import messagebox

operators = '+-/*.1234567890()%'


def calculate(event):
    for i in win.get():
        if i not in operators:
            messagebox.showwarning(
                "Error", f"Cannot use '{i}' in Calculator", parent=window)
            break

    prev = ''
    try:

        prev = eval(str(prev)+win.get())
    except ZeroDivisionError as e:
        messagebox.showwarning("Error", "Cannot Divide by Zero", parent=window)
        prev = "Undefined"
    except SyntaxError as e:
        messagebox.showwarning("Error", "Invalid Operation", parent=window)
        prev = "Undefined"

    if prev != "Undefined":
        num = ''
        s = str(prev)
        if '.' in s:
            stri = s[s.find('.')-1::-1]

        else:
            stri = str(prev)[::-1]

        for i in range(len(stri)):
            if i >= 3:
                if i % 2 != 0:
                    num += ','
            num += stri[i]

        if '.' in str(prev):
            num = num[::-1]+s[s.find('.'):]
        else:
            num = num[::-1]

        op.delete(0, "end")
        op.insert(0, num)
    else:
        op.delete(0, "end")
        op.insert(0, prev)


window = Tk()
window.state('zoomed')
window.title("Calculator")
head = Label(window, text="Calculator", fg="White", bg="Green",
             padx=800, pady=25, font=("Arial", 30, "bold"))
head.pack()

label = Label(window, text="", font=("Arial", 150)).pack()

win = Entry(window, font=("Arial", 25), width=50, justify=RIGHT)
win.pack()


label = Label(window, text="", font=("Arial", 20)).pack()
op = Entry(window, font=("Arial", 25), justify=RIGHT)
op.pack()

window.bind('<Return>', calculate)

window.mainloop()
