x=int(input("Enter the value of program: "))

if x % 3 ==0 and x % 5 ==0:
    print("Fizzbuzz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 == 0:
    print("Fizz")
else:
    print(x)    
 