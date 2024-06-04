from typing import Tuple
from sortedcontainers import SortedList
from collections import defaultdict

"""
{
  product: "laptop",
  warehouses: [
    {
      city: "Toronto",
      country: "Canada",
      coordinates: [2, 2],
      stock: 1
    },
    {
      city: "Montreal",
      country: "Canada",
      coordinates: [3, -1],
      stock: 99
    },
    {
      city: "Seattle",
      country: "US",
      coordinates: [-2, 1],
      stock: 5
    },
    {
      city: "London",
      country: "UK",
      coordinates: [10, 3],
      stock: 10
    },
  ],
}

"""


class warehouse:
    def __init__(self, city: str, country: str, coordinates: Tuple, stock: int):
        self.country = country
        self.city = city
        self.coordinates = coordinates
        self.stock = stock

    def print_warehouse(self):
        print(
            f'warehouse in {self.city},{self.country} at {self.coordinates} with {self.stock}')


class product:
    def __init__(self, product_info: dict):
        self.product = product_info['product']
        self.warehouses = defaultdict(list)  # country -> warehouses

        for new_warehouse in product_info['warehouses']:
            city = new_warehouse['city']
            country = new_warehouse['country']
            coordinates = new_warehouse['coordinates']
            stock = new_warehouse['stock']

            warehosue_class = warehouse(city, country, coordinates, stock)
            self.warehouses[country].append(warehosue_class)

    def hasStock(self, inCountry: list[warehouse], need: int) -> list[warehouse]:
        ret = []
        for warehouse in inCountry:
            if warehouse.stock >= need:
                ret.append(warehouse)
        return ret

    # def warehouse_in_country(self, country: str) -> list[warehouse]:
    #     inCountry = self.warehouses[country]
    #     for warehouse in inCountry:
    #         warehouse.print_warehouse()

    #     return inCountry

    def can_fulfill(self, country: str, need: int) -> list[warehouse]:
        inCountry = self.warehouses[country]

        canfulfill = self.hasStock(inCountry=inCountry, need=need)

        for warehouse in canfulfill:
            warehouse.print_warehouse()

        return canfulfill  # return list of warehouses

    def print_product(self):
        for country, warehouse in self.warehouses.items():
            print(f'warehouses in {country}: ')
            warehouse.print_warehouse()


class allProducts:
    def __init__(self, products: list[product]):
        self.allproducts = {}  # list of all products

        for product in products:
            print(product.product)
            # maps the name of the product -> product
            self.allproducts[product.product] = product


class buyer:
    def __init__(self, buyer_info: dict):
        self.name = buyer_info['buyer']['name']
        self.city = buyer_info['buyer']['city']
        self.country = buyer_info['buyer']['country']
        self.coordinates = buyer_info['buyer']['coordinates']

        self.product = buyer_info['product']
        self.quantity = buyer_info['quantity']


"""
Go through the sorted list:
1) country 
2) 
"""


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

new_product = product(product_info=product_info)

all_products = allProducts([new_product])
"""
# input
{
  buyer: {
    name: "Tom",
    city: "Vancouver",
    country: "Canada",
    coordinates: [-2, 5]
  }
  product: "laptop",
  quantity: 1
}

# output
["Toronto", "Montreal"]
"""

buyer1 = {
    'buyer': {
        'name': "Tom",
        'city': "Vancouver",
        'country': "Canada",
        'coordinates': [-2, 5]
    },
    'product': "laptop",
    'quantity': 2
}

b1 = buyer(buyer1)

p = all_products.allproducts[b1.product]  # product class

print(p.can_fulfill(b1.country, b1.quantity))
