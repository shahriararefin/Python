class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")
    
    def getAvg(self):
        sum = 0
        for val in self.marks:
            sum+= val
        print("hi", self.name, "avg score: ", sum/3)

s1 = Student("tony", [89, 98, 78])
s1.getAvg()
            