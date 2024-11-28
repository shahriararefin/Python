def findLargest_and_Smallest(num):
    if not num:
        return None, None
    
    smallest = min(num)
    largest = max(num)
    
    return smallest, largest

num = [12, 41, 53, 42, 45, 5 , 54, 31, 35, 22, 9, 4, 26]

smallest, largest = findLargest_and_Smallest(num)

print(smallest,"is smallest") 
print(largest,"is largest") 
    