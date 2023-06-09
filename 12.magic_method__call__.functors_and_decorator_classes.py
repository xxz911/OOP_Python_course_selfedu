# Магические методы еще называют DUNDER-методы(от англ double underscope)
import math


# Класс счётчик
class Counter:
    def __init__(self):
        self.__counter = 0

    # Магический метод для ВЫЗОВА экземпляра класса
    def __call__(self, step=1, *args, **kwargs):
        # Проверяем когда работает
        print("__call__ вызван")
        # Наш счётчик
        self.__counter += step
        return self.__counter


# При создании экземпляра класса, мы указываем (), в общем случае это оператор вызова функции,
# НО так можно вызывать классы(при вызове класса вызывается магический метод __call__)
c = Counter()
# При этом мы не можем вызвать экземпляр класса
# с() вернёт исключение!!(потому что в нем нет магического метода __call__)
# Теперь, когда мы прописали магический метод __call__ в классе, попробуем ВЫЗВАТЬ экземпляр класса(с)

# Вызываем несколько раз с, в конце проверяем работу счетчика(используем аргументы)
c()
c()
c(10)
print(c())

# Создадим еще одни экземпляр(счетчик) и проверим его(используем аргументы)
с2 = Counter()
с2(-1)
print(с2())

# Экземпляры класса которые можно ВЫЗВАТЬ(имеют магический метод __call__), называются ФУНКТОРАМИ
# Магический метод __call__ может пригодиться при замыкании функций

# Класс для удаления первых и последних символов в строке
class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        # Если первый аргумент не является строкой
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)


# Создаем экземпляр класса с набором символов для удаления
s1 = StripChars("!&?:;")
# Тут удаляем пробел
s2 = StripChars(" ")
# Передаем в параметр экземпляра класса строку из которой надо удалять
res = s1('!Привет?')
res2 = s2(' Привет!')
print(res)
print(res2)


# Магический метод __call__ может пригодиться для создания декораторов с помощью классов
# Класс Декоратор для вычисления производной определённой функции в точке x
class Derivate:
    def __init__(self, func):
        self.__fn = func

    # x - точка в которой вычисляем производную
    # dx - шаг изменения функции для вычисления производной
    def __call__(self, x, dx=0.0001, *args, **kwargs):
        # Возвращаем результат вычисления производной функции
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
# Функция для которой будет считаться производная
def df_sin(x):
    return math.sin(x)


# Если уберем декоратор с функции, то ответ изменится
print(df_sin(math.pi/3 ))

