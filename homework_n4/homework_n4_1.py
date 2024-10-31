"""
Ознакомьтесь с модулем datetime в Python. Создайте программу, которая будет использовать этот 
модуль для выполнения следующих задач:
- Отображение текущей даты и времени.
- Вычисление разницы между двумя датами.
- Преобразование строки в объект даты и времени.
- Убедитесь, что ваша программа работает корректно и использует функции из модуля datetime.
"""

import datetime


def display_current_datetime():
    """Отображает текущую дату и время"""
    current_datetime = datetime.datetime.now()
    print(f"Текущая дата и время: {current_datetime}")


def calculate_date_difference(date1, date2):
    """Вычисляет разницу между двумя датами"""
    difference = date2 - date1
    print(f"Разница между датами: {difference}")


def convert_string_to_datetime(date_string, format_string):
    """Преобразует строку в объект даты и времени"""
    date_object = datetime.datetime.strptime(date_string, format_string)
    print(f"Преобразованная дата и время: {date_object}")


# Отображение текущей даты и времени
display_current_datetime()

# Вычисление разницы между двумя датами
date1 = datetime.datetime(2024, 10, 1)
date2 = datetime.datetime(2024, 10, 31)
calculate_date_difference(date1, date2)

# Преобразование строки в объект даты и времени
date_string = "2024-10-31 17:28:00"
format_string = "%Y-%m-%d %H:%M:%S"
convert_string_to_datetime(date_string, format_string)
