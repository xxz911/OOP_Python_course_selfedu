class Point3D:
    def __init__(self, x, y, z):
        # Свойства экземпляров класса с режимом доступа (protected)(одна _)
        self._x = x
        self._y = y
        self._z = z

    # Статический метод для проверки значений(должны быть целыми числами)
    @staticmethod
    def verify_coord(coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    # Используем свой интерфейс для работы с атрибутами(property)(9, 10 уроки)
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord

# Создаем экземпляр класса Point3D
p = Point3D(1, 2, 3)
# Проверяем с какими локальными свойствами он создался
print(p.__dict__)
# ОДНАКО, теперь у нас дублирование кода с объектом property!
# Тут как раз пригодятся дескрипторы


# ДЕСКРИПТОР - это класс
# NON_DATA DESCRIPTOR
# если он имеет ТОЛЬКО специальный магический метод __get__
# DATA DESCRIPTOR
# если еще ДОПОЛНИТЕЛЬНО он имеет специальные магические методы(или один из них) __set__ и __del__

# Дескриптор определяется классом(у нас Integer)
class Integer:
    # Статический метод для проверки значений(должны быть целыми числами)
    @staticmethod
    def verify_coord2(coord2):
        if type(coord2) != int:
            raise TypeError("Координата должна быть целым числом")

    # Автоматически срабатывает, когда в классе Point3D2 создаются экземпляры класса Integer
    # (self - ссылка на создаваемый экземпляре класса(x2, y2, z2) Integer)
    # (owner - ссылка на класса Point3D2)
    # (name - имя переменной(x2, y2, z2) в классе Point3D2, которой присваивается экземпляр класса Integer)
    # В создаваемый экземпляре класса(x2, y2, z2) класса Integer создается свойство с именем переменной(_x2, _y2, _z2)
    # в классе Point3D2.
    # Этот метод создает локальный атрибут в name в экземпляре класса Integer в классе Point3D2
    # по итогу, например x2 от Integer имеет локальный атрибут name = _x2
    def __set_name__(self, owner, name):
        self.name = "_" + name

    # Геттер
    # (self - ссылка на создаваемый экземпляре класса(x2, y2, z2) Integer)
    # (instance - ссылается на текущий экземпляр(p2) класса Point3D2)
    # (owner - ссылается на класса Point3D2)
    def __get__(self, instance, owner):
        # Берем из текущий экземпляра(p2) класса Point3D2, через __dict__
        # Можем записать так
        # return instance.__dict__[self.name]
        # Лучше так, не стоит на прямую обращаться к __dict__
        return getattr(instance, self.name)

    # Сеттер
    # (self - ссылка на создаваемый экземпляре класса(x2, y2, z2) Integer)
    # (instance - ссылается на текущий экземпляр(p2) класса Point3D2)
    # (value - значение, которое мы присваиваем локальному свойству экземпляру класса pt2)
    def __set__(self, instance, value):

        # Используем наш метод для проверки введенных значений для координат
        self.verify_coord2(value)
        # В экземпляр(p2) класса Point3D2 создаем локальное свойство через __dict__, используя ключ, который сформирован
        # магическим методом __set_name__(например x2 от Integer имеет локальный атрибут name = _x2)
        # и передаем значение которое мы присваиваем локальному свойству экземпляру класса pt2
        # Можем записать так
        # instance.__dict__[self.name] = value
        # Лучше так, не стоит на прямую обращаться к __dict__
        setattr(instance, self.name, value)



class Point3D2:
    # Создаем экземпляры класса Integer('Экземпляры и будут являться ДЕСКРИПТОРАМИ(для каждой из координат')
    # Именно через них мы и будет работать(Наш интерфейс)
    x2 = Integer()
    y2 = Integer()
    z2 = Integer()

    # В инициализаторе идет обращение к нашим дескрипторам и передаются(СРАБАТЫВАЕТ СЕТТЕР) значения,
    # указанные при создании экземпляра класса Point3D2
    # (экземплярам класса Integer, которые создаются в свойствах класса Point3D2)
    def __init__(self, x2, y2, z2):
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

# Создаем экземпляр класса
p2 = Point3D2(1, 2, 3)
# Проверяем с какими локальными свойствами он создался
print(p2.__dict__)
# Используем Геттер нашего дескриптора
print(p2.z2)
# Используем Сеттер нашего дескриптора
p2.z2 = 4
print(p2.z2)
