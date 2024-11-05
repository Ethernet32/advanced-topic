#compisition is a clas that exists inside of another class (class has a other class)

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque
    def ignite(self):
        print("vroom Vroom")


myEngine = Engine("V8", 5.8, 236, 344)
myCar = Car("Mazda", "Mazda3", 2013, myEngine)

#to access a composit class you must access where it is saved within the class
print(myCar)
myCar.engine.ignite()