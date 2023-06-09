class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Длинна радиуса вектора
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt = Point(1, 2)
# Несмотря на то, что мы не разрешаем в __slots__ свойство length, оно доступно,
# так как length это не локальный атрибут, а атрибут класса Point2D
print(pt.length)
pt.length = 20
print(pt.length)

# Посмотрим, как ведет себя __slots__ при наследовании


class Point2:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3(Point2):
    # Если мы пропишем пустой __slots__ в дочернем классе,
    # то в этом классе будут разрешены ТОЛЬКО свойства __slots__ из родительского класса(pt3.z = 30 будет исключение)
    # z это не строка, а кортеж, обращаем внимание на запятую
    # По итогу разрешены 3(x, y, z) локальные переменные для класса Point3
    __slots__ = "z",

    # Можем прописать сразу инициализатор с тремя значениями
    # (удалять или нет инициализатор из родительского класса не принципиально щас)
    # def __init__(self, x, y, z):
    #     self.x = x
    #     self.y = y
    #     self.z = z

    # Будет работать(с нашим инициализатором в дочернем классе)
    # pt4 = Point3(0, 0, 0)
    # print(pt4.x, pt4.y, pt4.z)


pt3 = Point3(10, 20)

# Как мы видим, Дочерний класс НЕ НАСЛЕДУЕТ __slots__ и в нем есть __dict__(причем в ней нет свойств из __slots__
# (только z),
# так как __slots__ запрещает прописывать свои свойства в __dict__(если в дочернем классе не прописан __slots__)
pt3.z = 30
print(pt3.z)

# Если мы удалим свойство x и снова создадим, то все равно они не попадут в __dict__
# (если в дочернем классе не прописан __slots__)
del pt3.x
pt3.x = 99
print(pt3.x)


