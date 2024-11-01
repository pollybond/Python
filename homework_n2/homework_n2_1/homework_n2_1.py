"""
Создайте функцию, которая будет открывать файл, считывать его содержимое и выводить 
на экран только те строки, которые содержат числовые значения. Если файл не найден, 
должно возникнуть исключение FileNotFoundError, если внутри файла попалось значение 
отличное от числа, должно возникнуть исключение TypeError. Файл должен иметь текстовый формат.
"""


def read_numeric_lines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()

        for line in data:
            try:
                # Удаляем символы новой строки и пробелы
                cleaned_line = line.strip()

                # Проверяем, является ли строка числом
                if cleaned_line.isdigit():
                    print(cleaned_line)
                else:
                    # Пытаемся преобразовать строку в число
                    float(cleaned_line)
                    print(cleaned_line)
            except ValueError:
                # Если строка не является числом, вызываем исключение TypeError
                raise TypeError(f"Строка '{cleaned_line}' содержит нечисловое значение")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден")
    except TypeError as te:
        print(te)


# Пример использования
read_numeric_lines("test.txt")
