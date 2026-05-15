from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

import numpy as np

import pandas as pd
#1
class User:
    def __init__(self,_id:int,_name:str,_email:str):
        self._id=_id
        self._name=_name.strip().title()
        _email=_email.lower()
        self._email = _email
        if "@" not in _email:
            raise ValueError(f"Invalid email ")

    def _str_(self):
        return f"User(id={self._id},name='{self._name}',email='{self._email}')"
    def _del_(self):
        print(f"User {self._name} deleted")
U=User(1,"diana a","diana.abd711@gmail.COM")
print(U)
@app.get("/user1")
def get_user():
    U = User(1, "diana a", "diana.abd711@gmail.COM")
    return {str(U)}

#2
class User:
    def __init__(self,_id:int,_name:str,_email:str):
        self._id=_id
        self._name=_name
        self._email=_email
    def __str__(self):
        return f"User(id={self._id},name='{self._name}',email='{self._email}')"
    @classmethod
    def from_string(cls,data:str):
        parts=data.split(",")
        if len(parts) != 3:
            raise ValueError(f"Invalid Input format")
        _id=int(parts[0].strip())
        _name=parts[1].strip()
        _email=parts[2].strip()
        if "@" not in _email or "." not in _email:
            raise ValueError(f"Invalid Email")
        return cls(_id,_name,_email)
V=User.from_string("2,Dikosha Er,diana.abd711@gmail.COM")
print(V)


#3
class Product:
    def __init__(self,id:int,name:str,price:float,category:str):
        self.id=id
        self.name=name
        self.price=price
        self.category=category
    def __str__(self):
        return f"Product(id={self.id},name='{self.name}',price={self.price},category={self.category})"
    def __eq__(self,other):
        if not isinstance(other,Product):
            return False
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "category":self.category,
        }
p1 = Product(1, "Laptop", 1200.0, "Electronics")
p2 = Product(1, "Laptop Pro", 1500.0, "Electronics")

print(p1)

products = {p1, p2}
print(len(products))  # 1

print(p1.to_dict())


#4
class Inventory:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        for p in self.products:
            if p.id==product.id:
                return
        self.products.append(product)
    def remove_product(self,product_id:int):
        for p in self.products:
            if p.id==product_id:
                return p
        return None
    def get_all_products(self):
        return self.products
    def unique_products(self):
        return set(self.products)
    def to_dict(self):
        return {p.id:p for p in self.products}
p1 = Product(1, "Laptop", 1200, "Electronics")
p2 = Product(2, "Phone", 800, "Electronics")
p3 = Product(1, "Laptop Pro", 1500, "Electronics")

inv = Inventory()
inv.add_product(p1)
inv.add_product(p2)
inv.add_product(p3)
print(len(inv.unique_products()))
print(inv.get_all_products())
inv.remove_product(2)
print(inv.to_dict())


#5
class Product:
    def __init__(self,id:int,name:str,price:float,category:str):
        self.id=id
        self.name=name
        self.price=price
        self.category=category
class Inventory:
    def __init__(self):
        self.products=[]
    def add_product(self,product:Product):
        self.products.append(product)
    def filter_by_price(self,min_price:float)->list[Product]:
        is_expensive=lambda p:p.price>=min_price
        return[product for product in self.products if is_expensive(product)]
inv = Inventory()
inv.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
inv.add_product(Product(2, "Mouse", 25.0, "Electronics"))
inv.add_product(Product(3, "Keyboard", 150.0, "Electronics"))
expensive = inv.filter_by_price(100.0)
print([p.name for p in expensive])


#6
import datetime

class Logger:
    @staticmethod
    def log_action(user, action: str, product, filename: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{timestamp};{user._id};{action};{product.id}\n"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(log_line)

    @staticmethod
    def read_logs(filename: str):
        logs = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                t, uid, act, pid = line.strip().split(';')
                logs.append({'timestamp': t, 'user_id': uid, 'action': act, 'product_id': pid})
        return logs

#7
class Order:
    def __init__(self, order_id: int, user: User, products: list = None):
        self.id = order_id
        self.user = user
        self.products = products if products else []

    def add_product(self, product: Product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def __str__(self):
        return f"Order #{self.id} (Total: {self.total_price()})"


#8
    def most_expensive_products(self, n: int) -> list[Product]:
        return sorted(self.products, key=lambda x: x.price, reverse=True)[:n]

#9
def price_stream(products: list[Product]):
    for product in products:
        yield product.price

#10
class OrderIterator:
    def __init__(self, orders: list[Order]):
        self._orders = orders
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._orders):
            res = self._orders[self._index]
            self._index += 1
            return res
        raise StopIteration

#11
def get_prices_array(products):
    return np.array([p.price for p in products], dtype=float)
products = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"Mouse",25.0,"Electronics")]
print(get_prices_array(products))

