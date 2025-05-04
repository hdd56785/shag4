import random

class Encryptor:
    def __init__(self, a, b):
        # Інкапсульовані змінні
        self.__a = a
        self.__b = b
        self.__result = self.__calculate()

    def __calculate(self):
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            return self.__a + self.__b
        elif operation == '-':
            return self.__a - self.__b
        elif operation == '*':
            return self.__a * self.__b
        elif operation == '/':
            return round(self.__a / self.__b, 2) if self.__b != 0 else 'Division by zero'

    def __str__(self):
        return f"Результат шифрування: {self.__result}"


class AdvancedEncryptor(Encryptor):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.__c = c
        self.__advanced_result = self.__advanced_calculate()

    def __advanced_calculate(self):
        base_result = eval(str(self))
        if isinstance(base_result, (int, float)):
            return base_result + self.__c
        return base_result

    def __str__(self):
        return f"{self.__advanced_result}"


# Використання
e1 = Encryptor(10, 5)
print(e1)

e2 = AdvancedEncryptor(10, 5, 3)
print(e2)
