from random import *

# # seed(23)   # явно устанавливаем начальное значение для генератора случайных чисел

# # for _ in range(10):
# #     print(randint(1, 100))

# def randint(self, a, b):
#     return self.randrange(a, b + 1)

# print(randint(10, 10, 5))

# import random

# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# import random
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lowercase_letters = ['a', 'b', 'c', ',d' 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't,' 'u', 'v', 'w', 'x', 'y', 'z']
# uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T,' 'U', 'V', 'W', 'X', 'Y', 'Z']
# unctuation = ['!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_']
# chars = ''
# sht = input('Сколько паролей нужно сгенерировать? ')
# lenght = input('Какая длинна должна быть у пароля(-ей)? ')
# is_digit1 = input('Включать-ли символы "01234567890"?(да, нет) ')
# is_upper_simbols = input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?(да, нет) ')
# is_lower_simbols = input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"?(да, нет) ')
# is_unctuation = input('Вкючать ли специальные символы "!#$%&*+-=?@^_"?(да, нет) ')
# is_odnoznachnie = input('Включать ли однозначный символы "il1Lo0O"?(да,нет) ')
# if is_digit1 == 'да':
#     chars += ''.join(digits)
# if is_upper_simbols.lower() == 'да':
#     chars += ''.join(uppercase_letters)
# if is_lower_simbols.lower() == 'да':
#     chars += ''.join(lowercase_letters)
# if is_odnoznachnie.lower() == 'да':
#     chars = chars
# if is_odnoznachnie.lower() == 'нет':
#    chars.replace("il1Lo0O", '')
# def generate_password(lenght, chars):
#     return random.sample(chars, int(lenght))
# for i in range(int(sht)):
#     print(''.join(generate_password(lenght,chars)))

import random

numbers = list(range(2, 10, 2)) + [3]

num = random.choice(numbers)
