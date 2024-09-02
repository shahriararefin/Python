tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

search = int(input("Search Element: "))
index = 0
for el in tuple:
    if(search==el):
        print("Found at index: ", index)
        break
    
    else:
        print("Finding..")
    index+=1