class Vechile:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details: ', self.name,self.color,self.price)

    def max_speed(self):
        print("Vechile max speed is 150")

    def change_gear(slef):
        print("Vechile cahge 6 gear")


class Car(Vechile):
    def max_speed(self):
        print('Car max speed is 240') 

    def change_gear(self):
        print('Car max speed is 240')

car = Car('Car x1','red',20000)

car.show()
car.max_speed()
car.change_gear()





                                