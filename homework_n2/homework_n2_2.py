"""
Создайте класс, который будет представлять собой буфер данных. У класса должны быть следующие 
методы:
- add_data(data): добавить данные в буфер. 
Если в буфере уже есть хотя бы 5 элементов, вывести сообщение о переполнении буфера и очистить его.
- get_data(): получить данные из буфера. 
Если буфер пуст, вывести сообщение об отсутствии данных.
"""


class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Буфер переполнен. Очистка буфера.")
            self.buffer.clear()

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст. Данные отсутствуют.")
        else:
            return self.buffer


# Пример использования
buffer = DataBuffer()

# Добавляем данные в буфер
buffer.add_data("data1")
buffer.add_data("data2")
buffer.add_data("data3")
buffer.add_data("data4")
buffer.add_data("data5")  # Буфер переполнен, очистка буфера

# Получаем данные из буфера
print(buffer.get_data())  # Буфер пуст, данные отсутствуют

# Добавляем еще данные в буфер
buffer.add_data("data6")
buffer.add_data("data7")

# Получаем данные из буфера
print(buffer.get_data())  # Вывод: ['data6', 'data7']
