class LivingThing:
    def __init__(self, name: str):
        self._name = name 
    def breathe(self):
        return f"{self._name} กำลังหายใจ"


class Animal(LivingThing):
    def __init__(self, name: str):
        super().__init__(name) 
    def eat(self):
        return f"{self._name} กำลังกิน"
    def sleep(self):
        return f"{self._name} กำลังนอน"


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name) 
    def meow(self):
        return f"{self._name}: เมี้ยวๆ"


if __name__ == "__main__":
    cat = Cat("มิ้ว")
    print("+-----------+-----------+")
    print(cat.breathe())
    print("+-----------+")
    print(cat.eat())
    print("+-----------+")
    print(cat.sleep())
    print("+-----------+")
    print(cat.meow())
    print("+-----------+-----------+")