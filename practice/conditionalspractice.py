mybool = True
age = int(input("what's age"))

if age < 4:
    print("preschool")
elif age >= 4 and age < 10:
    print("lower school")
elif  age >= 10 and age < 18:
    print("upper school")
    if age < 13:
        print("middle school")
    else:
        print("high school")
else:
    print("you're too old for school")
    


print("do this whatever")