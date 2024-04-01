#exception = an event that ocuurs to distrupt the normal flow of operation
# try:
#     age=int(input())
#     print(age)
# except:
#     print('please provide numberic')

# print('xavier college')        


# try:
#     a = int(input("Enetr a value"))
#     b = int(input("enetr your valu"))
#     c= a/b
# except ValueError:
#     print('please provide numeric values')    
# except ZeroDivisionError:
#     print("Zero is not divided by any number")
# else:
#     print("the value in c : ", c)

def login():
    user1 = 'admin'
    pass1 = 'admin'
    try:
        username = input()
        password = input()

        if user1 != username:
            raise ZeroDivisionError
        elif pass1 != password:
            raise ValueError
    except ZeroDivisionError:
        print('user name is invalid')
        login()
    except ValueError:
        print('password is invalid')
        login()
    else:
        print("login succesfully")
    finally:
        print("Home")
login()        




