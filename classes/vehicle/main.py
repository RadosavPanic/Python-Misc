from vehicle import *

volvo = Truck("GR", "Greece", 2500, 1000)
scania = Truck("NL", "Netherlands", 4000, 1250)

mercedes = Car("D", "Germany", 1550, 5, 4)
nissan = Car("CH", "Switzerland", 2100, 3, 4)

isuzu = Bus("J", "Japan", 3300, 50, "Diesel")
iris = Bus("H", "Hungary", 4500, 41, "Diesel")

# Comparison defined in __gt__ -> truck-weight, car-num_doors, bus-num_seats
print(f"Weight Volvo > Scania: {volvo > scania}")
print(f"Number of doors Mercedes > Nissan: {mercedes > nissan}")
print(f"Number of seats Isuzu > Iris: {isuzu > iris}")

# Printing the winners
print(scania)
print(mercedes)
print(isuzu)
