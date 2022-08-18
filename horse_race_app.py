from project.core.race_type_factory import HorseTypeFactory
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

        self.horse_type_factory = HorseTypeFactory()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = ["Appaloosa", "Thoroughbred"]
        if horse_type in valid_horse_types:
            if any(horse.name == horse_name for horse in self.horses):
                raise Exception(f"Horse {horse_name} has been already added!")
            horse = self.horse_type_factory.create_horse_type(horse_type, horse_name, horse_speed)

            # if horse is None:
            #     return

            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(jockey.name == jockey_name for jockey in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(race.race_type == race_type for race in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.__find__the_last_added_horse_by_type(horse_type)

        if horse.is_taken or horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if horse and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__find_horse_race_by_type(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey and jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__find_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        jockey_with_fastest_horse = sorted(horse_race.jockeys, key=lambda obj_jockey: - obj_jockey.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {jockey_with_fastest_horse.horse.speed}km/h is " \
               f"{jockey_with_fastest_horse.name}! Winner's horse: {jockey_with_fastest_horse.horse.name}."

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def __find_horse_by_type(self, horse_type):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                return horse

    def __find_horse_race_by_type(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

    def __find__the_last_added_horse_by_type(self, horse_type):
        for horse in list(reversed(self.horses)):
            if horse.__class__.__name__ == horse_type:
                return horse

