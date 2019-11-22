# Угадай число

import random

secretNumber = random.randint(1, 20)
print('Я загадал число от 1 до 20.')

# Сообщить угадывающему, что у него есть 6 попыток
for guessesTaken in range(1, 7):
    print('У вас есть 6 попыток, чтобы его угадать. Введите число и нажмите ENTER: ')
    guess = int(input())

    if guess < secretNumber:
        print('Загаданное число больше, чем вы ввели.')
    elif guess > secretNumber:
        print('Загаданное число меньше, чем вы ввели.')
    else:
        break  # Использованы все 6 попыток и они не верны

if guess == secretNumber:
    print('Загаданное число было: ' + str(secretNumber) + '.')
    print('Вы угадали с ' + str(guessesTaken) + '-й попытки!')
else:
    print('Увы и ах. Число, которое вы не угадали, было: ' + str(secretNumber))
