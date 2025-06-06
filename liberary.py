class Library:
    def __init__(self ,name="Unknown", id="Unknown", section="Unknown", age=0):
        self.name_library = "central_library"
        self.section = section
        self.name_employee = name
        self.id_employee = id
        self.age_employee = age
        self.books = []
        self.employees = []  # لیست برای ذخیره اطلاعات کارمندها
        
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.name} to {self.name_library}\n")
    
    def employee_info(self):
        print(f"Employee: {self.name_employee}, ID: {self.id_employee}, Section: {self.section}, Age: {self.age_employee}\n")

    def add_employee(self, name, id, section, age):
        self.employees.append({"name": name, "id": id, "section": section, "age": age})
        print(f"Added employee {name} to {self.name_library}\n")

    def list_employees(self):
        if not self.employees:
            print("No employees registered.\n")
        else:
            print("Employees list:\n")
            for emp in self.employees:
                print(f"Name: {emp['name']}, ID: {emp['id']}, Section: {emp['section']}, Age: {emp['age']}\n")
 
 
class Book:
    def __init__(self ,name ,author ,book_cover ,year_of_production ,publications ,in_stock):
        self.name = name
        self.author = author
        self.book_cover = book_cover
        self.year_of_production = year_of_production
        self.publications = publications
        self.in_stock = in_stock
        
    @staticmethod      
    def add(library):
        name = input("pls enter name of book: ")
        author = input("pls enter Author of book: ")
        book_cover = input("pls enter book_cover: ")
        try:
            year_of_production = int(input("pls enter Year_of_production of book: "))
            in_stock = int(input("pls enter Inventory of book: "))
        except ValueError:
            print("Year and Inventory must be numbers! Try again.\n")
            return
        publications = input("pls enter publications of book: ")
        for n in library.books:
            if n.name == name and n.author == author and n.book_cover == book_cover and \
            n.year_of_production == year_of_production and n.publications == publications and n.in_stock == in_stock:
                print("This book is available in the library.")
                return
            
        n_book = Book(name ,author ,book_cover ,year_of_production ,publications ,in_stock)
        library.add_book(n_book)
    
    @staticmethod
    def search(name ,library):
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
        return
    
    @staticmethod 
    def borrow(library ,name ,author ,book_cover ,year_of_production ,publications):
        for n in library.books:
            if n.name == name and n.author == author and n.book_cover == book_cover and \
            n.year_of_production == year_of_production and n.publications == publications:
                if n.in_stock > 0:
                    n.in_stock -= 1
                    print(f"Borrowed {n.name}. Remaining stock: {n.in_stock}\n")
                    return
                else:
                    print("No copies available for borrowing.\n")
                    return
                
          
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def info(self):
        print(f"Member: {self.name}, ID: {self.member_id}, Borrowed books: {len(self.borrowed_books)}\n")


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
                for p in library.books:
                    if p.name == name and p.author == author and p.book_cover == book_cover and \
                    p.year_of_production == year_of_production and p.publications == publications:
                        p.remove(library)
                        print(f"{p.name} removed from library.\n")
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
            
            
         
if __name__ == "__main__":
    library = Library()
    print("Welcome to central_library")
    while True:
        print("1-menu_of_book \n2-member_info \n3-employees_info")
        try:
            chose = int(input("please chose the number: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue
        if chose == 1:
            print("1-add Book \n2-search book \n3-remove book \n4-borrow book \n5-exit menu")
            try:
                number = int(input("please chose your request: "))
            except ValueError:
                print("Please enter a valid number!\n")
                continue
            Menu.celected(number ,library)
        elif chose == 2:
            print("Library members info: ")
            name = input("pls enter name: ")
            id = input("pls enter id: ")
            member = Member(name , id)
            member.info()
        elif chose == 3:
            print("Employees of Library info: ")
            name = input("pls enter name: ")
            try:
                id = int(input("pls enter id: "))
                section = input("pls enter section: ")
                age_employee = int(input("pls enter age: "))
                library.add_employee(name, id, section, age_employee)  # اضافه کردن کارمند به لیست
                library.list_employees()  # نمایش لیست کارمندها
            except ValueError:
                print("ID and Age must be numbers! Try again.\n")
                continue
                
            
    print("Thank you to use apps. bye👋 ")
    