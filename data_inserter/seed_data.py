import threading
from django.core.management.base import BaseCommand
from data_inserter.models import User, Product, Order

class Command(BaseCommand):
    help = 'Insert data into databases concurrently'

    def handle(self, *args, **kwargs):
        user_data = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
            {"name": "Charlie", "email": "charlie@example.com"},
            {"name": "David", "email": "david@example.com"},
            {"name": "Eve", "email": "eve@example.com"},
            {"name": "Frank", "email": "frank@example.com"},
            {"name": "Grace", "email": "grace@example.com"},
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Henry", "email": "henry@example.com"},
            {"name": "", "email": "jane@example.com"},
        ]

        product_data = [
            {"name": "Laptop", "price": 1000.00},
            {"name": "Smartphone", "price": 700.00},
            {"name": "Headphones", "price": 150.00},
            {"name": "Monitor", "price": 300.00},
            {"name": "Keyboard", "price": 50.00},
            {"name": "Mouse", "price": 30.00},
            {"name": "Laptop", "price": 1000.00},
            {"name": "Smartwatch", "price": 250.00},
            {"name": "Gaming Chair", "price": 500.00},
            {"name": "Earbuds", "price": -50.00},
        ]

        order_data = [
            {"user_id": 1, "product_id": 1, "quantity": 2},
            {"user_id": 2, "product_id": 2, "quantity": 1},
            {"user_id": 3, "product_id": 3, "quantity": 5},
            {"user_id": 4, "product_id": 4, "quantity": 1},
            {"user_id": 5, "product_id": 5, "quantity": 3},
            {"user_id": 6, "product_id": 6, "quantity": 4},
            {"user_id": 7, "product_id": 7, "quantity": 2},
            {"user_id": 8, "product_id": 8, "quantity": 0},
            {"user_id": 9, "product_id": 1, "quantity": -1},
            {"user_id": 10, "product_id": 11, "quantity": 2},
        ]

        threads = []

        def insert_users():
            for user in user_data:
                User.objects.using('users').create(**user)

        def insert_products():
            for product in product_data:
                Product.objects.using('products').create(**product)

        def insert_orders():
            for order in order_data:
                Order.objects.using('orders').create(**order)

        threads.append(threading.Thread(target=insert_users))
        threads.append(threading.Thread(target=insert_products))
        threads.append(threading.Thread(target=insert_orders))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
