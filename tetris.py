### First try tetris by ActionHOSchT

# necessary imports
import pygame as pg


#global variables
width = 400
columns = 10
line = 20
distance = width // columns
height = distance * columns
grid = [0]* columns* line
weitermachen = True    #read go on

# game ground
pictures = []
for n in range(8):
    pictures.append(pg.transform.scale(pg.image.load('tetrisblock_{n}.gif')) #(f'tetrisblock_{n}.gif'),(distance,distance)))


#show screen
pg.init()
screen = pg.display.set_mode([width, height])


# gameloop
while goOn:
    for event in pg.event.get():
        if event.type == pg.QUIT:
        	weitermachen = False
    screen.fill((0,0,0))
    for n, color in enumerate(grid): # von 0 bis 199
        if color > 0:
            x = n % columns * distance
            y = n // columns * distance
            screen.blit(pictures[color],(x,y))

    pg.display.flip()


pg.quit()

# Spielfeld 
#
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]

# Blöcke/Figuren (auch Tetrominoe) (7)
#
# [1][ ][ ][ ]    # [ ][4][4][ ]    # [7][ ][ ][ ]
# [1][1][1][ ]    # [4][4][ ][ ]    # [7][ ][ ][ ]
# [ ][ ][ ][ ]    # [ ][ ][ ][ ]    # [7][ ][ ][ ]
# [ ][ ][ ][ ]    # [ ][ ][ ][ ]    # [7][ ][ ][ ]
#
# [ ][ ][2][ ]    # [ ][5][ ][ ]
# [2][2][2][ ]    # [5][5][5][ ]
# [ ][ ][ ][ ]    # [ ][ ][ ][ ]
# [ ][ ][ ][ ]    # [ ][ ][ ][ ]
#
# [3][3][ ][ ]    # [ ][ ][ ][ ]
# [ ][3][3][ ]    # [ ][6][6][ ]
# [ ][ ][ ][ ]    # [ ][6][6][ ]
# [ ][ ][ ][ ]    # [ ][ ][ ][ ]