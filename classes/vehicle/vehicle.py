class Vehicle:
    def __init__(self, registration_mark, country, price):
        self.registration_mark = registration_mark
        self.country = country
        self.price = price


class Car(Vehicle):
    def __init__(self, registration_mark, country, price, num_doors, num_seats):
        super().__init__(registration_mark, country, price)
        self.num_doors = num_doors
        self.num_seats = num_seats

    def __gt__(self, other):
        return self.num_doors > other.num_doors

    def __str__(self):
        return (f"Registration mark: {self.registration_mark}, country: {self.country}, price: {self.price}, "
                f"number of doors: {self.num_doors}, number of seats: {self.num_seats}")


class Truck(Vehicle):
    def __init__(self, registration_mark, country, price, max_weight):
        super().__init__(registration_mark, country, price)
        self.max_weight = max_weight

    def __gt__(self, other):
        return self.max_weight > other.max_weight

    def __str__(self):
        return (f"Registration mark: {self.registration_mark}, country: {self.country}, price: {self.price}, "
                f"max weight: {self.max_weight}")


class Bus(Vehicle):
    def __init__(self, registration_mark, country, price, num_seats, fuel_type):
        super().__init__(registration_mark, country, price)
        self.num_seats = num_seats
        self.fuel_type = fuel_type

    def __gt__(self, other):
        return self.num_seats > other.num_seats

    def __str__(self):
        return (f"Registration mark: {self.registration_mark}, country: {self.country}, price: {self.price}, "
                f"number of seats: {self.num_seats}, type of fuel: {self.fuel_type}")
