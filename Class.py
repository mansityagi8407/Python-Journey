class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
            print("Name:", self.name)
            print("Age:", self.age)

s1 = student("Annu",18)
s2 = student("Mansi",18)
s1.display()
s2.display()
