import random

# Функция возвращает случайный ответ из 9 вариантов.

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'Да'
	elif answerNumber == 2:
		return 'Нет'
	elif answerNumber == 3:
		return 'Наверно'
	elif answerNumber == 4:
		return 'Что ты такое?'
	elif answerNumber == 5:
		return 'Может позже'
	elif answerNumber == 6:
		return 'Может раньше'
	elif answerNumber == 7:
		return 'Когда-нибудь'
	elif answerNumber == 8:
		return 'Скоро'
	elif answerNumber == 9:
		return 'Уже началось'

# Присваиваем переменной r функцию randint() модуля random с аргументами 1, 9. 
# Это значит, что каждый раз переменной r будет присваиваться одно из 9 значений аргумента 
# answerNumber функции getAnswer.	
r = random.randint(1, 9)

# Объявляем переменную fortune, которой будет присваиваться значение функции getAnswer.
fortune = getAnswer(r)

# Выводим на экран случайный ответ.
print(fortune)
