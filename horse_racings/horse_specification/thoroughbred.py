from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 140

    @property
    def training_increment(self):
        return 3

    def train(self):
        if self.speed + self.training_increment > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.training_increment
