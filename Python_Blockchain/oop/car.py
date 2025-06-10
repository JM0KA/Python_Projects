from vehicle import Vehicle

class Car(Vehicle):
    def brag(self):
        print('Look how cool my car is!')


car1 = Car()
car1.drive()

# Car.top_speed = 200
car1.add_warning('this is a harmless warning')

# print(car1.__dict__)
# __dict__ is used to return a dictionary of the entire object
print(car1)

car2 = Car(200)
car2.drive()
car2.add_warning('The fender has fallen off')
car2.add_warning('There is no gas')
print(car2)

car3 = Car(250)
car3.drive()

