# #function is a block of code. we used functoin to reuse the code 
# # two type of function
# #1.bulit in function
# #2.user defined function


# # def function_name():
# #     function body

# #  function_name()  

# #simple program in user defined function
# def function_code():
#     print("hello world")
# function_code()

# #position arugments- take value according to proper positional order. 
# def hello(name, course_name):#parametres
#     print("hello", name, "welcomme to web")
#     print(course_name)

# #keywords arguments- take value according to key.
# hello(course_name='python with django',name='ram')# arguments

# #default arguments-kei xna bane default value linxa
# def hello(name, course_name):#parametres
#     print("hello", name, "welcomme to web")
#     print(course_name)

# hello(name='saurav', course_name='python with data science')    



# # arbitary arguments and it is denoted by *
# def sum(*args):#multiple value assgin garnu ko lagi
#     total= 0
#     for n in args:
#         total+=n
#     return total #return gives of function and stop the excutuion of function4

# result = sum(2,3,9,8)
# print(result)    

# #Artibatry keywords - **kwargs which contain data in key value:value pairs
# def hello(**kwargs):
#     print("hello", kwargs['name'],"welcome to web tranning")
#     print(kwargs['course_name'])
          
# hello(name='ram', course_name='python with django')   
 


# # SCOPE OF A VARIABLE

l = float(input('Enter a length : '))
b = float(input('Enter a breadth : '))
#global variable = which can be accesible from any place

def area():
    # local variable = this is defined inside the function and cannot be accesbile from outside the function.its scope is only around the declared function.
    area_of_object = l*b
    return area_of_object
def volume():
    h = float(input("Enter your height: "))
    v = l*b*h
    return v


result = area()
print(result)
result_volume = volume()
print(result_volume)


# #lambda function: the function without name. it is used for instant use and its one-time uses. lambda keyword is used
# x = lambda a,b :a*b
# area = x(2,3)
# print(area)


# #Recursion function = function calling iself again and again
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# result = factorial(4)
# print(result)          



#filter()
#map()