fruits =  ['apple', 'orange', 'mango', 'papaya']#for loop - iteration over sequence
for i in fruits:
    print(i)
for i in range(5):
    print(i)
for i in range(1, 20 , 3):
    print(i)

for i in range(1,11):
    if(i%2 ==0):
        print("the given number is even")
    else:
        print("the given number is odd")
    print(i)


for i in range(1,11):
    # if i ==5:
    #     break
    # print(i)

    # if i == 5:
    #     continue
    # print(i)

  #  if i == 5:
   #     pass
 #   print(i)
 i=1
while i<=10:
    print("multiplication table:",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
        i+=1
