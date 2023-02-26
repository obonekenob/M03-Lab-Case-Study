# new m03

class Vehicle:

    def __init__(self, vtyp, year, make, model, num_doors, roof_type):
        self.vtyp = vtyp

    def transport(self):
        print(f"Vehicle type: {self.vtyp}")

    def print_all_auto_input(self):
         everything = f"Year: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.num_doors}\nType of roof: {self.roof_type}"
         return everything.title()

class Automobile(Vehicle):
    
    def __init__(self, vtyp, year, make, model, num_doors, roof_type):
        self.year = year
        self.make = make
        self.model = model
        self.num_doors  = num_doors
        self.roof_type = roof_type
        super().__init__(vtyp, year, make, model, num_doors, roof_type)

my_type = str(input("Please enter the vehicle type: "))
my_year = str(input("Please enter a vehicle year: "))
my_make = str(input("Please enter a vehicle make: "))
my_model = str(input("Please enter a vehicle model: "))

door_cntr = 'Y'
while (door_cntr == 'Y'):
    my_num_doors = int(input("Please enter the number of doors in the vehicle (Must be 2 or 4): "))
    if ((my_num_doors == 2) or (my_num_doors == 4)):
        door_cntr = 'N'

roof_cntr = 'Y'
while (roof_cntr == 'Y'):
    my_roof_type = str(input("Please enter the vehicle roof type (Must be solid or sun roof): "))
    if ((my_roof_type == 'solid') or (my_roof_type == 'sun roof')):
        roof_cntr = 'N'

my_vehicle = Vehicle(my_type, my_year, my_make, my_model, my_num_doors, my_roof_type)
my_Automobile = Automobile(my_type, my_year, my_make, my_model, my_num_doors, my_roof_type)

my_vehicle.transport()
print(my_Automobile.print_all_auto_input())

