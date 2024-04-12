from tkinter import Tk, Label, Entry, Button
from calculator import Calculator
from buttons import Buttons

class UserInterface: #класс Ui, создает окно, овечает за работу ввода из окна и клавиатуры а также калькуляцию
    def __init__(self, root):
        self.root = root
        self.root.title("калькулятор")

        self.calc = Calculator()

        self.label = Label(root, text="Введите выражение:")
        self.label.grid(row=0, column=0, columnspan=4)

        self.input_entry = Entry(root)
        self.input_entry.grid(row=1, column=0, columnspan=3)

        self.result_label = Label(root, text="Результат:")
        self.result_label.grid(row=2, column=0, columnspan=4)
        self.result_value = Label(root, text="")
        self.result_value.grid(row=3, column=0, columnspan=4)

        buttons = Buttons(root, self.input_entry, self.calculate)
        buttons.create_buttons()

        self.input_entry.focus()
        self.input_entry.bind('<Key>', self.check_input)

    def check_input(self, event): # проверка ввода с клавиатуры
        allowed_characters = '0123456789.+-*/()^cistalepg'
        if event.char not in allowed_characters:
            return 'break'

    def calculate(self): # калькуляция
        expression = self.input_entry.get()
        try:
            result = self.calc.evaluate(expression)
            self.result_value.config(text=result)
        except Exception as e:
            self.result_value.config(text="Ошибка")

def main(): # функция создания и работы GUI
    root = Tk()
    ui = UserInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
