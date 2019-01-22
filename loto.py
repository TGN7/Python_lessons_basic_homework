#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

from random import randint

class Barrel:
    def __init__(self, name):
        vault = [x for x in range(1, 91)] 
        self.barrel = [__class__.gen_string(vault), __class__.gen_string(vault),
                     __class__.gen_string(vault)]
        self.name = name
        self.count_barrel = 15  

    def gen_string(vault): 
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            digit = randint(0, x) 
            while string[digit] != '': 
                digit += 1
            string[digit] = vault.pop(randint(0, len(vault) - 1))
        return string

    def __str__(self):
        rez = '{:-^26}\n'.format(self.name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.barrel[x]) + '\n'
        return rez + '--------------------------'


player1 = Barrel('Карточка игрока')
player2 = Barrel('Карточка компьютера')

vault = [x for x in range(1, 91)]  

while True:
    if len(vault) < 1:
        print('Бочонки в мешке закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'
              .format(player2.count_barrel, player1.count_barrel))
        break
    barrel = vault.pop(randint(0, len(vault) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(vault)))
    print(player1)
    print(player2)
    reply = input('Зачеркнуть цифру? (y/n)')
    reply = reply.lower()
    while len(reply) == 0 or reply not in 'yn':
        print('\n\n!!! Ответ не распознан!\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(vault)))
        print(player1)
        print(player2)
        reply = input('Зачеркнуть цифру? (y/n)')
        reply = reply.lower()
    if reply == 'y':
        check = False
        for x in range(3):
            if barrel in player1.barrel[x]:
                check = True
                player1.barrel[x][player1.barrel[x].index(barrel)] = '-'
                player1.count_barrel -= 1
            if barrel in player2.barrel[x]:
                player2.barrel[x][player2.barrel[x].index(barrel)] = '-'
                player2.count_barrel -= 1
        if check:
            if player1.count_barrel < 1:
                print('Победа!')
                break
            elif player2.count_barrel < 1:
                print('Проигрыш...')
                break
        else:
            print('Проигрыш... Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        check = False
        for x in range(3):
            if barrel in player1.barrel[x]:
                print('Проигрыш... Такое число было на Вашей карточке!')
                check = True
                break
            if barrel in player2.barrel[x]:
                player2.barrel[x][player2.barrel[x].index(barrel)] = '-'
                player2.count_barrel -= 1
        if check:
            break
        if player1.count_barrel < 1:
            print('Победа!')
            break
        elif player2.count_barrel < 1:
            print('Проигрыш...')
