import os, shutil
# # file handling =  open file, close file, read file, write and maintain file.
# my_file = open("text.txt")
# print(my_file)
# print(my_file.read())
# print(my_file.writable())# to check wheter to write in file or not.
# (my_file.close())

# my_another_file = open("text.txt", "r+")#to read and write
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write('ram \n')


# my_another_file = open("text.txt", "w+")#overwrite
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write('ram')
# print(my_another_file.seek(0))#indexing garerwa ka dekhi padne januxaa
# print(my_another_file.read())


# my_next_file = open('next.txt', 'a+') #
# print(my_next_file.writable())
# print(my_next_file.readable())
# print(my_next_file.write("hello world"))
# print(my_next_file.seek(0))
# print(my_next_file.read())

# list1 = ['Ram\n', 'Sita\n', 'Hari']
# print(my_next_file.writelines(list1))


my_next_file = open('next.txt', 'a+') 
print(my_next_file.writable())
print(my_next_file.readable())
print(my_next_file.write("hello world"))
print(my_next_file.seek(0))
print(my_next_file.read())

list1 = ['Ram\n', 'Sita\n', 'Hari']
print(my_next_file.writelines(list1))
print(my_next_file.seek(0))
print(my_next_file.readline())# auta matrwa dinxa
print(my_next_file.readlines())# list ma dinxa

shutil.copy('next.txt', 'next1.txt')
os.remove('next1.txt')

shutil.move('text.')


