age = int(input("What is your age?"))
if age < 4:
    print("Not in")
elif age >= 4 and age < 5:
    print("Preschool")
elif age >= 5 and age < 10:
    print("Lower")
elif age >= 10 and age < 13:
    print("Middle")
elif age >= 13 and age < 18:
    print("High")
elif age > 18:
    print("Not in school")
print("School")