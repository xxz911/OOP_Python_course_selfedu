# Магические методы арифметических операций
# __add__() - для операции сложения
# __sub__() - для операции вычитания
# __mul__() - для операции умножения
# __truediv__() - для операции деления
# __floordiv__() - для операции деления без остатка
# __mod__() - для операции остатка от деления

# Модификация с началом __iname__ означает использование всех виды i=, то есть(+=, -=, *=, /= и т.д.)
# Модификации с началом __rname__ означает использование экземпляра класса на роли правого операнда

# ПРИМЕР КОДА ДЛЯ __add__() ТАК ЖЕ АКТУАЛЕН ДЛЯ ОСТАЛЬНЫХ МАГИЧЕСКИХ МЕТОДОВ АРИФМИТИЧЕСКИХ ОПЕРАЦИЙ
class Clock:
    # Переменная класса (число секунд в одном дне)
    __DAY = 86400

    # seconds: int подсказывает программисту, какой тип данных должен быть в переменной seconds,
    # но не ограничивает вводимый тип данных
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    # Метод для получения времени
    def get_time(self):
        # Вычисляем секунды
        s = self.seconds % 60
        # Вычисляем минуты
        m = (self.seconds // 60) % 60
        # Вычисляем часы
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    # Метод для формата времени (если от 0-9, то добавляется 0 слева)
    @staticmethod
    def __get_formatted(x):
        return str(x).rjust(2, "0")

    # other - это значение, которое прибавляется
    # Возвращаем НОВЫЙ экземпляр класса, старый удаляется сборщиком мусора
    def __add__(self, other):
        # Проверка типа данных
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом или Clock")
        # Если данные являются экземпляром класса Clock
        if isinstance(other, Clock):
            return Clock(self.seconds + other.seconds)
        # Данные целочисленные
        return Clock(self.seconds + other)

    # Метод, когда other является левым операндом
    def __radd__(self, other):
        return self + other

    # Метод, когда используется оператор +=
    # В котором НЕ СОЗДАЕТСЯ НОВЫЙ ЭКЗЕМПЛЯР КЛАССА
    def __iadd__(self, other):
        # Проверка
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом или Clock")
        # Переменная sc присваивается в зависимости от типа данных other
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        # Прибавляем ТЕКУЩЕМУ ЭКЗЕМЛЯРУ КЛАССА ЗНАЧЕНИЯ other
        self.seconds += sc
        # Возвращаем ТЕКУЩИЙ ЭКЗЕМПЛЯР КЛАССА
        return self


# Создаем экземпляр класса и проверяем работу нашего кода
t1 = Clock(1000)
t2 = Clock(2000)
print(t1.get_time())


# Все работает, предположим, нам надо добавить секунды, щас мы можем добавить их обращаясь к атрибуту экземпляра класса
t1.seconds = t1.seconds + 100
print(t1.get_time())


# Если мы хотим добавлять время НЕ РАБОТАЯ с локальным атрибутом класса, а с самим экземпляром класса,
# надо использовать магический метод __add__
# Равнозначно записи c1.__add__(100)
t1 = t1 + 100
print(t1.get_time())


# Складываем данные двух экземпляров класса(дописали дополнительный код в __add__)
t3 = t1 + t2
print(t3.get_time())


# Складываем данные трёх экземпляров класса
# Равно записи t1.__add__(t2)
#              t1.__add__(t3)
t4 = t1 + t2 + t3
print(t4.get_time())


# Проверяем метод __radd__(когда экземпляр класса является правым операндом)
t4 = 100 + t4
print(t4.get_time())


# Проверяем метод __iadd__
# (без него все тоже работает, НО += например подразумевает изменять экземпляр класса, а не создавать новый)
t4 += 5
print(t4.get_time())