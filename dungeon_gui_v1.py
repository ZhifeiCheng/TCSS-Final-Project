import tkinter as tk
import random as rndm


class DungeonGui(object):
    my_window = tk.Tk()
    my_canvas = tk.Canvas(my_window, width=1000, height=1000, background='white')

    def __init__(self,num_rows, num_cols):
        self.num_rows=num_rows
        self.num_cols=num_cols

        self.col_width =100
        self.row_height=100

        self.room = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self.east_west_door = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self.north_south_door = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]


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


    def create_east_west_doors(self):
        for i in range(0,self.num_rows):
            row_blank_space=30
            for j in range(0,self.num_rows-1):
                col_blank_space=30
                self.east_west_door[i][j]=self.my_canvas.create_rectangle(j*self.col_width+col_blank_space+self.col_width, i*self.row_height+row_blank_space+ row_blank_space,
                                               (j+1)*self.col_width,(i+1)*self.row_height-self.row_height/3,
                                               fill="red")

            self.my_canvas.pack()
            self.my_canvas.update()


    def create_north_south_doors(self):
        for i in range(0,self.num_rows-1):
            row_blank_space=30
            for j in range(0,self.num_rows):
                col_blank_space=30
                self.north_south_door[i][j]=self.my_canvas.create_rectangle(j*self.col_width+col_blank_space+self.col_width/3, i*self.row_height+row_blank_space+self.row_height,
                                               (j+1)*self.col_width-self.col_width/4,(i+1)*self.row_height,
                                               fill="blue")
            self.my_canvas.pack()
            self.my_canvas.update()

    def create_A_pillar(self,index_i,index_j):
        """
        Creates 'A' pillar at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30

        self.my_canvas.create_text(j * self.col_width + col_blank_space+self.col_width/3,
                                   i * self.row_height + row_blank_space+self.row_height/3,
                                   text="A", font=("Helvetica", 32))
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_E_pillar(self,index_i,index_j):
        """
        Creates 'E' pillar at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30

        self.my_canvas.create_text(j * self.col_width + col_blank_space+self.col_width/3,
                                   i * self.row_height + row_blank_space+self.row_height/3,
                                   text="E", font=("Helvetica", 32))
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_I_pillar(self,index_i,index_j):
        """
        Creates 'I' pillar at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30

        self.my_canvas.create_text(j * self.col_width + col_blank_space+self.col_width/3,
                                   i * self.row_height + row_blank_space+self.row_height/3,
                                   text="I", font=("Helvetica", 32))
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_P_pillar(self,index_i,index_j):
        """
        Creates 'P' pillar at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30

        self.my_canvas.create_text(j * self.col_width + col_blank_space+self.col_width/3,
                                   i * self.row_height + row_blank_space+self.row_height/3,
                                   text="P", font=("Helvetica", 32))
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_start_location(self,index_i,index_j):
        """
        Creates 'Start' pillar at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30
        self.my_canvas.create_text(j * self.col_width + col_blank_space+self.col_width/3,
                                   i * self.row_height + row_blank_space+self.row_height/3,
                                   text="Start", font=("Helvetica", 20))
        self.my_canvas.pack()
        self.my_canvas.update()

    def create_end_location(self,index_i,index_j):
        """
        Creates 'End' pillar at a specified Index.
        """
        i=index_i
        j=index_j
        row_blank_space = 30
        col_blank_space = 30
        self.my_canvas.create_text(j * self.col_width + col_blank_space+self.col_width/3,
                                   i * self.row_height + row_blank_space+self.row_height/3,
                                   text="End", font=("Helvetica", 20))
        self.my_canvas.pack()
        self.my_canvas.update()

    def on_click(self,i, j, event):
        global counter
        # color = "red" if counter%2 else "yellow"
        color = "blue"
        event.widget.config(bg=color)
        self.room[i][j] = color
        counter += 1

def main():
    root = tk.Tk()                    # Instantiate a root window
    dungeon = DungeonGui(6,6)         # Instantiate a dungeon object (num rows=5, num col=5)
    dungeon.create_rooms()            # Create rooms
    dungeon.create_east_west_doors()  # Create East West doors
    dungeon.create_north_south_doors() # Create North South Doors
    dungeon.create_A_pillar(1,2)       # Create A-Pillar at a specified Index
    dungeon.create_E_pillar(3,1)       # Create E-Pillar at a specified Index
    dungeon.create_I_pillar(5,2)        # Create I-Pillar at a specified Index
    dungeon.create_P_pillar(3,5)        # Create P-Pillar at a specified Index
    dungeon.create_start_location(0, 0) # Create Start Location at a specified Index
    dungeon.create_end_location(5, 5)   # Create End Location at a specified Index
    root.mainloop()  # enter main loop

if __name__ == '__main__':
    main()


