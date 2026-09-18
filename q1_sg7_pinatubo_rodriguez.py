class Glassware:
    def __init__(self, material="Glass"):
        self.material = material


class Beaker(Glassware):
    def __init__(self, capacity, material="Glass"):
        super().__init__(material)
        self.capacity = capacity
    def __str__(self):
        return f"{self.capacity}ml Beaker ({self.material})"

class Tray:
    def __init__(self):
        self.beakers = [Beaker(capacity=175) for i in range(5)]
    def display(self):
        print(f"Tray contains {len(self.beakers)} beakers:")
        for index, beaker in enumerate(self.beakers, start=1):
            print(f"{index}.{beaker}")

my_tray = Tray()
my_tray.display()
del my_tray
