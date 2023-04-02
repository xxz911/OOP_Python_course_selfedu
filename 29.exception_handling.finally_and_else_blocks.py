# У try/except существуют дополнительные блоки finally, else
# else - выполняется при штатной работе блока try
# finally - выполняется всегда(вне зависимости были исключения или все сработало штатно)
# При это в функциях он выполняется ДО RETURN!
try:
    x, y = map(int, input("Введите 2 числа через пробел : ").split())
    res = x / y

    # Для работы с объектами исключений, можно использовать их псевдоним
except ZeroDivisionError as z:
    print(z)
except ValueError:
    print("Ошибка типа данных")
else:
    print('Исключений не произошло')
finally:
    print("Сообщение, вне зависимости от того, есть ли исключения или нет (конец 1-го примера кода)")



# Пример использования блока finally
# (открытие файла, код в качестве примера,
# обычно используют with open('text.txt') as f
# (сам всегда закрывает файл) и блок finally не нужен
try:
    f = open('text.txt')
    f.write('hello')
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
# Нужно всегда закрывать файл
finally:
    if f:
        f.close()
        print("Файл закрыт (конец 2-го примера кода)")


# Пример использования блока finally в функции
def get_values():
    try:
        x, y = map(int, input("Введите 2 числа через пробел : ").split())
        return x, y
    # Для работы с объектами исключений, можно использовать их псевдоним
    except ValueError:
        print("Ошибка типа данных")
        return 0, 0
    else:
        print('Исключений не произошло')
    finally:
        print("Блок finally выполняется до return")


x, y = get_values()
print(x, y, 'Конец 3-го примера кода')


# Пример вложенного try/except(явно вложенных)
try:
    x, y = map(int, input("Введите 2 числа через пробел : ").split())
    try:
        x/y
    except ZeroDivisionError:
        print("Деление на ноль")
except ValueError as v:
    print(v)
finally:
    print("Выполнился блок finally (конец 4-го примера кода)")


# Или можем записать так(вложенные блоки try/except через вызов функции)
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Деление на ноль"


res = 0
try:
    x, y = map(int, input("Введите 2 числа через пробел : ").split())
    res = div(x, y)
except ValueError as v:
    print(v)

print(res)
