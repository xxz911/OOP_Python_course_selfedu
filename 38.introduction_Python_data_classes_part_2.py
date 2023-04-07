from dataclasses import dataclass, field, InitVar


# Предположим нам надо создать класс данных c исчисляемым локальным свойством экземпляров класса
class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


# Создаем класс данных
# Параметры @dataclass
# init=True - флаг для создания метода __init__(),
# repr=True - флаг для создания метода __repr__(),
# eq=True - флаг для создания метода __eq__(),
# order=False - флаг для создания методов сравнения(<,<=,>,>=) класса,
# unsafe_hash=False - флаг для создания метода __hash__(),
# frozen=False - флаг для создания неизменяемого типа
# match_args=True - создает кортеж __match_args__ из списка аргументов (добавлено в Python 3.10),
# kw_only=False - помечает все поля класса как содержащие только ключевые слова (добавлено в Python 3.10),
# slots=False - если True, то генерирует атрибут __slots__ (добавлено в Python 3.10),
# weakref_slot=False - добавляет слот с именем __weakref__ (добавлено в Python 3.11).
@dataclass(order=True, eq=True, repr=True)
class V3D:
    # Функция field()
    # repr - булево значение указывает, использовать ли атрибут в магическом методе __repr__, по умолчанию True
    # compare - булево значение указывает использовать ли атрибут при сравнении объектов, по умолчанию True
    # default - значение по умолчанию(начальное значение)
    x: int
    y: int
    z: int
    # Чтобы выводить length при вызове print, надо прописать
    # (init=False указывает на то, что этот length не надо добавлять в параметры инициализатора)
    length: float = field(init=False, default=0)
    # InitVar автоматически передает переменную calc_len в магический метод __post_init__
    calc_len: InitVar[bool] = True

    # (инициализаторы класса,
    # которые создаются при помощи декоратора @dataclass в конце своей работы вызывают специальный метод __post_init__()
    # и именно в нем мы можем сформировать локальное свойство length)
    # Вызывается самым последним(уже существуют локальные свойства x, y, z)
    def __post_init__(self, calc_len: bool):
        # (если calc_len == True, то вычисляется length, а если False, то остаётся по умолчанию length =0)
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5 if calc_len else 0


v = V3D(1, 2, 3)
# Мы не увидим length,(до написания строки length: float = field(init=False)), но оно есть
# (потому что @dataclass прописывает в магический метод __repr__ только те атрибуты,
# которые прописаны в классе)
print(v)
# Видим length
print(v.__dict__)

# Проверяем параметры eq=True, repr=True в декораторе @dataclass
v2 = V3D(1, 2, 4)
print(v == v2)
print(v <= v2)
# frozen=True будет исключение
# v2.x = 4


