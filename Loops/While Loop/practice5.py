
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

search = int(input("Enter the item to search: "))
index = 0

   

while index< len(tuple):
    if(search==tuple[index]):
        print("Found at index: ", index)
        break
    else:
        print("Finding..")  
    index+=1
     
