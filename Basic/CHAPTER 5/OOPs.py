# class define
class Student:
    name = "john";
    age = 20;
    def __init__(self,name,age): # "__init__" this think call the 
        print(self.name, name);
        self.name = name;
        self.age = age;
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
a = Student("Raj",23);
a.display();
