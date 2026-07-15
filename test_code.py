import math

# ==========================================
# 1. คลาสฐานรากสุด / คลาสทวด (Base Class)
# ==========================================
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def move(self):
        return f"🚌 ยานพาหนะแบรนด์ {self.brand} กำลังเคลื่อนที่ไปข้างหน้า..."


# ==========================================
# [รูปแบบที่ 1 & 2] Single & Hierarchical Inheritance
# ==========================================

# 🔴 แบบที่ 1: Single Inheritance (แบบเดี่ยว) -> แม่ 1 ลูก 1 ตรงๆ
# Car สืบทอดมาจาก Vehicle ตัวเดียวโดดๆ
class Car(Vehicle):
    def __init__(self, brand: str, doors: int):
        super().__init__(brand)
        self.doors = doors

    def drive(self):
        return f"🚗 รถยนต์ {self.brand} ({self.doors} ประตู) วิ่งบนถนน"


# 🔴 แบบที่ 2: Hierarchical Inheritance (แบบลำดับขั้น) -> แม่ 1 แตกกิ่งมีลูกหลายคน
# ทั้ง Car และ Motorcycle ต่างรุมสืบทอดมาจาก Vehicle คลาสแม่คนเดียวกัน
class Motorcycle(Vehicle):
    def __init__(self, brand: str, bike_type: str):
        super().__init__(brand)
        self.bike_type = bike_type

    def ride(self):
        return f"🏍️ มอเตอร์ไซค์ {self.brand} ทรง {self.bike_type} กำลังบิดคันเร่ง!"


# ==========================================
# [รูปแบบที่ 3] Multilevel Inheritance (แบบหลายชั้น)
# ==========================================
# 🔴 แบบที่ 3: Multilevel Inheritance -> สืบทอดต่อกันเป็นทอดๆ (ทวด -> แม่ -> ลูก)
# ElectricCar สืบทอดมาจาก Car (ซึ่ง Car ก็ไปเอามาจาก Vehicle อีกทีก่อนหน้านี้)
class ElectricCar(Car):
    def __init__(self, brand: str, doors: int, battery_size: int):
        super().__init__(brand, doors)
        self.battery_size = battery_size

    def charge(self):
        return f"⚡ {self.brand} กำลังชาร์จไฟ แบตเตอรี่ขนาด {self.battery_size} kWh"


# ==========================================
# [รูปแบบที่ 4] Multiple Inheritance (แบบหลายกลุ่ม/พหุคูณ)
# ==========================================
# สร้างคลาสอิสระขึ้นมาอีกอัน เพื่อเตรียมเอาไปฟิวชั่นรวมร่าง
class AISystem:
    def __init__(self, ai_version: str):
        self.ai_version = ai_version

    def auto_drive(self):
        return f"🤖 ระบบ AI {self.ai_version} กำลังคำนวณเส้นทางและขับเคลื่อนอัตโนมัติ..."


# 🔴 แบบที่ 4: Multiple Inheritance -> ลูกคนเดียว แต่มีแม่หลายคนพร้อมกัน
# AutonomousCar สืบทอดความสามารถจากทั้ง ElectricCar และ AISystem มารวมกันในร่างเดียว
class AutonomousCar(ElectricCar, AISystem):
    def __init__(self, brand: str, doors: int, battery_size: int, ai_version: str):
        # เรียกทำงาน Constructor ของคลาสแม่ทั้งสองฝั่งให้ครบ
        ElectricCar.__init__(self, brand, doors, battery_size)
        AISystem.__init__(self, ai_version)

    def show_status(self):
        return f"🚀 ระบบพร้อม! {self.brand} รถยนต์ไฟฟ้าไร้คนขับเวอร์ชันอนาคต"


# ==========================================
# [รูปแบบที่ 5] Hybrid Inheritance (แบบผสมครอบจักรวาล)
# ==========================================
# 🔴 แบบที่ 5: Hybrid Inheritance คือภาพรวมของระบบทั้งหมดนี้เลยเว้ยเพื่อนพาร์ทเนอร์!
# มันเกิดจากการผสมผสานกันตั้งแต่ขั้นเดี่ยว ขั้นหลายชั้น และขั้นหลายกลุ่มมารวมอยู่ในโปรเจกต์เดียวกัน

# --- โซนทดสอบการทำงานของวัตถุ (Object Testing) ---
if __name__ == "__main__":
    print("--- 🛠️ เทสระบบที่ 1 & 2: Single & Hierarchical ---")
    my_car = Car("Toyota", 4)
    my_bike = Motorcycle("Honda", "Bigbike")
    print(my_car.drive())
    print(my_bike.ride())
    
    print("\n--- 🛠️ เทสระบบที่ 3: Multilevel ---")
    ev_car = ElectricCar("Tesla", 4, 85)
    print(ev_car.move())   # มรดกตกทอดมาจากคลาสทวด (Vehicle)
    print(ev_car.drive())  # มรดกตกทอดมาจากคลาสแม่ (Car)
    print(ev_car.charge()) # ความสามารถของตัวเอง
    
    print("\n--- 🛠️ เทสระบบที่ 4 & 5: Multiple & Hybrid ---")
    smart_car = AutonomousCar("Waymo", 4, 100, "v5.2")
    print(smart_car.move())        # ได้พลังมาจากสายฝั่งรถยนต์
    print(smart_car.auto_drive())  # ได้พลังมาจากสายฝั่ง AI สมองกล
    print(smart_car.show_status()) # ฟังก์ชันเฉพาะตัวของมันเอง