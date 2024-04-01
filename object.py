# #OOP in pyhton (object orinted program).We deal with real time object and entites

# class Room(): # blueprint of object.Capital letter should be frist in value
#     l = int(input("Enter a length: "))
#     w = int(input("Enter a width: "))
#     h = int(input("Enetr a height: "))


#     def area(self):#attributes  pass garna mildina
#         print("Area of room is: ", self.l*self.w)


#     def volume(self):
#         print("Area of height: ",self.l*self.w*self.h)
# area_of_room = Room()
# print(area_of_room.area())

# area_of_volume = Room()
# print(area_of_volume.volume())

class Calculator:


    def _init_(self, num1, num2):#afai call hunxa
        self.num1 = num1
        self.num2 = num2

    def add(self,*args):
        self.num1 = args[1]
        total = 0
        for n in args:
            total += n
        return total
    
    def sub(self,*args):
        total = 0
        for n in args:
            total -= n
        return total

    def add(self,*args, **kwargs):
        total = args[0]
        for n in args[1: ]:
            total += n
        return total

    def sub(self,*args, **kwargs):
        total = args[0]
        for n in args[1: ]:
            total -= n

    def multiply(self,num1,num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print("Error: Divison by Zero!")         
    
cal = Calculator()
print(cal.add(2,3,4,5))
print(cal.sub(2,3,4,5))
