class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom вызван для :{self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


# Наследуемся от Geom
class Line(Geom):
    # Если в дочернем классе есть атрибут, который есть в родительском, то это ПЕРЕОПРЕДЕЛЕНИЕ БАЗОВОГО КЛАССА
    name = "Line"

    # Если в дочернем классе есть атрибут, которого нет в родительском, то это РАСШИРЕНИЕ БАЗОВОГО КЛАССА
    def draw(self):
        print("Рисование линии")


# Наследуемся от Geom
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, full=None):
        # Явно вызываем инициализатор родительского класса(для создания х-ов и y-ов)
        # Функция super() возвращает ссылку на ОБЪЕКТ ПОСРЕДНИК(через который происходит вызов метода базового класса)
        # Вызов методов базового класса через функцию super() называется ДЕЛЕГИРОВАНИЕМ
        # Вызов __init__ базового класса следует делать ВНАЧАЛЕ
        # (иначе дефолтные значения в дочернем инициализаторе могут не применится,)
        super().__init__(x1, y1, x2, y2)
        print("Инициализатор Rect")
        self.full = full

    # Если в дочернем классе есть атрибут, которого нет в родительском, то это РАСШИРЕНИЕ БАЗОВОГО КЛАССА
    def draw(self):
        print("Рисование прямоугольника")


# () вызывают магический метод __call__(берется из метакласса)
# в котором вызываются магические методы __new__, __init__,
# они ищутся сначала в дочернем классе, если метода там нет, то в родительском классе)
l = Line(0, 1, 2, 3)
r = Rect(1, 1, 2, 2)
print('Локальные свойства экземпляра класса r :', r.__dict__)