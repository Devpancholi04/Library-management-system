class library:
    def add_books(self):
        book = input("enter the name of books : ")
        with open("D:/programming/project/library.txt", "a") as f:
            f.write(book + '\n')
        
    def count_books(self):
        count = 0
        with open("D:/programming/project/library.txt","r") as f:
            for line in f:
                count += 1
        print(f"the library has {count} books")
    
    def print_books(self):
        with open("D:/programming/project/library.txt", "r") as f:
            print("the books available are : ")
            print(f.read())

    def show_all_info(self):
                self.count_books()
                self.print_books()

a = library()
#a.show_all_info()
while True:
    option = int(input('''enter your choice :  
                        press__(1) for add books : 
                        press__(2) for count books : 
                        press__(3) for show availabe books : 
                        press__(4) for show available books and total books : 
                        press__(5) for exit
                        : '''))
    
    if(option == 1):
        a.add_books()
    elif(option == 2):
        a.count_books()
    elif(option == 3):
        a.print_books()
    elif(option  == 4):
        a.show_all_info()
    elif(option == 5):
        exit()
    else:
        print("invalid input!!")
