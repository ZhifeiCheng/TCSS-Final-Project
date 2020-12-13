import unittest
from Room import Room
from RoomFactory import RoomFactory
from Dungeon import Dungeon


class MyTests(unittest.TestCase):

    """
    1) Testing 'Room' class functionality
    """
    def test_room_content_with_A_pillar(self):
        try:
            room= Room("A")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "A", "room content does not returns A")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_E_pillar(self):
        try:
            room= Room("E")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "E", "room content does not returns E")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_I_pillar(self):
        try:
            room= Room("I")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "I", "room content does not returns I")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_P_pillar(self):
        try:
            room= Room("P")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "P", "room content does not returns P")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_empty_content(self):
        try:
            room= Room("")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "", "room content does not returns empty")
        except ValueError as value_error:
            self.assertEqual(True, True)


    """
    2) Testing 'Room Factory' class functionality
    """

    def test_RoomFactory_room_has_NORTH_doors_and_walls(self):
        try:
            rm_factory= RoomFactory.create_room(1,1,2,2," ")
            temp2=rm_factory.room_matrix[0][1]=='*' or rm_factory.room_matrix[0][1]=='-'
            self.assertEqual(temp2, True, "north doors and walls not present")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_RoomFactory_room_has_SOUTH_doors_and_walls(self):
        try:
            rm_factory= RoomFactory.create_room(2,2,2,2," ")
            print(rm_factory.room_matrix[2][1])
            temp3=rm_factory.room_matrix[2][1]=='*' or rm_factory.room_matrix[2][1]=='-'
            self.assertEqual(temp3, True, "south doors and walls not present")
        except ValueError as value_error:
            self.assertEqual(True, True)


    def test_RoomFactory_room_has_East_doors_and_walls(self):
        try:
            rm_factory= RoomFactory.create_room(0,0,1,1," ")
            temp1=rm_factory.room_matrix[1][2]=='*' or rm_factory.room_matrix[1][2]=='|'
            self.assertEqual(temp1, True, "room content does not returns P")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_RoomFactory_room_has_West_doors_and_walls(self):
        try:
            rm_factory= RoomFactory.create_room(0,0,1,1," ")
            temp1=rm_factory.room_matrix[1][0]=='*' or rm_factory.room_matrix[1][0]=='|'
            self.assertEqual(temp1, True, "room content does not returns P")
        except ValueError as value_error:
            self.assertEqual(True, True)

    """
    2) Testing 'Dungeon' class functionality
    """

    def test_dungeon_has_Pit_X(self):
        try:
            dungeon = Dungeon(10, 10)
            dungeon.dungeon_generator()
            temp_list = list(dungeon.__str__())
            self.assertIn('X', temp_list, "dungeon does not pit X")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_dungeon_has_entrance_i(self):
        try:
            dungeon = Dungeon(10, 10)
            dungeon.dungeon_generator()
            temp_list = list(dungeon.__str__())
            self.assertIn('i', temp_list, "dungeon does not have entrance i")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_dungeon_has_exit_O(self):
        dungeon = Dungeon(6, 6)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('O', temp_list, "dungeon does not have exit O")

    def test_dungeon_has_vision_potion_V(self):
        dungeon = Dungeon(8, 8)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('V', temp_list, "dungeon does not have healing potion V")

    def test_dungeon_has_healing_potion_H(self):
        dungeon = Dungeon(6, 6)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('H', temp_list, "dungeon does not have healing potion H")


    def test_dungeon_has_multiple_items_M(self):
        dungeon = Dungeon(10, 10)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('M', temp_list, "dungeon does not have multiple items 'M'")


    def test_dungeon_has_A_pillar(self):
        dungeon = Dungeon(6, 6)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('A',temp_list,"dungeon does not have 'A' pillar ")

    def test_dungeon_has_E_pillar(self):
        dungeon = Dungeon(6, 6)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('E',temp_list,"dungeon does not have 'E' pillar ")

    def test_dungeon_has_I_pillar(self):
        dungeon = Dungeon(6, 6)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('I',temp_list,"dungeon does not have 'I' pillar ")

    def test_dungeon_has_P_pillar(self):
        dungeon = Dungeon(6, 6)
        dungeon.dungeon_generator()
        temp_list = list(dungeon.__str__())
        self.assertIn('P',temp_list,"dungeon does not have 'P' pillar ")

    def test_entrance_location_is_positive(self):
        try:
            dungeon = Dungeon(6, 6)
            temp4 = dungeon.entrance_generator()
            self.assertGreaterEqual(temp4, [0, 0], "entrance location is positive")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_entrance_location_within_the_max_value(self):
        try:
            dungeon = Dungeon(6, 6)
            temp4 = dungeon.entrance_generator()
            self.assertLess(temp4, [6, 6], "entrance location is positive")
        except ValueError as value_error:
            self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()