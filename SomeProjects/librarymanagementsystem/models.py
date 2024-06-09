class Student:

    # student fields
    __name = None
    __address = None
    __phonenumber = None

    # constructor
    def __init__(self, name, address, phonenumber):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber

    # getter function for name
    @property
    def name(self):
        return self.__name
    
    # setter function for name
    @name.setter
    def name(self, name):
        self.__name = name

    # getter function for address
    @property
    def address(self):
        return self.__address
    
    # setter function for address
    @address.setter
    def address(self, address):
        self.__address = address

    # getter function for phonenumber
    @property
    def phonenumber(self):
        return self.__phonenumber
    
    # setter function for phonenumber
    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

# Creating an instance of Student
# student = Student("Sukhuti", "Trijuga", 10)
# print(student.phonenumber)  

class Book:

    # book fields
    __name1 = None
    __description = None
    __author = None
    __stock = None

    # constructor
    def __init__(self,name1,description,author,stock):
        self.__name1 = name1
        self.__description = description
        self.__author = author
        self.__stock = stock

    # getter function for name
    @property
    def name(self):
        return self.__name1
    
    # setter function for name
    @name.setter
    def name(self,name):
        self.__name = name
    
    # getter function for description
    @property
    def description(self):
        return self.__description
    
    # setter function for description
    @description.setter
    def description(self,description):
        self.__description = description
    
    # getter function for author
    @property
    def author(self):
        return self.__author
    
    # setter function for author
    @author.setter
    def author(self,author):
        self.__author = author

    # getter function for stock
    @property
    def stock(self):
        return self.__stock
    
    # setter function for stock
    @stock.setter
    def stock(self,stock):
        self.__stock = stock  


class Borrower(Student,Book):
    def __init__(self,name, address, phonenumber,name1,description,author,stock):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber
        self.__name1 = name1
        self.__description = description
        self.__author = author
        self.__stock = stock
        Student.__init__(self, name, address, phonenumber)
        Book.__init__(self,name1,description,author,stock)
