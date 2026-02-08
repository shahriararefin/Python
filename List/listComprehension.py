numbers = [ 23, 45, 67, 89, 12, 52, 34, 78, 90, 11 ]

# squared_numbers = [ num ** 2 for num in numbers ]
# print(squared_numbers)

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
        
    else:
        print(num, "is odd")    