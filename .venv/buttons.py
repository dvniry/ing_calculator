from tkinter import Button

class Buttons:
    def __init__(self, root, input_entry, calculate_function):
        self.root = root
        self.input_entry = input_entry
        self.calculate_function = calculate_function

    def create_buttons(self): # создание списка функций кнопок
        buttons = [
            ('7', lambda: self.append_to_input('7')),
            ('8', lambda: self.append_to_input('8')),
            ('9', lambda: self.append_to_input('9')),
            ('(', lambda: self.append_to_input('(')),
            (')', lambda: self.append_to_input(')')),
            ('4', lambda: self.append_to_input('4')),
            ('5', lambda: self.append_to_input('5')),
            ('6', lambda: self.append_to_input('6')),
            ('*', lambda: self.append_to_input('*')),
            ('/', lambda: self.append_to_input('/')),
            ('1', lambda: self.append_to_input('1')),
            ('2', lambda: self.append_to_input('2')),
            ('3', lambda: self.append_to_input('3')),
            ('+', lambda: self.append_to_input('+')),
            ('-', lambda: self.append_to_input('-')),
            ('π', lambda: self.append_to_input('pi')),
            ('0', lambda: self.append_to_input('0')),
            ('.', lambda: self.append_to_input('.')),
            ('cos', lambda: self.append_to_input('cos(')),
            ('sin', lambda: self.append_to_input('sin(')),
            ('tan', lambda: self.append_to_input('tan(')),
            ('cotan', lambda: self.append_to_input('cotan(')),
            ('| |', lambda: self.append_to_input('abs(')),
            ('e', lambda: self.append_to_input('e')),
            ('C', self.delete_last_char),
            ('CE', self.clear_input),
            ('√', lambda: self.append_to_input('sqrt(')),
            ('^', lambda: self.append_to_input('^')),
            ('log', lambda: self.append_to_input('log(')),
            ('=', self.calculate_function)
        ]

        for i, (text, command) in enumerate(buttons): # создание кнопок в окне
            button = Button(self.root, text=text, command=command, width=4, height=2)
            if text == 'C':
                button.grid(row=4, column=3, sticky='news', padx=5, pady=5)
            elif text == 'CE':
                button.grid(row=4, column=4, sticky='news', padx=5, pady=5)
            elif text == '√':
                button.grid(row=4, column=0, sticky='news', padx=5, pady=5)
            elif text == '^':
                button.grid(row=4, column=1, sticky='news', padx=5, pady=5)
            elif text == 'log':
                button.grid(row=4, column=2, sticky='news', padx=5, pady=5)
            elif text == '=':
                button.grid(row=8, column=3,columnspan=2, rowspan=3, sticky='news', padx=5, pady=5)
            elif (i>=15):
                button.grid(row=i // 3 + 3, column=i % 3, sticky='news', padx=5, pady=5)
            else:
                button.grid(row=i // 5 + 5, column=i % 5, sticky='news', padx=5, pady=5)

    def append_to_input(self, value): # функция ввода
        current_input = self.input_entry.get()
        self.input_entry.delete(0, 'end')
        self.input_entry.insert('end', current_input + value)

    def delete_last_char(self): # функция удаления 1 символа
        current_input = self.input_entry.get()
        self.input_entry.delete(len(current_input) - 1, 'end')

    def clear_input(self): # функция очистки
        self.input_entry.delete(0, 'end')