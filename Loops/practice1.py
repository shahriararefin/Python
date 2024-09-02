num = int(input("Enter a number: "))
i = 1
sum=0
calc = 0
while i<=num:
    sum+=i
    i+=1
print(sum)


for i in range(1, num+1):
    calc+=i
    
print(calc)