import tkinter


WINDOWS_COLOR = '#0e0e0e'
BUTTON_COLOR = '#414141'

root = tkinter.Tk()
label_1 = tkinter.Label(text='', padx=100, pady=10)
label_1.pack()


def main():
    create_window()
    create_buttons()
    root.mainloop()


class ButtonPress:
    def __init__(self, number):
        self.number = number

    def add_number_to_label_1(self):
        label_1['text'] += self.number


def create_window():
    root['bg'] = f'{WINDOWS_COLOR}'
    root.title('calculator_functions')
    root.geometry('320x500+100+150')
    icon = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)


def create_buttons():
    btn_1 = tkinter.Button(text='1', command=button_one.add_number_to_label_1, background=BUTTON_COLOR)
    btn_1.pack()
    btn_1.place(relx=.01, rely=.60, height=45, width=70)

    btn_2 = tkinter.Button(text='2', command=button_two.add_number_to_label_1, background=BUTTON_COLOR)
    btn_2.pack()
    btn_2.place(relx=.235, rely=.60, height=45, width=70)

    btn_3 = tkinter.Button(text='3', command=button_three.add_number_to_label_1, background=BUTTON_COLOR)
    btn_3.pack()
    btn_3.place(relx=.460, rely=.60, height=45, width=70)

    btn_4 = tkinter.Button(text='4', command=button_four.add_number_to_label_1, background=BUTTON_COLOR)
    btn_4.pack()
    btn_4.place(relx=.01, rely=.693, height=45, width=70)

    btn_5 = tkinter.Button(text='5', command=button_five.add_number_to_label_1, background=BUTTON_COLOR)
    btn_5.pack()
    btn_5.place(relx=.235, rely=.693, height=45, width=70)

    btn_6 = tkinter.Button(text='6', command=button_six.add_number_to_label_1, background=BUTTON_COLOR)
    btn_6.pack()
    btn_6.place(relx=.460, rely=.693, height=45, width=70)

    btn_7 = tkinter.Button(text='7', command=button_seven.add_number_to_label_1, background=BUTTON_COLOR)
    btn_7.pack()
    btn_7.place(relx=.01, rely=.787, height=45, width=70)

    btn_8 = tkinter.Button(text='8', command=button_eight.add_number_to_label_1, background=BUTTON_COLOR)
    btn_8.pack()
    btn_8.place(relx=.235, rely=.787, height=45, width=70)

    btn_9 = tkinter.Button(text='9', command=button_nine.add_number_to_label_1, background=BUTTON_COLOR)
    btn_9.pack()
    btn_9.place(relx=.460, rely=.787, height=45, width=70)

    btn_10 = tkinter.Button(text='0', command=button_zero.add_number_to_label_1, background=BUTTON_COLOR)
    btn_10.pack()
    btn_10.place(relx=.01, rely=.882, height=45, width=142)

    btn_11 = tkinter.Button(text='=', background=BUTTON_COLOR)
    btn_11.pack()
    btn_11.place(relx=.460, rely=.882, height=45, width=70)


button_one = ButtonPress('1')
button_two = ButtonPress('2')
button_three = ButtonPress('3')
button_four = ButtonPress('4')
button_five = ButtonPress('5')
button_six = ButtonPress('6')
button_seven = ButtonPress('7')
button_eight = ButtonPress('8')
button_nine = ButtonPress('9')
button_zero = ButtonPress('0')


if __name__ == '__main__':
    main()
