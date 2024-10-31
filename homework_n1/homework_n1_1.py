"""
Создайте класс Animal с атрибутами name и sound, и методом makesound(), 
который будет выводить на экран звук животного. Создайте объекты Cat и Dog, 
которые будут наследоваться от класса Animal и иметь дополнительный атрибут color. 
Переопределите метод makesound() для каждого подкласса, чтобы он выводил на экран 
соответствующий звук.
"""


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} говорит: {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"{self.color} котик {self.name} говорит: {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"{self.color} собачка {self.name} говорит: {self.sound}")


# Создаем объекты Cat и Dog
cat = Cat("Рыжик", "Мяу", "Рыжий")
dog = Dog("Бобик", "Гав", "Черная")

# Вызываем метод makesound() для каждого объекта
cat.makesound()
dog.makesound()
