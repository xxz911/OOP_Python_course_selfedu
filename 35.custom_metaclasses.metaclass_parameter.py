# В Python мы можем создавать свои метаклассы(которые используют type)
# Мы хотим создать класс следующего содержания
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


# Создаем свой метакласс(функцией)
def create_class_point(name, base, attrs):
    # Если атрибуты небыли переданы, мы добавим их, если были добавлены, то будут принимать наши значения
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0,0)


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())

print()


# Создаем свой метакласс(классом)
class Meta(type):
    # Добавляем свои атрибуты до создания класса
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD2': 200, 'MIN_COORD2': 3})
        return type.__new__(cls, name, base, attrs)

    # Добавляем свои атрибуты после создания класса
    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD2 = 200
    #     cls.MIN_COORD2 = 3


class Point2(metaclass=Meta):
    def get_coords2(self):
        return (2,2)


pt2 = Point2()
print(pt2.MAX_COORD2)
print(pt2.get_coords2())