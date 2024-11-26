def ageCalc( name, age):
    name = name
    ageNew = age+10
    print("Name: {name}")
    print(f"Age after 10 years: ", ageNew)
    
    
    
    

name = input("Please enter name: ")
ageToday = int(input("Please enter Today age: "))

if ageToday > 0:
    ageCalc(name,ageToday)
else:
    print("Let it born first")