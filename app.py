from tkinter import *

root = Tk()
root.title('Calculator')
root['bg'] = 'gray10'


def app():
    input_field = Entry(root, width=45, borderwidth=2)
    input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def on_click(digit):
        current_input = input_field.get()
        input_field.delete(0, END)
        input_field.insert(0, str(current_input) + str(digit))

    def on_math(math):
        first_number = input_field.get()
        global f_number, action
        action, f_number = math, int(first_number)
        input_field.delete(0, END)

    def on_eql():
        second_number = input_field.get()
        input_field.delete(0, END)
        input_field.insert(0, f_number + int(second_number))
        global action
        math, result = '', 0
        if action == "add":
            math, result = '+', f_number + int(second_number)
        elif action == "sub":
            math, result = '-', f_number - int(second_number)
        elif action == "mul":
            math, result = 'X', f_number * int(second_number)
        elif action == "dev":
            math, result = '/', f_number / int(second_number)
        elif action == "exp":
            math, result = '^', f_number ** int(second_number)
        r = Label(root, width=40, text=f'{f_number} {math} {int(second_number)} = {result}',
                  bg="black", fg='white', relief="solid").grid(row=8, columnspan=5)
        input_field.delete(0, END)

    def on_delete():
        input_field.delete(0, END)

    Button(root, text="1", padx=31, pady=3.5, relief="solid", command=lambda: on_click(1), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=3, column=0)
    Button(root, text="2", padx=31, pady=3.5, relief="solid", command=lambda: on_click(2), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=3, column=1)
    Button(root, text="3", padx=31, pady=3.5, relief="solid", command=lambda: on_click(3), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=3, column=2)
    Button(root, text="4", padx=31, pady=3.5, relief="solid", command=lambda: on_click(4), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=2, column=0)
    Button(root, text="5", padx=31, pady=3.5, relief="solid", command=lambda: on_click(5), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=2, column=1)
    Button(root, text="6", padx=31, pady=3.5, relief="solid", command=lambda: on_click(6), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=2, column=2)
    Button(root, text="7", padx=31, pady=3.5, relief="solid", command=lambda: on_click(7), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=1, column=0)
    Button(root, text="8", padx=31, pady=3.5, relief="solid", command=lambda: on_click(8), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=1, column=1)
    Button(root, text="9", padx=31, pady=3.5, relief="solid", command=lambda: on_click(9), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=1, column=2)
    Button(root, text="0", padx=31, pady=3.5, relief="solid", command=lambda: on_click(0), bg="black",
           fg='white', font=('Helvetica', '20')).grid(row=4, column=0)
    Button(root, text="+", padx=31, pady=3.5, relief="solid", command=lambda: on_math('add'), bg="gray7",
           fg='white', font=('Helvetica', '20')).grid(row=4, column=2)
    Button(root, text="-", padx=34, pady=3.5, relief="solid", command=lambda: on_math('sub'), bg="gray7",
           fg='white', font=('Helvetica', '20')).grid(row=4, column=1)
    Button(root, text="X", padx=30, pady=3.5, relief="solid", command=lambda: on_math('mul'), bg="gray7",
           fg='white', font=('Helvetica', '20')).grid(row=5, column=0)
    Button(root, text="/", padx=34, pady=3.5, relief="solid", command=lambda: on_math('dev'), bg="gray7",
           fg='white', font=('Helvetica', '20')).grid(row=5, column=1)
    Button(root, text="^", padx=33, pady=3.5, relief="solid", command=lambda: on_math('exp'), bg="gray7",
           fg='white', font=('Helvetica', '20')).grid(row=5, column=2)
    Button(root, text="=", padx=41, pady=20, relief="solid", command=on_eql, bg="SteelBlue3", fg='white'
           ).grid(row=6, column=2)
    Button(root, text="clear", padx=58, pady=5, relief="solid", command=on_delete, bg="gray7", fg='white',
           font=('Helvetica', '20')).grid(row=6, columnspan=2, column=0)
    root.mainloop()


if __name__ == '__main__':
    app()
