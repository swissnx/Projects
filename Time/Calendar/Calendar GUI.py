
from tkinter import *
from tkinter import colorchooser
import calendar


class CalendarApp:
    def __init__(self):
        self.__win = Tk()
        self.__win.title("Calendar")
        self.__text_color = 'brown'  # Default text color
        self.__create_widgets()

    def __create_widgets(self):
        label1 = Label(self.__win, text='Enter Year: ')
        label1.grid(row=0, column=0)
        label2 = Label(self.__win, text='Enter Month: ')
        label2.grid(row=0, column=1)

        self.__year = Entry(self.__win, width=24)
        self.__year.grid(row=1, column=0, padx=16)
        self.__month = Entry(self.__win, width=3)
        self.__month.grid(row=1, column=1)

        button_month = Button(self.__win, text='Go Month', command=self.__text_month)
        button_month.grid(row=1, column=2)

        button_year = Button(self.__win, text='Go Year', command=self.__text_year)
        button_year.grid(row=1, column=3)

        self.__textfield = Text(self.__win, height=20, width=50, foreground=self.__text_color)
        self.__textfield.grid(row=3, columnspan=4)

        color_label = Label(self.__win, text='Select Text Color: ')
        color_label.grid(row=2, column=0)
        self.__color_button = Button(self.__win, text='Pick Color', command=self.__pick_color)
        self.__color_button.grid(row=2, column=1)

        button_calendar = Button(self.__win, text='Show Calendar', command=self.__show_calendar)
        button_calendar.grid(row=2, column=2)

    def __text_month(self):
        year_str = self.__year.get()
        month_str = self.__month.get()

        if year_str and month_str:
            year_int = int(year_str)
            month_int = int(month_str)
            cal_month = calendar.month(year_int, month_int)
            self.__textfield.delete(0.0, END)
            self.__textfield.insert(INSERT, cal_month)
            self.__textfield.config(foreground=self.__text_color)

    def __text_year(self):
        year_str = self.__year.get()

        if year_str:
            year_int = int(year_str)
            cal_year = ""

            for i in range(1, 13):
                cal_year += calendar.month(year_int, i) + "\n"

            self.__textfield.delete(0.0, END)
            self.__textfield.insert(INSERT, cal_year)
            self.__textfield.config(foreground=self.__text_color)

    def __pick_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.__text_color = color
            self.__textfield.config(foreground=self.__text_color)

    def __show_calendar(self):
        year_str = self.__year.get()

        if year_str:
            year_int = int(year_str)
            gui = Tk()
            gui.config(background='grey')
            gui.title("Calendar for the year")
            gui.geometry("720x720")
            gui_content = calendar.calendar(year_int)
            cal_year = Label(gui, text=gui_content, font="Consolas 10 bold")
            cal_year.grid(row=5, column=1, padx=20)
            gui.mainloop()

    def run(self):
        try:
            self.__win.mainloop()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    app_calendar = CalendarApp()
    app_calendar.run()
