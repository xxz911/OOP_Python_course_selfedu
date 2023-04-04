# Формирование исключений происходит с использованием инструкции raise
# Благодаря ему мы можем сами формировать исключения
print('Первая строка')
print('Вторая строка')
print('Третья строка')
# После raise мы прописываем объект! класса исключения
# raise ZeroDivisionError("Деление на ноль")
# Можем записать и так(в e передать класс исключения с нашим сообщением)
# e = ZeroDivisionError("Деление на ноль - это наше сообщение")
# raise e
print('Четвертая строка')
print('Последняя строка')


# Пример вызова исключения(класс принтера)
# (исключение, если данные не могут попасть в принтер)

# Можем создать свою иерархию исключений
# (Создаем общий класс исключения для принтера)
class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""


# Создаем свой класс исключения
# Принято использовать для пользовательских(кастомных) исключений класс Exception,
# так как он является родительским для большинства общих исключений и в нем заложен базовый функционал
# (например отправка сообщений при исключении)


class ExceptionPrintSendData(ExceptionPrint):
    # Принято писать комментарий для чего это исключение
    """Класс для исключения при отправке данных принтеру"""
    def __init__(self, *args):
        # Если было передано наше сообщение при использовании исключения, то сообщение хранится в переменной message
        self.message = args[0] if args else None

    def __str__(self):
        # Если исключение не обработанно, то дописываем слово Ошибка и сообщение(если оно есть, если нет то None)
        return f"Ошибка: {self.message}"


class PrintData:
    # Метод самой печати
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    # Метод передачи данных в принтер
    def send_data(self, data):
        # Могут ли данные отправлены в принтер(если нет связи с принтером, то исключения)
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("Принтер не отвечает")

    # Метод связи с принтером(есть ли связь с принтером)
    def send_to_print(self, data):
        return False


p = PrintData()

# Мы можем обрабатываем исключения
try:
    p.print("123")
    # Если исключение связанное со связью принтера
except ExceptionPrintSendData:
     print('Принтер не отвечает')
     # Общий класс наших исключений(все остальные ошибки)
except ExceptionPrint:
    print("Общая ошибка печати")


# Если не обрабатываем наше исключение, то получим сообщение
# p.print("123")
# __main__.ExceptionPrintSendData: Ошибка: Принтер не отвечает

print("Конец нашего кода")