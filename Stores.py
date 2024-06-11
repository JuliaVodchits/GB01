class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        if name not in self.items:
            self.items[name] = price

    def del_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_item_price(self, name):
        if name in self.items:
            print(f"Цена товара {name} = {self.items[name]}")
            print("")
        else:
            return None

    def upd_item_price(self, name, price):
        if name in self.items:
            self.items[name] = price
            print(f"Цена товара {name} обновлена")
        print("")

    def view_items_info(self):
        print(f"Товары магазина {self.name}:")
        for name, price in self.items.items():
            print(f"{name}: {price}")
        print("")


stores = []
stores.append(Store("Лиговский", "СПб, Лиговский, 1"))
stores.append(Store("5 Углов", "СПб, Загородный проспект, 11/40"))
stores.append(Store("Новая Голландия", "СПб, наб. Адмиралтейского канала, 2"))

stores[1].add_item("Редис", 150.0)
stores[1].add_item("Морковь", 30.0)
stores[1].add_item("Икра красная", 1200.0)
stores[1].view_items_info()

stores[1].upd_item_price("Икра красная", 1300.0)
stores[1].del_item("Морковь")
stores[1].view_items_info()
stores[1].get_item_price("Редис")