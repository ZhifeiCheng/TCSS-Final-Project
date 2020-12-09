import random
from Room import Room


class RoomFactory:
    @staticmethod
    def create_room(row_count: int, col_count: int, max_row_count: int, max_col_count: int, is_entrance_or_exit=False,
                    room_content=" "):
        room = Room()
        room_matrix = room.room_matrix  # default room matrix is filled with "*" as walls
        room_matrix[1][1] = room_content
        if is_entrance_or_exit:  # if the room locates at the perimeter and is entrance or exit
            room_matrix[0][1] = "-"
            room_matrix[1][0] = "|"
            room_matrix[2][1] = "-"
            room_matrix[1][2] = "|"
        else:
            room_matrix[0][1] = "*" if row_count == 0 or bool(random.getrandbits(1)) else "-"
            room_matrix[1][0] = "*" if col_count == 0 or bool(random.getrandbits(1)) else "|"
            room_matrix[2][1] = "*" if row_count == max_row_count or bool(random.getrandbits(1)) else "_"
            room_matrix[1][2] = "*" if col_count == max_col_count or bool(random.getrandbits(1)) else "|"
        return room


if __name__ == "__main__":
    print(RoomFactory.create_room(0, 0, 5, 5, True))

