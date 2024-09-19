class Person ():
    def __init__ (self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def introduce_self(self):
        print(f"my name is{self.name}and I am {self.age}years old")

p1 = Person()
p1=('joy',18,'female')
p1.introduce_self