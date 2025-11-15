"""
Requirements:
Build a library management system with these functions:
Data to manage:

Books (title, author, ISBN, quantity available)
Members (member ID, name, books borrowed)

Functions you must implement:

add_book() - Add a new book to library

Take: title, author, ISBN, quantity
Store it properly


register_member() - Register a new library member

Auto-generate member ID (like LIB001, LIB002, etc.)
Take their name
Initialize empty borrowed books list


borrow_book() - Member borrows a book

Take: member ID and ISBN
Check if book is available (quantity > 0)
Reduce quantity by 1
Add to member's borrowed list
Handle errors (book not available, member doesn't exist)


return_book() - Member returns a book

Take: member ID and ISBN
Increase book quantity by 1
Remove from member's borrowed list


show_available_books() - Display all books with quantity > 0
show_member_books() - Show all books borrowed by a specific member
most_popular_book() - Find which book has been borrowed most times

You'll need to track borrow count per book



Must use:

Lists
Dictionaries
Functions
Loops
Conditionals

Menu-driven interface (like the student system)
"""

# to generate the Automatic ID use UUID

import uuid
from itertools import count

id_count = count(1)
id_prefix = "LIB"

books = []
members = []


borrowed_books = []

def view_books():
    if  not books:
        print("No Books Available.")
    else:
        for index, book in enumerate(books, start=1):
           
           print(f"  {index}. Title: {book['title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Quantity: {book['Quantity']}")
           print("----------------------------------------------------------------------------\n")

def add_book():
    book_title = input("Enter the name of book:")
    author = input("Enter the Author Name: ")
    ISBN = int(input("Enter the ISBN NO.: "))
    Quantity = int(input("Enter the No. of book Available: "))


    books.append({
        "title":book_title,
        "Author":author,
        "ISBN":ISBN,
        "Quantity":Quantity
    
    })

    print("New Book Added!!")

def register_members():

    sequnce_number = next(id_count)
    formatted_id = f"{sequnce_number:03d}" #for last 001, 002....

    # unique_uuid = uuid.uuid4().hex[8]

    # for book in books:
    #     if not book:
    #         return f"No Book is Available"
    #     print("Available Books")
    #     print("=============================================================")
    #     print(f"Title: {book['title']} and ISBN: {book['ISBN']}")
        
    
    member_id = f"{id_prefix}{formatted_id}"
    name = input("Enter the Name")
    
    # if borrowed_book == None:
    #     return f"No Book Borrowed Yet"
    # else:
    #     borrowed_book_isbn_str = input(f"Enter the ISBN No of the book {name} is borrowing")
    #     borrowed_book_isbn = int(borrowed_book_isbn_str)

        # print(f"Successfully recorded ISBN {borrowed_book_isbn} for {name}.")

    members.append({
        "Member_id":member_id,
        "Name":name
        # "borrowed_book_id":borrowed_book_isbn

    })

    print(f" Member with ID: {member_id} and Name {name} is Registered Successfully")

# def borrow_book():

#     if not books:
#         return "No Books Available"
    
#     for index, book in enumerate(books,start=1):
#         print("----Available Books----")
#         print("------------------------------------------------------------------------------")
#         print(f" {index}, Title:{book['title']} | Author: {book['author']} | ISBN: {book['ISBN']} | Quantity: {book['Quantity']}")

#     # if borrowed_books == None:
#     #     print("No one has Borrowed Books from any members!!! ")

#     # else:
        
#     #     Person_borrowing = input(f"Enter Name of borrower: {members['Name']} ")
#     #     member_id = int(input(f"ID is {members['member_id']}"))
#     #     borrow_book_Title= input(f"Enter the Borrowing Book Title {books['title']}")
#     #     borrowed_book_id = int(input(f"Enter the ISBN No. {books['ISBN']}"))
#     #     Qnty = int(input("Enter the Quantity of Book Borrowed"))

#     #     for Quantity, ISBN in books:
#     #         if Quantity > 0 and ISBN in borrowed_book_id:
#     #             books['Quantity'] = Quantity - Qnty


#     #     print("Details Entered Successfully")

