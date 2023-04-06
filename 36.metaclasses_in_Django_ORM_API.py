# Создаем метакласс,
# который в экземплярах класса(w) позволял формировать свойства(title, content, photo) из атрибутов класса(Women)
class Meta(type):

    # Метод для создания локальных атрибутов класса
    def create_local_attrs(self, *args, **kwargs):
        # Проходим циклом по ранее созданному словарю атрибутов Women
        for key, value in self.class_attrs.items():
            # Добавляем локальные свойства из словаря в инициализатор Women
            self.__dict__[key] = value

    # Инициализатор метакласса
    # (cls-ссылка на созданный класс, name-имя класса(Women), bases-родительские классы, attrs-атрибуты класса)
    def __init__(cls, name, bases, attrs):
        # В класс Women добавляем атрибут class_attrs (собирает все атрибуты в словарь)
        cls.class_attrs = attrs
        # В класс Women добавляем инициализатор через метод create_local_attrs метакласса Meta
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'Заголовок'
    content = 'Контент'
    photo = 'Путь к фото'


# Метакласс формирует class Women так:
# class Women():
#     class_attrs = {'title': 'Заголовок', 'content': 'Контент', 'photo': 'Путь к фото'}
#     title = 'Заголовок'
#     content = 'Контент'
#     photo = 'Путь к фото'
#
#     def __init__(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value

w = Women()
print(w.__dict__)


# Следует избегать применения метаклассов в коде,
# так как они запутывают код и являются источником трудноотслеживаемых ошибок
# СЛЕДУЕТ ИСПОЛЬЗОВАТЬ ИХ ТОЛЬКО ЕСЛИ МЫ ТОЧНО ЗНАЕМ ДЛЯ ЧЕГО И КАК МЫ ИХ ИСПОЛЬЗУЕМ

