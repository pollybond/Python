"""
Напишите функцию, которая принимает на вход строку и выводит количество уникальных слов 
в ней, игнорируя знаки препинания и пробелы. Используйте модуль collections для этой задачи.
"""

import re
from collections import Counter


def count_unique_words(text):
    # Удаляем знаки препинания и пробелы, приводим к нижнему регистру
    cleaned_text = re.sub(r"[^\w\s]", "", text.lower())

    # Разбиваем текст на слова
    words = cleaned_text.split()

    # Подсчитываем количество вхождений каждого слова
    word_counts = Counter(words)

    # Возвращаем количество уникальных слов
    return len(word_counts)


# Тест
text = "Свищет ветер, серебряный ветер В шёлковом шелесте снежного шума."
unique_word_count = count_unique_words(text)
print(f"Количество уникальных слов: {unique_word_count}")
