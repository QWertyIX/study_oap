#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime


# функция для расчёта номера текущего семестра
def sem_calc():
    cur_date = datetime.date.today()                  # взламываем компьютер и узнаём системное время
#    cur_date = datetime.date(2021, 2, 25)             # можно ввести свою дату
    st_un_date = datetime.date(2017, 8, 31)           # я поступил в этот день

    diff_date = cur_date - st_un_date                 # сравниваем даты

    if diff_date.days > 0:
        courses = diff_date.days // 365               # количество целых лет, по 2 семестра в каждом
        ex_sems = (diff_date.days % 365) // 150       # если осталось 150+ дней, значит осенний семестр уже прошёл
        return courses * 2 + ex_sems + 1              # суммируем прошедние семестры и учитываем начавшийся
    else:
        return -1                                     # передаём информацию об ошибке


# функция для определения текста информации о группе
def group_info(total_sem=sem_calc()):                 # аргументом будет число семестров из sem_calc()
    if 0 < total_sem < 13:                            # правильный диапазон семестров (1..12)
        return f'РКТ2-{total_sem}1'
    elif total_sem >= 13:                             # семестр больше 12, значит уже выпустился
        return 'инженер 2023 года выпуска'
    else:                                             # принимаем информацию об ошибке
        return 'а в вашей системе неверная дата :P'


# функция определения приветственного текста
def greeting_info(cur_time=datetime.datetime.now()):  # ещё раз взламываем систему и узнаём который час
    if 8 < cur_time.hour <= 11:                       # время, соответствующее утру
        return 'Доброе утро'
    elif 11 < cur_time.hour <= 17:                    # время, соответствующее дню
        return 'Добрый день'
    elif 17 < cur_time.hour <= 21:                    # время, соответствующее вечеру
        return 'Добрый вечер'
    else:
        return 'Здравствуйте'                         # вместо "доброй ночи"


if __name__ == '__main__':
    print(f'{greeting_info()}, я - Ерахтин Артем Олегович, {group_info()}')
