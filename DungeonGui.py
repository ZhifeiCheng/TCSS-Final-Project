from tkinter import *
import tkinter as tk
from Dungeon import Dungeon
from Adventurer import Adventurer
from Dungeon import Dungeon
from DungeonAdventure import DungeonAdventurer

class DungeonGui(object):

    def __init__(self,num_rows, num_cols):
        global my_canvas, my_window,adventurer_image, my_image
        self.num_rows=num_rows
        self.num_cols=num_cols

        self.col_width =100
        self.row_height=100

        self.room = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self.east_west_door = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self.north_south_door = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self.north_door = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self.south_door = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        my_window = tk.Tk()
        my_window.title('Dungeon-2')
        my_canvas = tk.Canvas(master=my_window, width=1000, height=1000, background='white')
        self.my_canvas = my_canvas
        self.adventurer_image = PhotoImage(master=my_canvas, file="adventurer2_img.png")
        #my_image = my_canvas.create_image(0, 0, anchor=NW, image=self.adventurer_image)
        my_window.bind("<Left>", DungeonGui.left)
        my_window.bind("<Right>", DungeonGui.right)
        my_window.bind("<Up>", DungeonGui.up)
        my_window.bind("<Down>", DungeonGui.down)


    def create_rooms(self):
        for i in range(0,self.num_rows):
            row_blank_space=30
            for j in range(0,self.num_rows):
                col_blank_space=30
                self.room[i][j]=self.my_canvas.create_rectangle(j * self.col_width + col_blank_space, i * self.row_height + row_blank_space,
                                                                (j+1) * self.col_width, (i+1) * self.row_height,

                                                              fill="yellow")
            self.my_canvas.pack()
            self.my_canvas.update()

    def create_content(self,index_i,index_j, content):
        """
        Create content such as Pillar, Pit etc at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30

        if content == 'A' or content == 'E' or content == 'E' or content == 'P' or content == 'I':
            self.my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
                                       i * self.row_height + row_blank_space + self.row_height / 3,
                                       text=content, font=("Helvetica", 32), fill='Red')

        else:
            self.my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
                                       i * self.row_height + row_blank_space + self.row_height / 3,
                                       text=content, font=("Helvetica", 20))


    def create_north_door(self,index_i, index_j,north_door_symbol):
        i = index_i
        j = index_j
        if north_door_symbol == '-':
            self.north_door[i][j]=self.my_canvas.create_rectangle(j*self.col_width+50, i*self.row_height+20,
                                               j*self.col_width+80,i*self.row_height+30,
                                               fill="green")
            self.my_canvas.pack()
            self.my_canvas.update()

    def create_south_door(self,index_i, index_j, south_door_symbol):
        i = index_i
        j = index_j
        if south_door_symbol == '-':
            self.south_door[i][j]=self.my_canvas.create_rectangle(j*self.col_width+50, i*self.row_height+110,
                                               j*self.col_width+80,i*self.row_height+100,
                                               fill="green")
            self.my_canvas.pack()
            self.my_canvas.update()

    def create_east_door(self,index_i, index_j, east_door_symbol):
        i = index_i
        j = index_j
        row_blank_space = 40
        col_blank_space = 10
        if east_door_symbol=='|':
            self.east_west_door[i][j]=self.my_canvas.create_rectangle(j*self.col_width+col_blank_space+self.col_width, i*self.row_height+row_blank_space+ row_blank_space,
                                               (j+1)*self.col_width,(i+1)*self.row_height-self.row_height/2,
                                               fill="blue")
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_west_door(self,index_i, index_j, west_door_symbol):
        i = index_i
        j = index_j
        row_blank_space = 40
        col_blank_space = 10
        if west_door_symbol == '|':
            self.east_west_door[i][j]=self.my_canvas.create_rectangle(j*self.col_width+20, i*self.row_height+50,
                                               (j)*self.col_width+col_blank_space+20,(i)*self.row_height+80,
                                               fill="blue")
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_adventurer(self, index_i, index_j):
        return my_canvas.create_image(index_i, index_j, anchor=NW, image=self.adventurer_image)

    def left(event):
        global adventurer_i_index, adventurer_j_index, dng
        curr_i=adventurer_i_index
        curr_j=adventurer_j_index
        next_i=adventurer_i_index

        if event.keysym=='Left':
            adventurer_j_index  = adventurer_j_index-1
            next_j=adventurer_j_index

        if DungeonAdventurer.if_passable(dng,curr_i,curr_j,next_i,next_j,6, 6):
            x = -100
            y = 0
            my_canvas.move(my_image,x,y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image,x,y)

    def right(event):
        global adventurer_i_index, adventurer_j_index, dng
        curr_i = adventurer_i_index
        curr_j = adventurer_j_index
        next_i = adventurer_i_index

        if event.keysym == 'Right':
            adventurer_j_index = adventurer_j_index + 1
            next_j = adventurer_j_index

        if DungeonAdventurer.if_passable(dng, curr_i, curr_j, next_i, next_j, 6, 6):
            x = 100
            y = 0
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)


    def up(event):
        global adventurer_i_index, adventurer_j_index, dng
        curr_i=adventurer_i_index
        curr_j=adventurer_j_index

        next_j=adventurer_j_index
        if event.keysym=='Up':
            adventurer_i_index  = adventurer_i_index-1
            next_i=adventurer_i_index

        if DungeonAdventurer.if_passable(dng,curr_i,curr_j,next_i,next_j,6, 6):
            x = 0
            y = -100
            my_canvas.move(my_image,x,y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image,x,y)

    def down(event):
        global adventurer_i_index, adventurer_j_index, dng
        curr_i=adventurer_i_index
        curr_j=adventurer_j_index

        next_j=adventurer_j_index
        if event.keysym=='Down':
            adventurer_i_index  = adventurer_i_index+1
            next_i=adventurer_i_index

        if DungeonAdventurer.if_passable(dng,curr_i,curr_j,next_i,next_j,6, 6):
            x = 0
            y = 100
            my_canvas.move(my_image,x,y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image,x,y)


    def main(self):
        global my_image, adventurer_i_index, adventurer_j_index, dng
        adventurer_i_index = 0
        adventurer_j_index = 0

        root = tk.Tk()                    # Instantiate a root window
        root.title('Dungeon-3')
        dungeon = DungeonGui(6,6)         # Instantiate a dungeon object (num rows=5, num col=5)
        dungeon.create_rooms()            # Create rooms

        dng = Dungeon(6,6)
        dng.dungeon_generator()
        print(dng)
        for i in range(0, 6):
            for j in range(0, 6):
                row_index = i
                col_index = j
                content = dng.room_list[i][j].room_content
                dungeon.create_content(row_index, col_index, content)

                east_door_symbol=dng.room_list[i][j].room_matrix[1][2]
                dungeon.create_east_door(row_index, col_index, east_door_symbol)

                west_door_symbol = dng.room_list[i][j].room_matrix[1][0]
                dungeon.create_west_door(row_index, col_index, west_door_symbol)

                north_door_symbol = dng.room_list[i][j].room_matrix[0][1]
                dungeon.create_north_door(row_index, col_index, north_door_symbol)

                south_door_symbol = dng.room_list[i][j].room_matrix[2][1]
                dungeon.create_south_door(row_index, col_index, south_door_symbol)

                if content =='i':
                    adventurer_i_index=i
                    adventurer_j_index=j
                    my_image=dungeon.create_adventurer(adventurer_j_index*100+32, adventurer_i_index*100+32)



        root.mainloop()  # enter main loop
        #return adventurer_i_index, adventurer_i_index

if __name__ == "__main__":
    column_count=6
    row_count=6
    dungeon_gui = DungeonGui(int(column_count), int(row_count))
    dungeon_gui.main()

    dng = Dungeon(6, 6)
    dng.dungeon_generator()
    print(DungeonAdventurer.if_passable(dng,1,2,1,3,6,6))