#12
def get_price_stats(prices_array):
    mean_price = np.mean(prices_array)
    median_price = np.median(prices_array)
    return (mean_price, median_price)
print(get_price_stats(np.array([1200.0, 25.0, 450.0])))

#13
def normalize_prices(prices_array):
    min_p = np.min(prices_array)
    max_p = np.max(prices_array)
    return (prices_array - min_p) / (max_p - min_p)
print(normalize_prices(np.array([1200.0, 25.0, 450.0])))

#14
def get_categories_array(products):
    return np.array([p.category for p in products])
products14 = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"T-Shirt",20.0,"Clothing")]
print(get_categories_array(products14))

#15
def count_unique_categories(categories_array):
    return len(np.unique(categories_array))
print(count_unique_categories(np.array(["Electronics", "Clothing", "Electronics"])))

#16
def products_above_average(products):
    prices_array = np.array([p.price for p in products])
    mean_price = np.mean(prices_array)
    return [p for p in products if p.price > mean_price]

products16 = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"Mouse",25.0,"Electronics"), Product(3,"Monitor",450.0,"Electronics")]
print(products_above_average(products16))

#17
def apply_discount(prices_array):
    return prices_array * 0.9
print(apply_discount(np.array([1200.0, 25.0, 450.0])))

#18
def get_orders_matrix(orders):
    amounts = [[sum(p.price for p in o.products)] for o in orders]
    return np.array(amounts)
u1 = User(1, "Diana Abdr", "diana@gmail.com")
u2 = User(2, "Zere B", "zere.bd@gmail.com")
orders = [Order(1,u1,[Product(1,"Laptop",1200.0,"Electronics")]), Order(2,u2,[Product(2,"Mouse",25.0,"Electronics"), Product(1,"Laptop",1200.0,"Electronics")])]
print(get_orders_matrix(orders))

#19
def average_order_amount(amounts_array):
    return np.mean(amounts_array)
print(average_order_amount(np.array([1200.0, 1225.0])))

#20
def expensive_order_indices(amounts_array):
    indices = np.where(amounts_array > 1000)[0]
    return indices.tolist()
print(expensive_order_indices(np.array([1200.0, 900.0, 1500.0])))

#21
def create_users_df(users):
    data = [{
        'id': u._id,
        'name': u._name,
        'email': u._email,
        'registration_date': datetime.date.today()
    } for u in users]
    return pd.DataFrame(data)
users = [User(1,"John Doe","john@example.com"), User(2,"Alice","alice@example.com")]
print(create_users_df(users))

#22
def create_products_df(products):
    data = [{
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': p.price
    } for p in products]
    return pd.DataFrame(data)
products = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"T-Shirt",20.0,"Clothing")]
print(create_products_df(products))

#23
def merge_users_orders(users_df, orders_df):
    merged = pd.merge(users_df, orders_df, left_on='id', right_on='user_id')
    return merged[['order_id', 'name', 'total']].rename(columns={'name': 'user_name'})
users_data = {
    'id': [1, 2],
    'name': ['John', 'Alice']
}
users_df = pd.DataFrame(users_data)
orders_data = {
    'order_id': [101, 102],
    'user_id': [1, 2],
    'total': [1200, 25]
}
orders_df = pd.DataFrame(orders_data)
tapsyrma23 = merge_users_orders(users_df, orders_df)
print(tapsyrma23)

#24
def filter_orders_by_total(df, min_value):
    return df[df['total'] > min_value]
print(filter_orders_by_total(tapsyrma23, 100))

#25
def group_total_by_user(df):
    return df.groupby('user_name')['total'].sum().reset_index()
orders_user = {
    'order_id' : [101, 103, 102],
    'user_name' : ['John', 'John', 'Alice'],
    'total' : [1200, 500, 25]
}

users_df = pd.DataFrame(orders_user)
print(group_total_by_user(users_df))
#26
def average_order_by_user(df):
    return df.groupby('user_name')['total'].mean().reset_index()
print(average_order_by_user(users_df))

#27
def count_orders_by_user(df):
    return df.groupby('user_name')['order_id'].count().reset_index(name='orders_count')
print(count_orders_by_user(users_df))

#28
def avg_price_by_category(products_df):
    return products_df.groupby('category')['price'].mean().reset_index(name='mean_price')
products_data = {
    'id' : [1, 2, 3],
    'name' : ['Laptop', 'Mouse', 'Shirt'],
    'category' : ['Electronics', 'Electronics']
}

#29
def add_discounted_price(products_df):
    products_df['discounted_price'] = products_df['price'] * 0.9
    return products_df

#30
def sort_products_by_price(products_df):
    return products_df.sort_values(by='price', ascending=False)