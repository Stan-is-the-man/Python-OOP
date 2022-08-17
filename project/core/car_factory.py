from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    types = {"SportsCar":SportsCar, "MuscleCar": MuscleCar}

    def create_car(self, car_type: str, model: str, speed_limit: int):
        return self.types[car_type](model, speed_limit)