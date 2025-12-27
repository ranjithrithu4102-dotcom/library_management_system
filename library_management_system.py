class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_issued=False


class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def display_book(self):
        if not self.books:
            print("no books availbale.")    
            return

        for book in self.books:
            status="issued" if book.is_issued else "available"
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")
   
    def issue_book(self,book_id):
        for book in self.books:
            if book.book_id== book_id:
                if not book.is_issued:
                    book.is_issued=True
                    print("book issued successfully.")
                else:
                    print("book already issued.")    
                return
        print ("book not found.")



    def return_book(self,book_id):
            for book in self.books:
                if book.book_id==book_id:
                    if book.is_issued:
                        book.is_issued=False
                        print("book returned successfully.")
                    else: 
                        print("book was not issued.") 
                    return
            print("book not found.") 


library=Library()         


while True:
        print("\n----- Library Management System -----")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")    

        choice=input("enter your choice: ")     


        if choice=="1":
            book_id = input("enter book ID: ")  
            title = input("enter book title: ")
            author = input("enter author name: ")
            book=Book(book_id,title,author)
            library.add_book(book)


        elif choice=="2":
            library.display_book()

        elif choice=="3":
            book_id=input("enter book ID to issue: ")    
            library.issue_book(book_id)   

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)    

        elif choice=="5":
            print("exiting library system.")    
            break
        else:
            print("invaild choice.try again.")