def listofEven(inputs):
    evenNumbers=[]
    
    for input in inputs:
        if input%2==0:
            evenNumbers.append(input)
    return evenNumbers

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listofEven(inputs))

        