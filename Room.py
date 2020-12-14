class Room:
    def __init__(self, room_content=None):
        self.__point = 0
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

    @property
    def is_visited(self):
        return self.__visited

    @is_visited.setter
    def is_visited(self, is_visited: bool):
        self.__visited = is_visited

    @property
    def room_point(self):
        """
        getter method that allows other classes retrieve the rooms points
        """
        return self.__point

    @room_point.setter
    def room_point(self, point):
        """
        setter method that allows other classes change the rooms points with "health
        potion or pits
        """
        self.__point = point


if __name__ == "__main__":
    room = Room("E")
    print(room)
