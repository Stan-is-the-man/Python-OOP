from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

        self.car_factory = CarFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(car.model == model for car in self.cars):
            raise Exception(f"Car {model} is already created!")
        car = self.car_factory.create_car(car_type, model, speed_limit)

        # The valid car types are "MuscleCar" and "SportsCar". In any other case, ignore the command.
        if car is None:
            return
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(driver.name == driver_name for driver in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(race.name == race_name for race in self.races):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        car = self.__find_last_free_car_by_type(car_type)
        if driver.car:
            old_car = driver.car.model
            driver.car.is_taken = False  # old car set to NOT taken
            driver.car = car  # change the car with new one
            car.is_taken = True  # new car set to taken
            return f"Driver {driver_name} changed his car from {old_car} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_3_drivers = sorted(race.drivers, key=lambda obj_driver: -obj_driver.car.speed_limit)[:3]
        message_result = ""
        for driver in fastest_3_drivers:
            driver.number_of_wins += 1
            message_result += f"Driver {driver.name} wins the {race_name}" + \
                              f" race with a speed of {driver.car.speed_limit}.\n"
        return message_result.strip()

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f'Driver {driver_name} could not be found!')

    def __find_last_free_car_by_type(self, car_type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]

            if not car.is_taken and car.__class__.__name__ == car_type:
                return car
        raise Exception(f'Car {car_type} could not be found!')

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")
