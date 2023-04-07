from dataclasses import dataclass, field, make_dataclass
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    # Не аннотируем, декоратор его не заметит
    current_uid = 0
    # Исключаем из инициализатора
    uid: int = field(init=False)

    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")
        Goods.current_uid += 1
        # Генерируем значение uid
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    # title и author будут идти последними в инициализаторе, так как вначале идут свойства из базового класса
    title: str = ""
    author: str = ""
    # price и weight будут идти 2 и 3 в инициализаторе, так как переопределяют свойства из базового класса
    price: float = 0
    weight: int or float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print("Post: post_init")


b = Book(100, 100, "Python ООП", "Васильев В.В")
# Проверяем порядок локальных свойств в инициализаторе Book
print(b)
print()

# Второй способ объявления класса данных

# Функция make_dataclass (обычно используют если надо сформировать класс данных в процессе работы программы)
# cls_name - имя класса данных,
# fields - атрибуты класса данных,
# * - произвольный набор позиционных аргументов
# bases=() - базовые классы,
# namespace=None - пространство имен,
# init=True - флаг для создания метода __init__(),
# repr=True - флаг для создания метода __repr__(),
# eq=True - флаг для создания метода __eq__(),
# order=False - флаг для создания методов сравнения класса,
# unsafe_hash=False - флаг для создания метода __hash__(),
# frozen=False - флаг для создания неизменяемого типа.


# Предположим, мы хотим создать с помощью функции make_dataclass такой класс
# class Car:
#     def __init__(self, model, max_speed, price=0):
#         self.model = model
#         self.max_speed = max_speed
#         self.price = price
#
#     def get_max_speed(self):
#         return self.max_speed


CarData = make_dataclass('CarData',
                         [('model', str),
                          # max_speed можно без аннотации
                            "max_speed",
                            ("price", float, field(default=0))],
                         namespace={"get_max_speed": lambda self: self.max_speed})

c = CarData("BMW", 256, 4096)
print(c)
print(c.get_max_speed())
