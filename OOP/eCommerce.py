class Products:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def isInStock(self):
        return self.stock > 0
    
    def reduceStock(self, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero")
            return False
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Stock reduced by {quantity}. New stock: {self.stock}")
            return True
        else:
            print("Not available")
            return False
    
    def displayDetails(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock}")
    
if __name__ == "__main__":
    
    product = Products("Laptop", 999.99, 10)
    product.displayDetails()

    
    print(f"Is the product in stock? {product.isInStock()}")  
    print("\nPlacing an order for 3 laptops...")
    product.reduceStock(3)
    
    product.displayDetails()

    
    print("\nPlacing an order for 8 laptops...")
    product.reduceStock(8) 