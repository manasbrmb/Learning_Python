class Library:
    def __init__(self):
        self.noofBooks = 0
        self.books = []

    def add_book(self, book):
        self.noofBooks += 1
        self.books.append(book)
        print(f"{book} ")
        

    def get_noofbooks(self):
        return self.noofBooks

    def show_books(self):
        print("Total Books In Your Library:")
        for book in self.books:
            print(book)

lib = Library()
B = "Books"
l = "You Library"
print(l.center(50))
print(B.center(50))
option = ("yes", "no")
while True:
    user_input = input("Do you want to add books? (yes/no)").lower()
    while user_input not in option:
      print("Invalid Input, Please try again.")
      user_input = input("Do you want to add more books? (yes/no)").lower()
    
    if user_input == "yes":
        book = input("Enter the book name: ")
        lib.add_book(book)
    else:
        break

# get the number of books in the library
print(f"Number of books: {lib.get_noofbooks()}")

# show all the books in the library
lib.show_books()

  