from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    capacity: float
    horse_power: float

    def __init__(self, fuel: float, horse_power: float):
        self.fuel = fuel
        self.capacity = self.fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if self.fuel < fuel_needed:
            raise Exception("Not enough fuel")
        self.fuel -= fuel_needed

    def refuel(self, fuel):
        if self.fuel + fuel > self.capacity:
            raise Exception("Too much fuel")
        self.fuel += fuel

    def __str__(self):
        return f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"


from unittest import TestCase, main


class TestVehicle(TestCase):
    def test_constructor(self):
        vehicle = Vehicle(50.0, 139.0)
        self.assertEqual(50.0, vehicle.fuel)
        self.assertEqual(139.0, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_raise_error_not_enough_fuel(self):
        vehicle = Vehicle(50.0, 139.0)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        vehicle = Vehicle(52.5, 139.0)
        vehicle.drive(10)
        self.assertEqual(40, vehicle.fuel)

    def test_refuel_raises_error_too_much_fuel(self):
        vehicle = Vehicle(52.5, 140.0)
        vehicle.drive(10)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(13)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_fule(self):
        vehicle = Vehicle(52.5, 140.0)
        vehicle.drive(10)
        vehicle.refuel(12.5)
        self.assertEqual(52.5, vehicle.fuel)

    def test_str(self):
        vehicle = Vehicle(52.5, 139.0)
        result = "The vehicle has 139.0 " \
                 "horse power with 52.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, vehicle.__str__())


if __name__ == "__main__":
    main()
