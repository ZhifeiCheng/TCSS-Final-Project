class Room:

    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = "No pillar"
        self.__pit = False
        self.__entrance = False
        self.__exit = False
        self.__impassable = False
        self.__visited = False
        self.__healthChance = 10
        self.__door_N = ""
        self.__door_S = ""
        self.__door_E = ""
        self.__door_W = ""
        self.__pillar_A = ""
        self.__pillar_E = ""
        self.__pillar_I = ""
        self.__pillar_P = ""

    def __str__(self):
        item_count = 0
        if self.__healthPotion:
            item_count += 1
        if self.__visionPotion:
            item_count += 1

        if item_count > 1:
            return "M"

        # return "Health potion: " + str(self.__healthPotion) + "\n" \
        #        + "Vision potion: " + str(self.__visionPotion) + "\n" \
        #        + "Pillar: " + str(self.__pillar) + "\n" \
        #        + "Pit: " + str(self.__pit) + "\n" \
        #        + "Exit: " + str(self.__exit) + "\n\n"

        return print(str(self.__door_N) + '\n'
                     + str(self.__door_W)
                     + str(self.__pillar_P)
                     + str(self.__door_E)
                     + '\n' +str(self.__door_S))

    def get_health_chance(self):
        return self.__healthChance

    def set_entrance(self):
        self.__entrance = True

    def set_exit(self):
        self.__exit = True

    def set_pit(self):
        self.__impassable = True

    def set_door_N(self):
        self.__door_N = "*-*"

    def set_door_S(self):
        self.__door_S = "*-*"

    def set_door_E(self):
        self.__door_E = "|"

    def set_door_W(self):
        self.__door_W = "|"

    def set_pillar_A(self):
        self.__pillar_A = "A"

    def set_pillar_E(self):
        self.__pillar_E = "E"

    def set_pillar_I(self):
        self.__pillar_I = "I"

    def set_pillar_P(self):
        self.__pillar_P = "P"

    def set_health(self, add_potion):
        self.__healthPotion = add_potion

    def set_visited(self, visited):
        self.__visited = visited

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

