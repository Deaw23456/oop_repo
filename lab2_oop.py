
class Product:
   
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"สินค้า: {self.name} | ราคา: {self.price} | จำนวน: {self.quantity}")

    def calc_total(self) -> float:
        return self.price * self.quantity



p1 = Product("Laptop", 25000, 5)
p2 = Product("Phone", 8500, 10)
p3 = Product("Tablet", 12000, 3)


print("-------------------------------------------------+")
p1.show_info()
print(f"มูลค่ารวม: {p1.calc_total()}")
p2.show_info()
print(f"มูลค่ารวม: {p2.calc_total()}")
p3.show_info()
print(f"มูลค่ารวม: {p3.calc_total()}")
print("-------------------------------------------------+")