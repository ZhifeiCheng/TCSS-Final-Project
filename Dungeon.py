import math
import random
from RoomFactory import RoomFactory


class Dungeon:
    def __init__(self, column_count, row_count):
        self.__column_count = column_count
        self.__row_count = row_count
        self.__room_list = []
        self.__room_content = {"M": 0.05, "P": 0.1, "X": 0.1, "V": 0.1, "H": 0.2}  # dict of each room content & ratio
        self.__room_content_count = None   # number count of each room content
        self.__vision_rooms = []

    @property
    def room_content(self):
        return self.__room_content.keys()

    def entrance_exit_generator(self):
        """
        Generate the 2d coordinate pair for the entrance by randomly pick one coordinate along the perimeter.

        """
        entrance_x = random.choice([0, self.__row_count - 1])
        entrance_y = random.choice([0, self.__column_count - 1])
        entrance_location = random.choice([[entrance_x, random.randint(0, self.__column_count - 1)],
                                           [random.randint(0, self.__row_count - 1), entrance_y]])
        return entrance_location

    def dungeon_generator(self):
        """
        Generate the dungeon by setting up the entrance point, create_room from RoomFactory class and lists of lists.
        """
        entrance_point = self.entrance_exit_generator()
        while True:
            exit_point = self.entrance_exit_generator()
            if exit_point != entrance_point:
                break
        for r in range(0, self.__row_count):
            room_row = []
            for c in range(0, self.__column_count):
                is_entrance_or_exit = entrance_point == [r, c] or exit_point == [r, c]
                content = " " if is_entrance_or_exit else self.set_room_content()
                room_row.append(RoomFactory.create_room(r, c, self.__row_count - 1, self.__column_count - 1,
                                                        is_entrance_or_exit,
                                                        content))
                if content == "V":
                    self.__vision_rooms.append([r, c])
            self.__room_list.append(room_row)
        self.set_room_vision_potion()
        return self.__room_list

    def set_room_content(self):
        """
        Set each room content type by percentage
        """
        self.cal_room_content()
        num = random.randint(0, sum(self.__room_content_count))  # generate a sequence of random numbers based on the room has content
        for idx in range(len(self.__room_content)):  # iterate through each room content type
            if num < self.__room_content_count[idx]:
                self.__room_content_count[idx] -= 1
                return list(self.__room_content.keys())[idx]
            else:
                num -= self.__room_content_count[idx]
        return list(self.__room_content.keys())[-1]

    def cal_room_content(self):
        """
        Calculate the count of each room content type by percentage
        """
        total_room_count = self.__column_count * self.__row_count
        self.__room_content_count = [math.floor(x * total_room_count) for x in self.__room_content.values()]

    def set_room_vision_potion(self):
        """
        Visualize the 8 adjacent rooms around the current room
        """
        for row, col in self.__vision_rooms:
            self.__room_list[row][col].vision_potion_rooms = self.get_vision_potion_rooms(row, col)

    def get_vision_potion_rooms(self, row, col):
        rooms = []
        offsets = [-1, 0, 1]
        for r_offset in offsets:
            n_row = row + r_offset
            if 0 <= n_row < self.__row_count:
                room = []
                for c_offset in offsets:
                    n_col = col + c_offset
                    if 0 <= n_col < self.__column_count:
                        room.append(self.__room_list[n_row][n_col])
                rooms.append(room)
        return rooms

    def __str__(self):
        res = ""
        for row in self.__room_list:
            for i in range(3):
                line = []
                for col in row:
                    line += col.room_matrix[i]
                    line.append(" ")
                res += "".join(line) + "\n"
        return res


if __name__ == "__main__":
    dungeon = Dungeon(6, 6)
    dungeon.dungeon_generator()
    print(dungeon)
    # print(dungeon.entrance_exit_generator())
    # print(dungeon.set_room_content())
