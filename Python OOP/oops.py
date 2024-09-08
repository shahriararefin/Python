# class Car:
#     brand = "Toyota"
#     color = 'white'
#     print("okokkoko")

# c1 = Car()
# # print(c1.brand)




class Student:
    # default constructor
    def __init__(self):
        pass
    # parametarized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(self)
    
    def hello(self):
        print("hello", s1.name)
    
    def getMarks(self):
        return self.marks

s1= Student("karan", 99)
print(s1.name, s1.marks)

s2 = Student("K", 70)
print(s2.name, s2.marks)

s1.hello()
print(s1.getMarks())