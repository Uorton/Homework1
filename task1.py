# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

number = int(input('Введите цифру дня недели: '))
if number > 7 or number < 1:
    print('Пожалуйста, повторите ввод')
elif number == 6 or number == 7:
    print("Сегодня выходной день!")
else:
    print("Сегодня НЕ выходной день!")
