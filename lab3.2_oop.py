# ==========================================================
# 1.(Parent_Class)
# ==========================================================
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self._owner = owner          
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"ฝากเงินสำเร็จจำนวน {amount:,} บาท")

    def get_info(self) -> None:
        print(f"เจ้าของ: {self._owner} | ยอด: {self._balance}")


# ==========================================================
# 2. Child_Class_1: SavingAccount (บัญชีออมทรัพย์)
# ==========================================================
class SavingAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float):
        super().__init__(owner, balance)
        self.__interest_rate = interest_rate  

    
    def get_info(self) -> None:
        print("--- SavingAccount ---")
        super().get_info()
        print(f"อัตราดอกเบี้ย: {self.__interest_rate}%")


# ==========================================================
# 3. Child_Class_2: CurrentAccount (บัญชีกระแสรายวัน)
# ==========================================================
class CurrentAccount(BankAccount):
    def __init__(self, owner: str, balance: float, overdraft_limit: float):
        super().__init__(owner, balance)
        self.__overdraft_limit = overdraft_limit 

    #เมธอดถอนเงินเบิกเกินบัญชี
    def withdraw(self, amount: float) -> None:

        if amount <= self._balance + self.__overdraft_limit:
            self._balance -= amount
            print(f"ถอนเงินสำเร็จจำนวน {amount:,} บาท")
        else:
            print("ไม่สามารถถอนได้: เกินวงเงินเบิกเกินบัญชีที่เราจำกัดไว้")

    def get_info(self) -> None:
        print("--- CurrentAccount ---")
        super().get_info()


# ==========================================================
# 4. Child_Class_3: LoanAccount (บัญชีเงินกู้)
# ==========================================================
class LoanAccount(BankAccount):
    def __init__(self, owner: str, loan_amount: float):
        
        super().__init__(owner, 0)
        self.__loan_amount = loan_amount


    def make_payment(self, amount: float) -> None:
        if amount > 0:
            self.__loan_amount -= amount
            print(f"ชำระหนี้สำเร็จจำนวน {amount:,} บาท")

   
    def get_info(self) -> None:
        print("--- LoanAccount ---")
        print(f"เจ้าของ: {self._owner} | ยอดหนี้คงเหลือ: {self.__loan_amount}")


# ==========================================================
# 5. print :  Object และรัน Loop
# ==========================================================
if __name__ == "__main__":

    acc1 = SavingAccount(owner="สมชาย", balance=10000, interest_rate=3.5)
    acc2 = CurrentAccount(owner="สมหญิง", balance=5000, overdraft_limit=2000)
    acc3 = LoanAccount(owner="สมศรี", loan_amount=50000)


    account_list = [acc1, acc2, acc3]


    for acc in account_list:
        acc.get_info()