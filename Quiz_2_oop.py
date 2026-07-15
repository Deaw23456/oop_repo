class Book :
    def __init__(self, isbn:str, title:str, author:str, price:int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price


class Cart : 
    def __init__(self, cart_ID:str):
        self.cart_ID = cart_ID
        self.book_in_cart = []

    def Add_book(self, book:Book) -> None :
        self.book_in_cart.append(book)

    def calculate_total(self) -> int:
        return sum(book.price for book in self.books_in_cart)
    
    def show_items(self) -> None:
        print("=== ใบเสร็จรับเงิน ===")
        print(f"รหัสตะกร้า: {self.cart_id}")
        print("รายการ:")
        
        for book in self.books_in_cart:
            print(f" - {book.title} ({book.isbn}): {book.price} บาท")
            
        print(f"ราคารวม: {self.calculate_total()} บาท")

class Bookstore:
    def __init__(self):
        self.books_stock = [] 

    def add_to_stock(self, book: Book) -> None:
        self.books_stock.append(book)


if __name__ == "__main__":
    book1 = Book("978-0132350884", "Clean Code", "Robert C. Martin", 450)
    book2 = Book("978-1234567890", "TypeScript Deep Dive", "Basarat Ali Syed", 320)
    
    shop = Bookstore()
    shop.add_to_stock(book1)
    shop.add_to_stock(book2)

    my_cart = Cart(cart_id="C001")

   
    my_cart.add_book(book1)
    my_cart.add_book(book2)

   
    my_cart.show_items()