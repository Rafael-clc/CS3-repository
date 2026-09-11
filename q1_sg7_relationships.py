# INFLUENCE
class Vehicle:
    def __init__(self,kindofvehicle):
        self.kindofvehicle = kindofvehicle
        print(self.kindofvehicle,"created")
    def move(self,distance):
        print(self.kindofvehicle,"moved",distance,end="")

class Car(Vehicle):
    def __init__(self,kindofvehicle,brand,model):
        self.brand = brand; self.model = model
        super().__init__(kindofvehicle)
        print("It is a",brand,model)
    def move(sef,distance):
        super().move(distance)
        print("KM")

class Boat(Vehicle):
    def __init__(self,kindofvehicle,model):
        self.model = model
        super().__init__(kindofvehicle)
        print("It is a",self.model)
    def move(self,distance):
        super().move(distance)
        print("Nm")

class Plane(Vehicle):
    def __init__(self,kindofvehicle,model):
        self.model = model
        super().__init__(kindofvehicle)
        print("It is a",self.model)
    def move(self,distance):
        super().move(distance)
        print("Nm")
    

vios = Car("car","Toyota","Vios")
vios.move(10)
ferry = Boat("ferry","SuperFerry")
ferry.move(20)
yacht = Boat("yacht","Subic Yacht")
yacht.move(25)
airplane = Plane("airplane","Philippine Airlines")
airplane.move(50)





# COMPOSITION
class Nucleus:
    def __init__(self):
        print("Nucleus created")
    def __del__(self):
        print("Nucleus is gone")

class Mitochondria:
    def __init__(self):
        print("Mitochondria created")
    def powerTheCell(self):
        print("Mitochondria is providing energy")
    def __del__(self):
        print("Mitochondria is gone")

class Cell:
    def __init__(self):
        print("Cell created")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()
    def exist(self):
        print("Cell is existing")
        self.mitochondria.powerTheCell()
    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell is gone")

cellAtWork = Cell()
cellAtWork.exist()
del cellAtWork






# AGGREGATION
class Sauce:
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste
        print(self.name,"is cooked")
    def __del__(self):
        print(self.name,"is goners")
    def __str__(self):
        return "This is "+self.name+" and it tastes "+self.taste
class Tusoktusok:
    def __init__(self,name,sauce):
        self.name = name
        self.sauce = sauce
        print(self.name,"is cooked and dipped in",self.sauce.name)
    def eat(self):
        print("I am eating",self.name,"and it tastes",self.sauce.taste)
    def __del__(self):
        print(self.name,"was thrown away")

vinegar = Sauce("vinegar","sour")
fishball = Tusoktusok("fishball",vinegar)
fishball.eat()
del fishball
print(vinegar)
