import tkinter


WINDOWS_COLOR = '#0e0e0e'
BUTTON_COLOR = '#414141'

root = tkinter.Tk()
entry = tkinter.Entry(root, justify=tkinter.RIGHT)
entry.grid(row=0, column=0, columnspan=3)


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


def create_buttons():
    btn_1 = tkinter.Button(text='1', command=lambda: add_digit(1), background=BUTTON_COLOR)
    btn_1.grid(row=1, column=0, sticky='wens', padx=2, pady=2)
    btn_2 = tkinter.Button(text='2', command=lambda: add_digit(2), background=BUTTON_COLOR)
    btn_2.grid(row=1, column=1, sticky='wens', padx=2, pady=2)
    btn_3 = tkinter.Button(text='3', command=lambda: add_digit(3), background=BUTTON_COLOR)
    btn_3.grid(row=1, column=2, sticky='wens', padx=2, pady=2)
    btn_4 = tkinter.Button(text='4', command=lambda: add_digit(4), background=BUTTON_COLOR)
    btn_4.grid(row=2, column=0, sticky='wens', padx=2, pady=2)
    btn_5 = tkinter.Button(text='5', command=lambda: add_digit(5), background=BUTTON_COLOR)
    btn_5.grid(row=2, column=1, sticky='wens', padx=2, pady=2)
    btn_6 = tkinter.Button(text='6', command=lambda: add_digit(6), background=BUTTON_COLOR)
    btn_6.grid(row=2, column=2, sticky='wens', padx=2, pady=2)
    btn_7 = tkinter.Button(text='7', command=lambda: add_digit(7), background=BUTTON_COLOR)
    btn_7.grid(row=3, column=0, sticky='wens', padx=2, pady=2)
    btn_8 = tkinter.Button(text='8', command=lambda: add_digit(8), background=BUTTON_COLOR)
    btn_8.grid(row=3, column=1, sticky='wens', padx=2, pady=2)
    btn_9 = tkinter.Button(text='9', command=lambda: add_digit(9), background=BUTTON_COLOR)
    btn_9.grid(row=3, column=2, sticky='wens', padx=2, pady=2)
    btn_10 = tkinter.Button(text='0', command=lambda: add_digit(0), background=BUTTON_COLOR)
    btn_10.grid(row=4, column=0, sticky='wens', padx=2, pady=2)
    btn_11 = tkinter.Button(text='=', background=BUTTON_COLOR)
    btn_11.grid(row=4, column=2, sticky='wens', padx=2, pady=2)


if __name__ == '__main__':
    main()