#     while True:
#         try:
#             isbn_to_borrow = int(input(f"Enter the ISBN No. og book You Want {books['ISBN']}"))

#             selected_books = None
#             for book in books:
#                 if book['ISBN'] == isbn_to_borrow:
#                     selected_books = book
#                     break

#             if selected_books is None:
#                 print(f"Error: ISBN {isbn_to_borrow} not found. Please try again.")
#                 continue

#         except ValueError:
#             print("Invalid input. Please enter a numerical ISBN.")

#     if not members:
#         print("No members registered yet.")
#         return

#     while True:
#         member_id_input = input(f"Enter the Member ID borrowing the book (e.g., LIB001): ").strip().upper()
        
#         selected_member = None
#         for member in members:
#             if member['member_id'] == member_id_input:
#                 selected_member = member
#                 break
        
#         if selected_member is None:
#             print(f"Error: Member ID {member_id_input} not found. Please try again.")
#             continue
        
#         break
#     selected_books['Quantity'] -= 1


        



    

#     borrowed_books.append({
#         "Member_ID": selected_member['member_id'],
#         "Member_Name": selected_member['name'],
#         'Book_Title': selected_books['title'],
#         'Book_ISBN': selected_books['ISBN'],
#         'Quantity_Borrowed': Quantity,
#     })


def borrow_book():
    if not books:
        print("No Books Available to Borrow.")
        return 

    
    print("\n----Available Books----")
    print("------------------------------------------------------------------------------")
    for index, book in enumerate(books, start=1):
        
        print(f" {index}. Title:{book['title']} | Author: {book['Author']} | ISBN: {book['ISBN']} | Quantity: {book['Quantity']}")
    print("------------------------------------------------------------------------------\n")

    selected_book = None
    while True:
        try:
            
            isbn_to_borrow_input = input("Enter the ISBN No. of the book you want to borrow: ")
            isbn_to_borrow = int(isbn_to_borrow_input)

            
            for book in books:
                if book['ISBN'] == isbn_to_borrow:
                    selected_book = book
                    break
            
            if selected_book is None:
                print(f"Error: ISBN {isbn_to_borrow} not found. Please try again.")
                continue 

            if selected_book['Quantity'] <= 0:
                print(f"Error: Book '{selected_book['title']}' is out of stock.")
                return 

            break 
        except ValueError:
            print(f"'{isbn_to_borrow_input}' is not a valid numerical ISBN.")

    
    if not members:
        print("No members registered yet.")
        return 

    selected_member = None
    while True:
        
        print("--- Registered Members ---")
        for member in members:
             print(f"  ID: {member['member_id']}, Name: {member['name']}")
        
        member_id_input = input(f"\nEnter the Member ID borrowing the book (e.g., LIB001): ").strip().upper()
        
        for member in members:
            if member['member_id'] == member_id_input:
                selected_member = member
                break
        
        if selected_member is None:
            print(f"Error: Member ID {member_id_input} not found. Please try again.")
            continue
        
        break
    
    
    selected_book['Quantity'] -= 1 

    
    quantity_borrowed = 1 
    
    
    borrowed_books.append({
        "Member_ID": selected_member['member_id'],
        "Member_Name": selected_member['name'],
        'Book_Title': selected_book['title'],
        'Book_ISBN': selected_book['ISBN'],
        'Quantity_Borrowed': quantity_borrowed, 
    })

    print("Borrowed Successful!")
    print(f"'{selected_book['title']}' borrowed by '{selected_member['name']}'.")
    print(f"Remaining stock for '{selected_book['title']}': {selected_book['Quantity']}")


# def return_book():

#     if not borrowed_books:
#         print("There NO currently borrowed Books")
#         return
    

#     while True:
#         try:
#             book_isbn = int(input("Enter the ISBN No of BOOk Returning:  "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter a numerical ISBN.")

#     selected_book_In_library = False
#     for book in books:
#         if book['ISBN'] == book_isbn:
#             book['Quantity'] += 1
#             selected_book_In_library = True
#             print("Quantity is Updated")

#     if not selected_book_In_library:
#         print("No such Book is Available")

