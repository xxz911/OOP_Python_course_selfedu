# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключу key
# __delitem__(self, key) - удаление элемента по ключу key

# Класс с именами студентов и списком их оценок
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    # В item передается индекс
    def __getitem__(self, item):
        # Прописываем проверку(чтобы указанный индекс не превышал длину списка)
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        # Проверка ключа(индекса)
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        # Проверка значения(оценки)
        if value < 2 or value > 5:
            raise TypeError("Значение должно быть от 2 до 5")

        self.marks[key] = value

    def __delitem__(self, key):
        # Проверка ключа(индекса)
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        del self.marks[key]


s1 = Student("Tom", [5, 5, 3, 2, 5])
print(s1.marks[2])

# Если мы хотим ОБРАЩАТЬСЯ непосредственно к индексу экземпляра класса(s1[2]),
# а не через индекс локального атрибута s1.marks[2]
# нам надо прописать магический метод __getitem__
print(s1[2])

# Если мы хотим МЕНЯТЬ значения через индекс экземпляра класса(s1[2] = 4),
# нам надо прописать магический метод __setitem__
s1[2] = 2
print(s1[2])

# Если мы хотим УДАЛЯТЬ значения через индекс экземпляра класса(del s1[2]),
# нам надо прописать магический метод __delitem__
del s1[2]
print(s1.marks)

