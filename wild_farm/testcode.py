from wild_farm.animals.birds import Hen, Owl
from wild_farm.food import Vegetable, Fruit, Meat

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
