class Vehicle:
    def Vehicle_info(self):
        return 'Inside Vehicle class'

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()

# Access Vehicle's info using car object
print(car.Vehicle_info())  # Output: Inside Vehicle class
car.car_info()      # Output: Inside Car class
