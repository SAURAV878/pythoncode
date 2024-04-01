#dict 
dictionary = {}

dictionary['name']='Ram'
dictionary['age']=22
dictionary['subject']=['math','science','social','nepali']
dictionary['education'] = {
    'school': {
    'name':'xavier school',
    'adress':'boudha,tusal'
 },
'high school':{'name':'penatgon college',
               'adress':'tinkune,sinamngal'},
'bachleor level':{
    'name':'xavier college',
    'adress':'boudha,kathmandu'
}               
}
print(dictionary)

# for i in dictionary.keys():
#     print(i)

# for i in dictionary['subject']:
#     print(i)

#acessing elemnt of nested dict from for loop
for i, j in dictionary['education']['school'].items():
    print(i, "=", j)    

#dict = {key:{nestkey:{subnested:value}}


print(dictionary['education']['school']['adress'])

