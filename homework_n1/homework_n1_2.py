"""
Создайте программу, которая будет моделировать систему учёта товаров на складе. 
Программа должна включать следующие классы:
Товар (Product):
- атрибуты: название, количество, цена;
- методы: увеличение количества, уменьшение количества, расчёт стоимости.
Склад (Warehouse):
- атрибуты: список товаров;
- методы: добавление товара, удаление товара, расчёт общей стоимости товаров.
Продавец (Seller):
- атрибуты: имя;
- методы: продажа товара (уменьшение количества и расчёт выручки), отчёт о продажах.
Программа должна позволять добавлять товары на склад, удалять товары со склада, продавать 
товары и формировать отчёт о продажах в виде списка проданных товаров с указанием их количества 
и стоимости. Также программа должна вести логирование всех операций с товарами, чтобы можно было 
отслеживать историю изменений количества товаров на складе и продаж.
"""

import logging

# Настройка логирования
logging.basicConfig(
    filename="warehouse.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        """Увеличивает количество товара"""
        if amount > 0:
            self.quantity += amount
            logging.info(
                f"Увеличено количество товара '{self.name}' на {amount}. Новое количество: {self.quantity}"
            )
        else:
            logging.warning("Количество для увеличения должно быть положительным.")

    def decrease_quantity(self, amount):
        """Уменьшает количество товара"""
        if amount > 0:
            if self.quantity >= amount:
                self.quantity -= amount
                logging.info(
                    f"Уменьшено количество товара '{self.name}' на {amount}. Новое количество: {self.quantity}"
                )
            else:
                logging.warning(f"Недостаточно товара '{self.name}' для уменьшения на {amount}.")
        else:
            logging.warning("Количество для уменьшения должно быть положительным.")

    def calculate_total_cost(self):
        """Рассчитывает общую стоимость товара"""
        total_cost = self.quantity * self.price
        logging.info(f"Общая стоимость товара '{self.name}': {total_cost} у.е.")
        return total_cost


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Добавляет товар на склад"""
        self.products.append(product)
        logging.info(f"Товар '{product.name}' добавлен на склад.")

    def remove_product(self, product_name):
        """Удаляет товар со склада по названию."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                logging.info(f"Товар '{product.name}' удален со склада.")
                return
        logging.warning(f"Товар '{product_name}' не найден на складе.")

    def calculate_total_cost(self):
        """Рассчитывает общую стоимость всех товаров на складе."""
        total_cost = sum(product.calculate_total_cost() for product in self.products)
        logging.info(f"Общая стоимость всех товаров на складе: {total_cost} у.е.")
        return total_cost


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []

    def sell_product(self, product, quantity):
        """Продает товар, уменьшает количество и рассчитывает выручку"""
        if product.quantity >= quantity:
            product.decrease_quantity(quantity)
            revenue = quantity * product.price
            self.sales_report.append((product.name, quantity, revenue))
            logging.info(
                f"Продавец '{self.name}' продал {quantity} единиц товара '{product.name}'. Выручка: {revenue} у.е."
            )
        else:
            logging.warning(f"Недостаточно товара '{product.name}' для продажи.")

    def generate_sales_report(self):
        """Формирует отчёт о продажах"""
        report = "Отчёт о продажах:\n"
        for sale in self.sales_report:
            report += f"Товар: {sale[0]}, Количество: {sale[1]}, Выручка: {sale[2]} у.е.\n"
        logging.info(f"Сформирован отчёт о продажах продавца '{self.name}'.")
        return report


# Пример использования классов
product1 = Product("Молоток", 10, 1500)
product2 = Product("Рулетка", 20, 800)

warehouse = Warehouse()
warehouse.add_product(product1)
warehouse.add_product(product2)

seller = Seller("Иван Иванов")
seller.sell_product(product1, 2)
seller.sell_product(product2, 5)

print(seller.generate_sales_report())

warehouse.calculate_total_cost()
