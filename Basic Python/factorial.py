num = int(input("enter a number: "))
fact = 1
if num>0:
    for i in range(1, num+1):
        fact = fact*i
        print(fact)
else:
    print("Invalid value")


