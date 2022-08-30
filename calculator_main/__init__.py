"""The calculator_main is responsible for the interactive window and the calculator itself"""
import tkinter

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


def create_window():
    """Creates a window and sets its settings"""
    root['bg'] = '#131313'
    root.title('SimpleCalculator')
    root.geometry('350x436+100+150')
    icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)


def grid_configure():
    """Sets grid options"""
    root.grid_columnconfigure(0, weight=15)
    root.grid_columnconfigure(1, weight=15)
    root.grid_columnconfigure(2, weight=15)
    root.grid_columnconfigure(3, weight=15)


def add_digit(digit):
    """Adds the button-pressed number to the entry field"""
    value = entry.get()
    if value == '0':
        value = value[1:]
    elif not value.isdigit() and ' ' in value:
        value = ''
    entry.delete(0, tkinter.END)
    entry.insert(0, value + digit)


def add_operator(operator):
    """Adds an operator to the entry field and if the last symbol of the entry is the operator changes
     it to the new selected one"""
    value = entry.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    entry.delete(0, tkinter.END)
    entry.insert(0, value + operator)


def clear_entry():
    """Clear the entry field"""
    entry.delete(0, tkinter.END)
    entry.insert(0, '0')


def do_calculations(value):
    """Depending on the selected operators, it performs calculations"""
    if value[-1] in '+-*/':
        value = value + value[:-1]
    entry.delete(0, tkinter.END)
    try:
        entry.insert(0, eval(value))
        return eval(value)
    except SyntaxError:
        entry.insert(0, 'Syntax Error')
    except NameError:
        entry.insert(0, 'Name Error')
    except ZeroDivisionError:
        entry.insert(0, 'Zero Division Error')


def digit_button_settings(digit, row, column):
    """Indicates number button settings"""
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
    """Indicates operator button settings"""
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
    """Indicates equals button settings"""
    return tkinter.Button(text=operator,
                          font=('Arial', 16),
                          command=lambda: do_calculations(entry.get()),
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
    """Indicates clear button settings"""
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
    """Creates digit buttons"""
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
    """Creates operator buttons"""
    operator_button_settings('+', 1, 3)
    operator_button_settings('-', 2, 3)
    operator_button_settings('*', 3, 3)
    operator_button_settings('/', 4, 3)


def create_equals_button():
    """Creates equal button"""
    equals_button_settings('=', 4, 2)


def create_clear_button():
    """Creates clear button"""
    clear_button_settings('CLR', 4, 1)


def main():
    create_window()
    grid_configure()
    create_digit_buttons()
    create_operator_buttons()
    create_equals_button()
    create_clear_button()
    root.mainloop()


if __name__ == '__main__':
    main()
