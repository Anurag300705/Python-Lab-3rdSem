# Base class
class Vehicle:
    def start(self):
        print("Starting vehicle")

# Derived class
class Car(Vehicle):
    # Overriding the start() method
    def start(self):
        print("Starting car")

# Instantiate both classes
vehicle = Vehicle()
car = Car()

# Call the start() method to demonstrate method overriding
vehicle.start()  # Calls the start() method from Vehicle class
car.start()      # Calls the overridden start() method from Car class
