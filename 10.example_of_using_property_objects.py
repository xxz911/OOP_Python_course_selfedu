# Пример использования property из прошлого(9 урока)
# Надо разработать класс в котором:
# -ФИО
# -Возраст(целое число от 14 до 120)
# -Серия и номер паспорта в формате(ххх хххххх, где х число от 0-9)
# -Вес, в кг(вещественное число от 20 и выше)

# Импорт коллекции латинских букв
from string import ascii_letters


class Person:
    # Коллекция со строчными русскими буквами
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя-"
    # Коллекция с заглавными русскими буквами
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        # Проверяем корректность данных при создании экземпляра класса Person
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_passport(ps)
        self.verify_weight(weight)

        # Если все данные прошли проверки, то создаем локальные свойства экземпляра класса
        # Записи не содержат имен с доступом private(нет __),
        # потому что мы указываем наши сеттеры(через объект property, который имеет высший приоритет,
        # и мы не сможем обратиться напрямую к свойству, только через сеттер)
        self.fio = fio
        self.old = old
        self.passport = ps
        self.weight = weight

    # Метод класса для проверки вводимого ФИО
    @classmethod
    def verify_fio(cls, fio):
        # Проверяем являются ли введенные данные строкой
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        # Проверяем введены ли все элементы ФИО
        if len(f) < 3:
            raise TypeError("Неверный формат записи")
        # Проверяем состоят ли данные только из букв и дифиса
        leters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(leters)) > 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")

    # Метод класса для проверки вводимого Возраста
    @staticmethod
    def verify_old(old):
        # Проверяем являются ли данные целочисленным числом от 14 до 120
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым  числом от 14 до 120")

    # Метод класса для проверки вводимого Веса
    @staticmethod
    def verify_weight(w):
        # Проверяем состоят ли данные из вещественных чисел от 20 и выше
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")

    # Метод класса для проверки вводимого Паспорта
    @staticmethod
    def verify_passport(ps):
        # Проверяем состоят ли данные строкой
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        # Проверяем формат данных
        p = ps.split()
        if len(p) != 2 or len(p[0]) != 4 or len(p[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        # Проверяем состоят ли данные только из чисел
        for s in p:
            if not s.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    # Создаем ИНТЕРФЕЙС для работы с приватными свойствами через @property(с применением наших проверок для данных)
    # Для ФИО(про property смотреть в 9 уроке)
    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        # Проверяем значение, если нормально, то применяем изменения
        self.verify_fio(fio)
        self.__fio = fio

    # Для Возраста
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        # Проверяем значение, если нормально, то применяем изменения
        self.verify_old(old)
        self.__old = old

    # Для Паспорта
    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        # Проверяем значение, если нормально, то применяем изменения
        self.verify_passport(ps)
        self.__passport = ps

    # Для Веса
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        # Проверяем значение, если нормально, то применяем изменения
        self.verify_weight(weight)
        self.__weight = weight


# Создаем экземпляр класса
p = Person("Василий Николай Александрович", 30, '1234 567890', 80.0)

# Проверяем, что создали экземпляр класса
print(p.__dict__)

# Изменяем приватные данные через объект property
p.fio = "Питоневский Василий Васильевич"
p.old = 100
p.passport = '4567 890123'
p.weight = 70.0

# Читаем приватные данные через объект property(и проверяем изменились ли приватные свойства через наш ИНТЕРФЕЙС)
print(p.fio, p.old, p.passport, p.weight)
