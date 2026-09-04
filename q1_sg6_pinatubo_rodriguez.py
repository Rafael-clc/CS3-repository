class Lab:
    def __init__(self, room_number: str):
        self.room_number = room_number

class Technician:
    def __init__(self, name: str):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj: Lab):
        self.assigned_lab = lab_obj

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)

print(f"Technician: {mr_cruz.name}")
print(f"Assigned Room Number: {mr_cruz.assigned_lab.room_number}")