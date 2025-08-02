class Employee:
    name = "raj";
    age = 20;
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Programmer(Employee):
    name = "suresh";

a = Programmer();
a.display()