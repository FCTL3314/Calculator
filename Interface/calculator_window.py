import tkinter

WINDOWS_COLOR = '#0e0e0e'
BUTTON_COLOR = '#414141'


root = tkinter.Tk()
entry = tkinter.Entry(root, justify=tkinter.RIGHT, font=('Arial', 20), width=16)
entry.grid(row=0, column=0, columnspan=3, stick='we')


def main():
    create_window()
    create_buttons()
    root.mainloop()


def create_window():
    root['bg'] = f'{WINDOWS_COLOR}'
    root.title('calculator_functions')
    root.geometry('320x500+100+150')
    icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)


def add_digit(digit):
    value = entry.get() + str(digit)
    entry.delete(0, tkinter.END)
    entry.insert(0, value)


def button_settings(digit, row, column):
    return tkinter.Button(text=digit,
                          font=('Arial', 16),
                          command=lambda: add_digit(digit),
                          background=BUTTON_COLOR,
                          height=2,
                          width=2
                          ).grid(row=row,
                                 column=column,
                                 stick='wens',
                                 padx=2,
                                 pady=2
                                 )


def create_buttons():
    button_settings('1', 1, 0)
    button_settings('2', 1, 1)
    button_settings('3', 1, 2)
    button_settings('4', 2, 0)
    button_settings('5', 2, 1)
    button_settings('6', 2, 2)
    button_settings('7', 3, 0)
    button_settings('8', 3, 1)
    button_settings('9', 3, 2)
    button_settings('0', 4, 0)
    button_settings('=', 4, 2)


if __name__ == '__main__':
    main()
