import tkinter


def main():
    create_window()
    create_digit_buttons()
    create_operator_buttons()
    create_equals_button()
    create_clear_button()
    root.mainloop()


def create_window():
    root['bg'] = '#0e0e0e'
    root.title('calculator_functions')
    root.geometry('320x500+100+150')
    icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)
    root.resizable(True, True)


def add_digit(digit):
    value = entry.get() + str(digit)
    entry.delete(0, tkinter.END)
    entry.insert(0, value)


def add_operator(operator):
    value = entry.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    entry.delete(0, tkinter.END)
    entry.insert(0, value + operator)


def clear_entry():
    entry.delete(0, tkinter.END)


def digit_button_settings(digit, row, column):
    return tkinter.Button(text=digit,
                          font=('Arial', 16),
                          command=lambda: add_digit(digit),
                          background='#414141',
                          fg='black',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=2,
                                 pady=2
                                 )


def operator_button_settings(operator, row, column):
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          command=lambda: add_operator(operator),
                          background='#4d4d4d',
                          fg='purple',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=2,
                                 pady=2
                                 )


def equals_button_settings(operator, row, column):
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          background='#4d4d4d',
                          fg='white',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=2,
                                 pady=2
                                 )


def clear_button_settings(operator, row, column):
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          command=clear_entry,
                          background='#4d4d4d',
                          fg='white',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=2,
                                 pady=2
                                 )


def create_digit_buttons():
    digit_button_settings('1', 1, 0)
    digit_button_settings('2', 1, 1)
    digit_button_settings('3', 1, 2)
    digit_button_settings('4', 2, 0)
    digit_button_settings('5', 2, 1)
    digit_button_settings('6', 2, 2)
    digit_button_settings('7', 3, 0)
    digit_button_settings('8', 3, 1)
    digit_button_settings('9', 3, 2)
    digit_button_settings('0', 4, 0)


def create_operator_buttons():
    operator_button_settings('+', 1, 3)
    operator_button_settings('-', 2, 3)
    operator_button_settings('*', 3, 3)
    operator_button_settings('/', 4, 3)


def create_equals_button():
    equals_button_settings('=', 4, 2)


def create_clear_button():
    clear_button_settings('CLR', 4, 1)


if __name__ == '__main__':
    root = tkinter.Tk()
    entry = tkinter.Entry(root, justify=tkinter.RIGHT, font=('Arial', 20), width=16)
    entry.grid(row=0, column=0, columnspan=4, stick='we')

    main()
