# __iter__(self) - получение итератора для перебора объекта
# __next__(self) - переход к следующему значению и его считывание

# Класс для возврата арифметической последовательности вещественных чисел
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    # Делаем итератор из экземпляра класса
    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        # Описываем как именно формируется очередное значение нашего итерируемого объекта
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
fr2 = FRange(1, 3, 0.5)

# next(fr) равен записи fr.__next__()
# Функция next неявно вызывает ТОЛЬКО магический метод __next__(), и что вернет этот маг метод, вернет и функция next()
print(next(fr))
print(next(fr))
print(next(fr))
print('Конец', next(fr))

# Чтобы перебирать в цикле for, надо прописать магический метод __iter__(),
# так как экземпляр класса fr не может быть аргументом функции iter() без магического метода  __iter__()
# В цикле for вызов __iter__() проходит неявно, так что вызывать перед этим iter(fr2) не надо
for x in fr2:
    print(x)


# Формирует таблицу значений
class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        # rows - кол-во строк
        self.rows = rows
        # Создаем экземпляр класса FRange (формирует числа для каждой строки)
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        # Начальное кол-во строк(rows)
        self.value = 0
        return self

    # У нас возвращает не конкретное значение, а итератор
    def __next__(self):
        if self.value < self.rows:
            # увеличиваем кол-во строк
            self.value += 1
            # Возвращаем итератор для экземпляра класса fr
            return iter(self.fr)
        else:
            raise StopIteration


fr3 = FRange2D(0, 2, 0.5, 4)
# Цикл for неявно вызывает маг. метод __iter__(), делая экземпляр класса fr3 итератором,
# потом вызывает неявно маг. метод __next__() и передает в него наш итератор,
# возвращая итератор для итератор(из-за предыдущего цикла) self.fr
for row in fr3:
    # Вложенный цикл for принимая итератор(из-за предыдущего цикла) self.fr,
    # потом вызывает неявно маг. метод __next__() и передает в него наш итератор, возвращаются уже значения self.fr
    for x in row:
        print(x, end=" ")
    print()
