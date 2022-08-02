from unittest import TestCase, main
from project.vehicle import Vehicle


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
