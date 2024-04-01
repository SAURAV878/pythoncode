student = {
    'name':'ram',
    'age':20,
    'adress':'bouddha'
}
print(student)

capital = {
    'Nepal':'Kathmandu',
    'India':'New  Dehli',
    'China':'Beijing'
}
print(capital)
print(len(capital))
print(type(capital))
print(capital.keys()) #give the list in the dict

print(capital.values())

print(capital['Nepal'])#gives the value of given key


capital ['Japan'] = 'Tokyo'#adds the value in dict
print(capital)

capital ['Russia'] = 'Moscow'
print(capital)

capital ['Bhutan'] = 'Thimbu'
print(capital)

pop_element = capital.pop('Bhutan')
print(pop_element)
print(capital)

a={1,2,3,4}
b=(1,2,3,4)
#list reaminig part
c=['a','b','c','e','d','f']
print(c.index('a'))#gives the values to index
c.sort()#ascending order
print(c)



marks = {
    'Math':'80',
    'Social':'80',
    'Science':'80'
}
print(marks)
capital.update(marks)#to combine marks and capital
print(capital)

copy_list = capital.copy()
print('This is the copy:', copy_list)
copy_list.clear()
print(copy_list)


