# -------------------------------
# OOP Concepts in Python Example
# -------------------------------

# CLASS and ENCAPSULATION (Data Hiding)
class Person:
    def __init__(self, name, age):
        # Public attribute
        self.name = name
        
        # Private attribute (data hiding using __)
        self.__age = age  

    # Public method to access private data (Getter)
    def get_age(self):
        return self.__age

    # Public method to modify private data (Setter)
    def set_age(self, age):
        if age > 0:
            self.__age = age

    # Method (can be overridden -> polymorphism)
    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")


# INHERITANCE (Student inherits Person)
class Student(Person):
    def __init__(self, name, age, roll_no):
        # Call parent constructor
        super().__init__(name, age)
        self.roll_no = roll_no

    # POLYMORPHISM (method overriding)
    def display(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}, Age: {self.get_age()}")


# Another child class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # POLYMORPHISM (method overriding)
    def display(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}, Age: {self.get_age()}")


# -------------------------------
# OBJECTS and INSTANCES
# -------------------------------

# Creating objects (instances)
p1 = Person("Ram", 30)
s1 = Student("Hari", 20, 101)
t1 = Teacher("Sita", 40, "Math")

# Calling methods
p1.display()   # Person object
s1.display()   # Student object (overridden method)
t1.display()   # Teacher object (overridden method)

# Accessing private data using getter
print("Access Age using getter:", p1.get_age())

# Modifying private data using setter
p1.set_age(35)
print("Updated Age:", p1.get_age())