# Метакласс - объект особого рода, он служит основой для других объектов(динамически создает другие классы)
# Метаклассом является type


class Point:
    MAX_COORD = 100
    MIN_COORD = 0


print(type(object))
print(type(int))
print(type(Point))


# Создадим свой класс через Метакласс такого содержания
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


# Создаем родительские классы
class B1:
    pass


class B2:
    pass


# Создаем метод
def method1(self):
    print(self.__dict__)


# Первым параметром является имя класса, потом его родители, потом его атрибуты(свойства, методы(можно лямбда функции)
A = type('Point', (B1, B2), {'MAX_COORD': 100,
                             'MIN_COORD': 0,
                             'method1': method1,
                             'method2': lambda self: self.MIN_COORD
                             })

# Можем создать экземпляр класса
pt = A()
# Проверяем его атрибуты
print(pt.MAX_COORD)
pt.method1()
print(pt.method2())
# Смотрим какие классы являются родительскими
print(A.__mro__)
