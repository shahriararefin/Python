class Car:
    def __init__(self) -> None:
        self.acc = False
        self.brk = True
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.brk = False
        self.acc = True
        print("Car started...")
    
c1= Car()
c1.start()
    