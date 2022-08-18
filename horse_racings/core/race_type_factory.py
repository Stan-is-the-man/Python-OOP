from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseTypeFactory:
    types = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def create_horse_type(self, horse_type: str, horse_name: str, horse_speed: int):
        return self.types[horse_type](horse_name, horse_speed)
