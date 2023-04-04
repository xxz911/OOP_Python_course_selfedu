# Благодаря разным пространствам имен, можем обращаться к двум разным атрибутам с одним именем
class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        # Если мы хотим создать экземпляр класса Meta, то должны указать это явно
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


# Обращаемся напрямую
print(Women.ordering)
print(Women.Meta.ordering)

# Обращаемся через экземпляры класса
# Создается только экземпляр Women, экземпляра Meta нет
w = Women('root', '12345')
print(w.ordering)
print(w.Meta.ordering)
# Прописали инициализаторы
print(w.__dict__)
print(w.meta.__dict__)

# Не следует обращаться к атрибутам основного класса из вложенного!
# (Основной класс должен использовать вложенный, а не наоборот)
