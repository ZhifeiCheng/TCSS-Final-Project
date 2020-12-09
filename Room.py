import random


class Room:
    def __init__(self, room_content=None):
        self.__potion = 0
        self.__vision_potion = None
        self.__visited = False
        self.__room_content = room_content  # vision potion, health potion, pit, M
        self.__room_matrix = [['*', "*", "*"], ['*', "*", "*"], ['*', "*", "*"]]  # room template

    @property
    def room_content(self):
        return self.__room_content

    @room_content.setter
    def room_content(self, room_content: str):
        """
        Assign content such as health potion, pit and etc to the room
        """
        self.__room_content = room_content
        self.__room_matrix[1][1] = room_content

    @property
    def room_matrix(self):
        return self.__room_matrix

    @room_matrix.setter
    def room_matrix(self, *room_matrix: str):
        """
        Assign content such as health potion, pit and etc to the room
        """
        self.__room_matrix = room_matrix

    @property
    def vision_potion_rooms(self):
        return self.__vision_potion

    @vision_potion_rooms.setter
    def vision_potion_rooms(self, rooms):
        self.__vision_potion = rooms

    def __str__(self):
        res = ""
        for row in self.__room_matrix:
            res += " ".join(row) + "\n"
        return res

    def room_message(self):
        print(f"You have entered the room with {self.__room_content} and {self.__potion}")

    def is_visited(self):
        return self.__visited is True

    def add_potion(self):
        add_potion = random.randint(5, 15)
        self.__potion = self.__potion + add_potion
        print(f"The room has lost {add_potion} potion")

    def add_pit(self):
        lose_potion = random.randint(1, 20)
        self.__potion = self.__potion - lose_potion
        print(f"The room has lost {lose_potion} potion")

    def potion_change(self):
        pass

    def vision_potion(self):
        pass

if __name__ == "__main__":
    room = Room("E")
    print(room)