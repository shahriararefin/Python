numbers= [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.remove(3)
print(numbers)  

if 5 in numbers:
    numbers.remove(5)


print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)