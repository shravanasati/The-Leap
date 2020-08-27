class Library:
    lenders = {}
    donors = {}
    booklist = []

    def __init__(self, booklist, libname, lenders, donors):
        self.booklist = booklist
        self.libname = libname
        self.lenders = lenders
        self.donors = donors

    @property
    def books(self):
        return self.booklist

    def lend(self, bookname, name):
        if bookname in self.booklist:
            self.booklist.remove(bookname)
            self.lenders.update({name.lower():bookname})
            print("Book lended successfully!!")
        else:
            print("No such book available in the directory!")

    def returnb(self, name):
        print(self.lenders.keys())
        if name.lower() in self.lenders.keys():
            self.booklist.append(self.lenders[name.lower()])
            self.lenders.pop(name.lower())
            print("Book returned successfully!")
        else:
            print("Put proper name!")

    def donate(self, kindname, newbook):
        print("Thanks", kindname)
        self.booklist.append(newbook)
        self.donors.update({kindname.capitalize():newbook})
    
Shravan_Lib = Library(["Factfulness", "Think and Grow Rich", "Rich Dad Poor Dad", "Enlightenment Now", "To Sell is Human"], "Leap ahead", {}, {})

if __name__ == "__main__":
    while True:
        print("This is the", Shravan_Lib.libname, "library!")
        op = int(input("What would you like to do:\n1. See the book list\n2. Borrow a book\n3. Donate a book\n4. Return a book\n(1/2/3/4) "))

        if op==1:
            print(Shravan_Lib.books)
            print(Shravan_Lib.donors)       

        elif op==2:
            name = input("Name: ")
            print(Shravan_Lib.books)
            print(Shravan_Lib.donors)
            book = input("Bookname: ") 
            Shravan_Lib.lend(book, name)

        elif op==3:
            name = input("Name: ")
            book = input("Bookname: ")
            Shravan_Lib.donate(name, book)
        
        else:
            name = input("Name: ")
            Shravan_Lib.returnb(name)
