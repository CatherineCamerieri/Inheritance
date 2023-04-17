
class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
    
    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Telephone Number:", self.__phone)


class Customer(Person):

    def __init__(self, name, address, phone, number, mail):

        Person.__init__(self, name, address, phone)

        self.__number = number
        self.__mail = mail

    def get_number(self):
        return self.__number
    
    def get_mail(self):
        return self.__mail


    def print_person(self):
        Person.print_person(self)
        print("Customer Number:", self.__number)
        if self.__mail:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")
