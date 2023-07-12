
from tkinter import *
from tkinter import ttk

#colors
co0 = "#ffffff"  #white
co1 = "#000000"  #black
co2 = "#ED61AE"  #light pink
co3 = "#23800E"  #darker_green
co4 = "#BEFC03"  #lime


window = Tk()
window.title('')
window.geometry('475x475')
window.resizable(width=False, height=False)
window.configure(bg=co0)

style = ttk.Style()
style.theme_use('clam')

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

def convert():
    def number_to_decimal(number, base):
        try:
            decimal = int(number, base)
        except ValueError:
            l_binary['text'] = "Invalid input for selected base"
            l_octal['text'] = ""
            l_decimal['text'] = ""
            l_hexadecimal['text'] = ""
            return

        binary = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        l_binary['text'] = str(binary[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexadecimal[2:]).upper()

    base = combo.get()
    number = e_value.get()

    if base == 'BINARY':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    else:
        base = 16

    number_to_decimal(number, base)


#frames
frame_up = Frame(window, width=400, height=60, bg=co0, pady=0, padx=10)
frame_up.grid(row=1, column=0)

frame_down = Frame(window, width=400, height=300, bg=co0, pady=12, padx=0)
frame_down.grid(row=2, column=0)

app_name = Label(frame_up, text="Numeric Base Converter", anchor="center", font="Arial 20", bg=co2, fg=co1)
app_name.place(x=3, y=15)

bases = ['DECIMAL', 'BINARY', 'OCTAL', 'HEXADECIMAL']

combo = ttk.Combobox(frame_down, width=14, justify="center", font='Arial 11 bold')
combo['values'] = bases
combo.current(0)
combo.place(x=30, y=10)

e_value = Entry(frame_down, width=25, justify="center", font=("", 13), highlightthickness=1, relief=SOLID)
e_value.place(x=170, y=10)

b_converter = Button(frame_down, command=convert, text="CONVERT", height=1, bg=co4, fg=co1, font='Arial 8 bold', relief=RAISED, overrelief=RIDGE)
b_converter.place(x=338, y=10)

l_decimal = Label(frame_down, text="DECIMAL", width=14, height=1, relief="flat", anchor='nw', font='Arial 12', bg=co3, fg=co0)
l_decimal.place(x=35, y=60)
l_decimal = Label(frame_down, text="", width=25, height=1, relief="flat", anchor='center', font='Arial 12', fg=co1)
l_decimal.place(x=170, y=60)

l_binary = Label(frame_down, text="BINARY", width=14, height=1, relief="flat", anchor='nw', font='Arial 12', bg=co3, fg=co0)
l_binary.place(x=35, y=100)
l_binary = Label(frame_down, text="", width=25, height=1, relief="flat", anchor='center', font='Arial 12', fg=co1)
l_binary.place(x=170, y=100)

l_octal = Label(frame_down, text="OCTAL", width=14, height=1, relief="flat", anchor='nw', font='Arial 12', bg=co3, fg=co0)
l_octal.place(x=35, y=140)
l_octal = Label(frame_down, text="", width=25, height=1, relief="flat", anchor='center', font='Arial 12', fg=co1)
l_octal.place(x=170, y=140)

l_hexadecimal = Label(frame_down, text="HEXADECIMAL", width=14, height=1, relief="flat", anchor='nw', font='Arial 12', bg=co3, fg=co0)
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_down, text="", width=25, height=1, relief="flat", anchor='center', font='Arial 12', fg=co1)
l_hexadecimal.place(x=170, y=180)

window.mainloop()
