def daynumtoname(num):
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif  4:
        return "Thursday"
    elif  5:
        return "Friday"
    elif  6:
        return "Saturday"
    else:
        return "Please enter an integer between 0 and 6."
print(daynumtoname(int(input("Please enter an integer between 0 and 6."))))    