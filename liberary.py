class Library:
    def __init__(self):
        self.name = "central_library"
        self.section = ...
        self.name_employee = ...
        self.id_employee = ...
        self.age_employee = ...
        self.books = []
 
class Book:
    def __init__(self ,name ,author ,book_cover ,year_of_production ,publications ,in_stock):
        self.name = name
        self.author = author
        self.book_cover = book_cover
        self.year_of_production = year_of_production
        self.publications = publications
        self.new_book = 1
        self.in_stock = in_stock
          
    def add(self ,library):
        while self.new_book == 1:
            self.new_book = 1
            name = input("pls enter name of book: ")
            author = input("pls enter Author of book: ")
            book_cover = input("pls enter book_cover: ")
            year_of_production = int(input("pls enter Year_of_production of book: "))
            publications = input("pls enter publications of book: ")
            in_stock = int(input("pls enter Inventory of book: "))
            for n in library.books:
                if n.name == name and n.author == author and n.book_cover == book_cover and \
                n.year_of_production == year_of_production and n.publications == publications and n.in_stock == in_stock:
                    print("This book is available in the library.")
                    self.new_book = 0
            
            if self.new_book == 1:
                n_book = Book(name ,author ,book_cover ,year_of_production ,publications ,in_stock)
                library.books.append(n_book)
                self.new_book = 0
            else:
                self.new_book = 0
    
    def search(self , name ,library):
        flag = 0
        while True:
            for n in library.books:
                if n.name.lower() == name.lower():   # جستجوی بدون توجه به حروف بزرگ/کوچک
                    print("Book specifications:")
                    print("name: ", n.name ,"\nAuthor: " , n.author , "\nbook_cover: " , n.book_cover , "\nYear_of_production: " ,
                    n.year_of_production , "\npublications: " , n.publications)
                    flag = 1
                    
            if flag == 0:
                print("There is no such book.")
            else:
                break
                    
    def remove(self ,library):
        library.books.remove(self)
     
    def borrow(self ,library ,name ,author ,book_cover ,year_of_production ,publications):
        for n in library.books:
            if n.name == name and n.author == author and n.book_cover == book_cover and \
            n.year_of_production == year_of_production and n.publications == publications:
                n.in_stock -= 1
                
          
class Member:
    def __init__(self):
        ...

class Menu():
    def celected(chose ,library):
        while True:
            if chose == 1:
                print("add Book selected:")
                Book.add(library)
            elif chose == 2:
                print("search book selected: ")
                search = input("pls enter name of book: ")
                Book.search(search ,library)
            elif chose == 3:
                print("remove book selected: ")
                name = input("pls enter name of book: ")
                author = input("pls enter Author of book: ")
                book_cover = input("pls enter book_cover: ")
                year_of_production = int(input("pls enter Year_of_production of book: "))
                publications = input("pls enter publications of book: ")
                for p in Library.books:
                    if p.name == name and p.author == author and p.book_cover == book_cover and \
                    p.year_of_production == year_of_production and p.publications == publications:
                        p.remove(library)
            elif chose == 4:
                print("borrow book selected: ")
                name = input("pls enter name of book: ")
                author = input("pls enter Author of book: ")
                book_cover = input("pls enter book_cover: ")
                year_of_production = int(input("pls enter Year_of_production of book: "))
                publications = input("pls enter publications of book: ")
                Book.borrow(library ,name ,author ,book_cover ,year_of_production ,publications)
            elif chose == 5:
                print("bye 👋")
                exit(0)
            
            
    
main_book = []       
if __name__ == "__main__":
    library = Library()
    print("Welcome to centeral_library")
    while True:
        print("1-menu_of_book \n2-member_info")
        chose = int(input("please chose the number: "))
        if chose == 1:
            print("1-add Book \n2-search book \n3-remove book \n4-borrow book \n5-exit menu")
            number = int(input("please chose your request: "))
            Menu.celected(number ,library)
        elif chose == 2:
            Member.info()
    print("Thank you to use apps. bye👋 ")
    