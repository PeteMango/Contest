"""
merchants:
    - products
        - warehouses
            - city
            - country
            - coordinates
            - stock

buyers:
    - name
    - city
    - country
    - coordinates
    - order
        - product
        - quantity

class Merchant

class Buyers

delivery strategy
3. closest to buyer
2. within the same country
1. stock availability
"""
import math

product_info = {
    'product': "laptop",
    'warehouses': [
        {
            'city': "Toronto",
            'country': "Canada",
            'coordinates': [2, 2],
            'stock': 1
        },
        {
            'city': "Montreal",
            'country': "Canada",
            'coordinates': [3, -1],
            'stock': 99
        },
        {
            'city': "Seattle",
            'country': "US",
            'coordinates': [-2, 1],
            'stock': 5
        },
        {
            'city': "London",
            'country': "UK",
            'coordinates': [10, 3],
            'stock': 10
        },
    ],
}

buyer_info_1 = {
    'buyer': {
        'name': "Tom",
        'city': "Vancouver",
        'country': "Canada",
        'coordinates': [-2, 5]
    },
    'product': "laptop",
    'quantity': 2
}

buyer_info_2 = {
    'buyer': {
        'name': "Kevin",
        'city': "New York",
        'country': "US",
        'coordinates': [4, -3]
    },
    'product': "laptop",
    'quantity': 1
}

buyer_info_3 = {
    'buyer': {
        'name': "Jack",
        'city': "Paris",
        'country': "France",
        'coordinates': [15, -3]
    },
    'product': "laptop",
    'quantity': 1
}

class Merchant:
    def __init__(self):
        self.products = []

    def add_products(self, productInfo: dict):
        p = Product(productInfo['product'])
        for l in productInfo['warehouses']:
            city, country, coordinates, stock = l['city'], l['country'], l['coordinates'], l['stock']
            p.add_item(Location(city, country, coordinates[0], coordinates[1], stock))

        self.products.append(p)

class Location:
    def __init__(self, city: str, country: str, xcoord: int, ycoord: int, stock: int):
        self.city = city
        self.country = country
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.stock = stock

    def __eq__(self, a):
        return self.xcoord == a.xcoord and self.ycoord == a.ycoord

    def __repr__(self):
        return f'city: {self.city}, country: {self.country}, stock: {self.stock}'

class Product:
    def __init__(self, pname: str):
        self.pname = pname
        self.locations = []

    def __repr__(self):
        ret = f'name: {self.pname}\n'
        for l in self.locations:
            ret += f'{l}' + '\n'
        return ret

    def add_item(self, warehouse: Location) -> None:
        self.locations.append(warehouse)

class Buyer:
    def __init__(self, buyerInfo: dict):
        self.name = buyerInfo['buyer']['name']
        self.city = buyerInfo['buyer']['city']
        self.country = buyerInfo['buyer']['country']
        self.xcoord = buyerInfo['buyer']['coordinates'][0]
        self.ycoord = buyerInfo['buyer']['coordinates'][1]
    
    def __repr__(self) -> str:
        return f'name: {self.name}, city: {self.city}, country: {self.country}'

    def buy_same_country(self, merchant: Merchant, product: str) -> list[Location]:
        pos_warehouse = []
        idx = -1
        for i, p in enumerate(merchant.products):
            if p.pname == product:
                idx = i
                break
        
        if idx == -1:
            # not found
            return []

        for l in merchant.products[idx].locations:
            if l.country == self.country:
                pos_warehouse.append(l.city)

        return pos_warehouse

    def buy_closest(self, merchant: Merchant, product: str) -> list[Location]:
        closest, warehouse = 10**9 + 7, ''
        idx = -1
        for i, p in enumerate(merchant.products):
            if p.pname == product:
                idx = i
                break

        if idx == -1:
            # not found
            return []

        for l in merchant.products[idx].locations:
            dist = math.sqrt(abs(l.xcoord - self.xcoord)**2 + abs(l.ycoord - self.ycoord)**2)

            if dist < closest:
                closest = dist
                warehouse = l.city

        return [warehouse]

    def buy_available(self, merchant: Merchant, product: str, quantity: int) -> list[Location]:
        pos_warehouse = []
        idx = -1
        for i, p in enumerate(merchant.products):
            if p.pname == product:
                idx = i
                break
        
        if idx == -1:
            # not found
            return []

        for l in merchant.products[idx].locations:
            if l.stock >= quantity:
                pos_warehouse.append(l.city)

        return pos_warehouse

    def __closest_location(self, warehouses: list[str], product: str, merchant: Merchant) -> str:
        idx = -1
        for i, p in enumerate(merchant.products):
            if p.pname == product:
                idx = i
                break
        
        if idx == -1:
            # not found
            return []
    
        closest, warehouse = 10**9 + 7, ''
        for l in merchant.products[idx].locations:
            if l.city not in warehouses:
                continue
            dist = math.sqrt(abs(l.xcoord - self.xcoord)**2 + abs(l.ycoord - self.ycoord)**2)

            if dist < closest:
                closest = dist
                warehouse = l.city

        return [warehouse]

    def buy(self, merchant: Merchant, product: str, quantity: int) -> str:
        pos_warehouse = self.buy_available(merchant, product, quantity)
        if len(pos_warehouse) == 1:
            return pos_warehouse[0]

        same_country = set(pos_warehouse).intersection(set(self.buy_same_country(merchant, product)))
        if len(same_country) == 1:
            return same_country

        return list(self.__closest_location(same_country, product, merchant))

def main():
    m = Merchant()
    m.add_products(product_info)
    # print(m.products[0])

    b1 = Buyer(buyer_info_1)
    # print(b1.buy_same_country(m, "laptop"))
    # print(b1.buy_closest(m, 'laptop'))
    # print(b1.buy_available(m, "laptop", 5))
    # print(b1.buy(m, "laptop", 5))

    b2 = Buyer(buyer_info_2)
    # print(b2.buy_same_country(m, "laptop"))
    # print(b2.buy_available(m, "laptop", 98))
    print(b2.buy(m, "laptop", 5))

    b3 = Buyer(buyer_info_3)
    # print(b3.buy_same_country(m, "laptop"))
    # print(b3.buy_closest(m, "laptop"))
    # print(b3.buy_available(m, "laptop", 100))

if __name__ == "__main__":
    main()