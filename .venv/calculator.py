import math

class Calculator: # класс, отвечающий за вычесления функций с помошью math с выключением встроенный
    def evaluate(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "cotan": lambda x: 1 / math.tan(x), "log": math.log, "pi": math.pi, "e": math.e})
            return result
        except Exception as e:
            return "Ошибка: " + str(e)