#         found_book = False
#         for index in range(len(borrowed_books) - 1, -1, -1):
#             if borrowed_books[index]['Book_ISBN'] == book_isbn:
#                 returned = borrowed_books.pop(index)
#                 found_book = True
#                 print(f"received Book from Borrower with Member ID: {returned['member_id']} ")

#         if not found_book:
#             print(f"Warning: ISBN {book_isbn} was found in inventory but no matching active borrowing transaction was found.")
        
#         print("Book successfully Returned!")
        
def return_book():
    if not borrowed_books:
        print("There are NO currently borrowed Books")
        return
    
    while True:
        try:
            book_isbn = int(input("Enter the ISBN No of Book Returning: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical ISBN.")

    # Update book quantity in library
    book_found_in_library = False
    for book in books:
        if book['ISBN'] == book_isbn:
            book['Quantity'] += 1
            book_found_in_library = True
            break
    
    if not book_found_in_library:
        print("This book is not in our library system.")
        return
    
    # Remove from borrowed_books list
    borrow_record_found = False
    for index in range(len(borrowed_books) - 1, -1, -1):
        if borrowed_books[index]['Book_ISBN'] == book_isbn:
            returned = borrowed_books.pop(index)  # ← FIX: Use index, not ISBN
            borrow_record_found = True
            print(f"Book received from {returned['Member_Name']} (ID: {returned['Member_ID']})")
            break
    
    if borrow_record_found:
        print("Book successfully returned!")
    else:
        print(f"Warning: Book was in library but no borrowing record found.")    

def view_borrowed_books():
    if not borrowed_books :
        print("No Books yet Borrowed")

    for index, borrowed_book in enumerate(borrowed_books, start=1):
        print(f"{index} Member ID: {borrowed_book['Member_ID']} |, Member Name: {borrowed_book['Member_Name']} | Book Title: {borrowed_book['Book_Title']} | Book ISBN: {borrowed_book['Book_ISBN']} | Qnt: {borrowed_book['Quantity_Borrowed']}")


# def popular_book():
#     total_Books_per_isbn  = 0
#     count = 0
#     for borrowed_book in borrowed_books:
#         count += borrowed_book['Quantity_Borrowed']
#         total_Books_per_isbn += borrowed_book['Book_ISBN']

       
#         top_book = max(total_Books_per_isbn)

#         top_book_title = "Unknown"
#         for book in books:
#             if book['ISBN'] == total_Books_per_isbn:
#                 top_book_title = book['Title']
        

#         print(f"The Top Popular Book in Libray is {top_book_title} with {top_book} Borrowed:")


def popular_book():
    if not borrowed_books:
        print("No books have been borrowed yet.")
        return
    
    # Count borrows per ISBN
    borrow_count = {}
    for record in borrowed_books:
        isbn = record['Book_ISBN']
        if isbn in borrow_count:
            borrow_count[isbn] += 1
        else:
            borrow_count[isbn] = 1
    
    # Find ISBN with most borrows
    max_borrows = 0
    most_popular_isbn = None
    for isbn, count in borrow_count.items():
        if count > max_borrows:
            max_borrows = count
            most_popular_isbn = isbn
    
    # Find book title
    book_title = "Unknown"
    for book in books:
        if book['ISBN'] == most_popular_isbn:
            book_title = book['title']
            break
    
    print(f"Most Popular Book: '{book_title}' (ISBN: {most_popular_isbn}) - Borrowed {max_borrows} times")
        

        



while True:

    print("-- Select from the Choice --")
    print("1. Add Books ")
    print("2. Register Members")
    print("3. View Books")
    print("4. Borrow Books")
    print("5. Return Books")
    print("6. View Borrowed Books")
    print("7. Popular Book")
    print("8. Exit")

    choice = int(input("Enter the choice"))

    if choice == 1:
        add_book()

    elif choice == 2:
        register_members()
    
    elif choice == 3:
        view_books()
    
    elif choice == 4:
        borrow_book()
    
    elif choice == 5:
        return_book()
    
    elif choice == 6:
        view_borrowed_books()
    
    elif choice == 7:
        popular_book()

    elif choice == 8:
        break
    else:
        print("Invalid Choice")
