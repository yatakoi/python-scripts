# Последовательность Коллатза

# Определяем переменную collatz.
def collatz (number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    else:
        return 0

# Добавляем исключение try - expect.
# Исключение проверяет введено ли целое число. 
# Если не введено целое число, то появится ошибка "ValueError" и оператор except сообщит об этом.
try:
    number = int (input())
except ValueError:
    print ('Вы должны ввести целое число. Повторите запуск скрипта и введите ЦЕЛОЕ число.')
else: # Иначе если введено целое число, то цикл while будет выполняться до тех пор, пока значение не станет 1.
    while number != 1:
        print (number)
        number = collatz (number)
    print (1)
