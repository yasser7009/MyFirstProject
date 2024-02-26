def main():

    books = []
    choice = 0

    while choice != 4:
        print("Library Manager")
        print("1. Add a book")
        print("2. Find a book")
        print("3. Show all books")
        print("4. Exit")
        choice = int(input())

        if choice == 1:
            print("Adding a book")
            title = input("Enter the book's title: ")
            gender = input("Enter the book's gender: ")
            author = input("Enter the book's author: ")
            books.append([title, gender, author])
        
        elif choice == 2:
            print("Finding a book")
            search_word = input("Enter search word: ")
            for book in books:
                if search_word in book:
                    print(book)

        elif choice == 3:
            print("Showing all books")
            for book in books:
                print(book)

        else:
            choice == 4
            print("Exiting program")

    print("Program terminated")

if __name__ == "__main__":
    main()
    