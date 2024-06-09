from models import *
from editexcel import *
if __name__ == '__main__':
    print("Enter 1. Add student \n Enter 2. Add book \n Enter 3. Edit Student \n Enter 4. Delete Stduent")
    choice = int(input("Enter your below choice"))

    if choice == 1:
        name = input("Enter the name")
        addres = input("Enter the address")
        phonenumber = input("Enter the phone number")
        student = Student(name, addres, phonenumber)
        print("Students have been added successfully")
        # here I will write code for searching that data so that the user will be able to add phonenumber
        addstudent(student.name,student.address,student.phonenumber)

    elif choice == 2:
        name = input("Enter the book name")
        description = input("Enter the book desciption")
        author = input("Enter the author name")
        stock = int(input("Enter the stock"))
        book = Book(name,description,author,stock)
        # here this code will add the book
        addbook(book.name,book.description,book.author,book.stock)
    else:
        print("please enter a valid option")
