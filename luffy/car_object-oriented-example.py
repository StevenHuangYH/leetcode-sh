class Car:


    def __init__(self, make, model, year, color): #object constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving.")
        print(f"This {self.model} is driving")
        print("This" + " " + self.model + " is driving")
    

    def stop(self):
        print("This car is stopped.")
