from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    #another varian at the botttom
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 120

    @property
    def training_increment(self):
        return 2

    def train(self):
        if self.speed + self.training_increment > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.training_increment

    # class Appaloosa(Horse):
    #     MAX_SPEED = 120
    #
    #     def __init__(self, name: str, speed: int):
    #         super().__init__(name, speed)
    #
    #     def train(self):
    #         try:
    #             self.speed += 2
    #         except ValueError:
    #             self.speed =  self.MAX_SPEED
