# def func2():
#     return 1/0

# def func1():
#     return func2()

# func1()

# В терминале мы увидим стек распространение ошибки
# (ошибка зародилась в func2, потом исключение перешло в func1, потом перешло в место вызова функции func1())
# обрабатывать исключения можно В ЛЮБОМ МЕСТЕ стека распространения исключений


# Если закомментировать все блоки try/except кроме одного(любого), то исключение будет обработано
# Важно, что обрабатываются первое исключение, а остальные уже нет
def f2():
    try:
        return 1/0
    except:
        print("Ошибка f2")


def f1():
    try:
        return f2()
    except:
        print("Ошибка f1")


try:
    f1()
except:
    print("Ошибка при вызове f1")

print("Конец кода")


# Принято, что нижние функции служат для обработки данных(и могут генерировать исключения),
# а верхние для формирования сервисной информации(и обработки исключений) для пользователя
