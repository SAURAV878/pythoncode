user = input("Enter Youre UserName: ")

if user == "admin":
    print("You're Logging In")
    attendence = input("Enter your attendence: ")
    if attendence == "Full":
        print("Staff Attendce Is Full")
    elif attendence == "Half":
        print("Staff Attendce Is Half")
    elif attendence == "Morning":
        print("Staff Attendnce Is Morning")
    else:
        print("Staff Is Absent")    
else:
    print("You Can't Login In")    