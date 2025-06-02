class liberary:
    def __init__(self):
        self.name = "centeral_liberary"
        self.section = ...
        self.name_employee = ...
        self.id_employee = ...
        
        
        
        
class Book:
    def __init__(self):
        self.name = ...
        self.Author = ...
        self.book_cover = ...
        self.Year_of_production = ...
        self.publications = ...
        
        
        
class Member:
    def __init__(self):
        self.name = ...
        self.id = ...
        self.age = ...
        
        
        
        
class borrow:
    def __init__(self):
        ...
        


class Menu():
    def celected(chose):
        while True:
            if chose == 1:
                print("add Book selected:")
                book = input("pls enter name of book: ")
                Author = input("pls enter Author of book: ")
                book_cover = input("pls enter book_cover: ")
                Year_of_production = input("pls enter Year_of_production of book: ")
                publications = input("pls enter publications of book: ")
                Book.add_book(book ,Author ,book_cover ,Year_of_production ,publications )
            elif chose == 2:
                ...
            elif chose == 3:
                ...
            elif chose == 4:
                ...
            elif chose == 5:
                ...
            
            
            
    
        
if __name__ == "__main__":
    print("Welcome to centeral_liberary")
    chose = input("please chose the number: ")
    Menu.celected(chose)
    print("Thank you to use apps. bye👋 ")
    