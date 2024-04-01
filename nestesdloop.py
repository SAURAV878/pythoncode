# color = ['red', 'white', 'purple', 'orange']
# fruits = ['apple', 'mango', 'grapes', 'litchi']

# for x in color:
#     for y in fruits:
#         print(x,y,end=" ")

# # nested loop is loop insdide loop
# for i in range(1,11):
#     print("Mulitiplaction table: ",i)
#     for j in range(1,11):
#         print(i, "*", j , "=", i*j,end=" ")

# x = 0
# while x<=10:
#     j=0
#     while j<=10:
#         print(x, "*", j, "=", x*j)
#         j+=1
#         x+=1

#while loop inside for loop
for i in range(1,11):
    print("Multpilacton: ",i)
    x=1
    while x<=10:
        print(x,"*",i,"=",i*x)
        x+=1


