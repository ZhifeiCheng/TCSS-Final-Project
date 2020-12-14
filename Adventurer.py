import random


class Adventurer:
    def __init__(self, name):
        self.__name = name
        self.__hit_points = random.randint(75, 100)
        self.__healing_potion = 0
        self.__vision_potion = 0
        self.__pillar_collected = []

    @property
    def hit_points(self):
        return self.__hit_points

    @hit_points.setter
    def hit_points(self, point_change: int):
        self.__hit_points = point_change

    @property
    def healing_potion_count(self):
        return self.__healing_potion

    @healing_potion_count.setter
    def healing_potion_count(self, healing_potion: int):
        self.__healing_potion = healing_potion

    @property
    def vision_potion_count(self):
        return self.__vision_potion

    @vision_potion_count.setter
    def vision_potion_count(self, vision_potion: int):
        self.__vision_potion = vision_potion

    @property
    def pillar_collected(self):
        return self.__pillar_collected

    def __str__(self):
        return f'Name {self.__name}, \nTotal Hit Points = {self.__hit_points}, \nTotal Healing Potion = ' \
               f'{self.__healing_potion}, \nTotal Vision Potion' \
               f' = {self.__vision_potion}, \nList of Pillars Pieces Found = {self.__pillar_collected}'


if __name__ == "__main__":
    adv = Adventurer("tututu")
    print(adv)


