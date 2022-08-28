import tkinter


def main():
    create_window()
    grid_configure()
    create_digit_buttons()
    create_operator_buttons()
    create_equals_button()
    create_clear_button()
    root.mainloop()


def create_window():
    root['bg'] = '#131313'
    root.title('SimpleCalculator')
    root.geometry('350x436+100+150')
    icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)


def grid_configure():
    root.grid_columnconfigure(0, weight=15)
    root.grid_columnconfigure(1, weight=15)
    root.grid_columnconfigure(2, weight=15)
    root.grid_columnconfigure(3, weight=15)


def add_digit(digit):
    value = entry.get()
    if value != '':
        if value[0] == '0':
            value = value[1:]
        elif value == 'Error':
            value = ''
    entry.delete(0, tkinter.END)
    entry.insert(0, value + digit)


def add_operator(operator):
    value = entry.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    entry.delete(0, tkinter.END)
    entry.insert(0, value + operator)


def clear_entry():
    entry.delete(0, tkinter.END)
    entry.insert(0, '0')


def do_calculations():
    value = entry.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    entry.delete(0, tkinter.END)
    try:
        entry.insert(0, eval(value))
    except SyntaxError:
        entry.insert(0, 'Error')
    except NameError:
        entry.insert(0, 'Error')


def digit_button_settings(digit, row, column):
    return tkinter.Button(text=digit,
                          font=('Arial', 16),
                          command=lambda: add_digit(digit),
                          background='#585858',
                          fg='#ffffff',
                          height=3,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=5,
                                 pady=5
                                 )


def operator_button_settings(operator, row, column):
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          command=lambda: add_operator(operator),
                          background='#343434',
                          fg='#ffffff',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=5,
                                 pady=5
                                 )


def equals_button_settings(operator, row, column):
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          command=do_calculations,
                          background='#898989',
                          fg='#ffffff',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=5,
                                 pady=5
                                 )


def clear_button_settings(operator, row, column):
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          command=clear_entry,
                          background='#898989',
                          fg='#ffffff',
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=5,
                                 pady=5
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
    entry = tkinter.Entry(root,
                          justify=tkinter.RIGHT,
                          font=('Arial', 20),
                          width=18,
                          background='#131313',
                          foreground='#ffffff'
                          )
    entry.grid(row=0,
               column=0,
               columnspan=4,
               stick='we'
               )
    entry.insert(0, '0')

    main()
