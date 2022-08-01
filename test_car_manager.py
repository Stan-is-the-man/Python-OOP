class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarTest(TestCase):

    def test_constructor_with_true_inputs_happy_case(self):
        my_car = Car("Honda", "FR-V", 8, 50)
        self.assertEqual("Honda", my_car.make)
        self.assertEqual("FR-V", my_car.model)
        self.assertEqual(8, my_car.fuel_consumption)
        self.assertEqual(50, my_car.fuel_capacity)
        self.assertEqual(0, my_car.fuel_amount)

    def test_constructor_make_no_data_raises_error(self):
        with self.assertRaises(Exception) as ex:
            my_car = Car("", "FR-V", 8, 50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_constructor_model_no_data_raises_error(self):
        with self.assertRaises(Exception) as ex:
            my_car = Car("Honda", "", 8, 50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_constructor_fuel_consumption_raises_error(self):
        with self.assertRaises(Exception) as ex:
            my_car = Car("Honda", "FR-V", 0, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            my_car = Car("Honda", "FR-V", -1, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raises_error(self):
        with self.assertRaises(Exception) as ex:
            my_car = Car("Honda", "FR-V", 8, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            my_car = Car("Honda", "FR-V", 8, -16)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_new_fuel_amount_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            my_car = Car("Honda", "FR-V", 8, 50)
            with self.assertRaises(Exception) as ex:
                my_car._Car__fuel_amount = -1
            self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_not_positive_num_raises_error(self):
        my_car = Car("Honda", "FR-V", 8, 50)
        with self.assertRaises(Exception) as ex:
            my_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        my_car = Car("Honda", "FR-V", 8, 50)
        with self.assertRaises(Exception) as ex:
            my_car.refuel(-7)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_itself(self):
        my_car = Car("Honda", "FR-V", 8, 50)
        my_car.refuel(60)
        self.assertEqual(50, my_car.fuel_amount)

        my_car = Car("Honda", "FR-V", 8, 50)
        my_car.refuel(10)
        self.assertEqual(10, my_car.fuel_amount)

    def test_drive_raises_error(self):
        my_car = Car("Honda", "FR-V", 8, 50)
        my_car.refuel(8)
        with self.assertRaises(Exception) as ex:
            my_car.drive(101)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_itself(self):
        my_car = Car("Honda", "FR-V", 8, 50)
        my_car.refuel(8)
        my_car.drive(100)
        self.assertEqual(0, my_car.fuel_amount)


if __name__ == "__main__":
    main()
