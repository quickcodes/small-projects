class liberary:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def display(self):
        for books in self.books:
            print("\t-> " + books)

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print("\tReturned successfully")

    def borrowBooks(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print("\tIssued successfully")
        else:
            print("\t<= Book is not available =>")


class User:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"\n\tHello {self.name}. We are glad to see you here\n\tYou are in Quick codes library. ")

    def borrowBook(self):
        self.book = input(f"\t{self.name} enter the name of book : ")
        return self.book

    def reutrnBook(self):
        self.book = input(f"\t{self.name} enter name of book : ")
        return self.book


if __name__ == "__main__":
    yup = False
    quickCodes = liberary(["maths", "let us c", "statists", "english", "ethical hacking", "c in depth"])
    n = input("\n\n\tPlease enter your name: ")
    customer = User(n)
    customer.intro()
    while True:
        welcomeScreen = '''
        ***** PLEASE CHOOSE AN OPTION *****
        1. I want to see list of books Quick codes have.
        2. I want to issue a book.
        3. I want to Donate or return a book.
        4. All done! Exit me.

        '''

        print(welcomeScreen)
        a = input("\tPlease enter your choice: ")
        print()
        if a == '1':
            quickCodes.display()
        elif a == '2':
            quickCodes.borrowBooks(customer.borrowBook())
        elif a == '3':
            quickCodes.returnBooks(customer.reutrnBook())
        elif a == '4':
            exit()
        else:
            print("\t<= Please choose a operation between 1 to 4 =>")








