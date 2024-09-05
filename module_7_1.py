import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        # Создаем файл, если он не существует
        if not os.path.exists(self.__file_name):
            open(self.__file_name, 'w').close()

    def get_products(self):
        file = open(self.__file_name, 'r')  # Открываем файл
        products = file.read()  # Считываем весь файл
        file.close()  # Закрываем файл
        return products  # Возвращаем сырые данные

    def add(self, *products):
        existing_products = set(self.get_products().split('\n'))  # Разделяем по новой строке
        for product in products:
            product_name = product.name
            if product_name in existing_products:
                print(f'Продукт {product_name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')  # Открываем файл для добавления
                file.write(f"{product}\n")  # Записываем продукт в файл
                file.close()  # Закрываем файл


# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
