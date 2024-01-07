# MTD 1 : 

from collections import namedtuple

Colors = namedtuple('Colors', ['WHITE', 'RED', 'GREEN1', 'GREEN2', 'BLACK'])

colors = Colors(
    WHITE=(255, 255, 255),
    RED=(220, 48, 75),
    GREEN1=(61, 163, 0),
    GREEN2=(69, 187, 0),
    BLACK=(0, 0, 0)
)

'''
Can be used as (in any other file): 

from colors import colors

print("WHITE color:", colors.WHITE)
print("RED color:", colors.RED)

'''




#MTD 2 : 
# colors = {
#     'WHITE': (255, 255, 255),
#     'RED': (220, 48, 75),
#     'GREEN1': (61, 163, 0),
#     'GREEN2': (69, 187, 0),
#     'BLACK': (0, 0, 0)
# }

'''
Can be used as (in any other file): 

from colors import colors

print("WHITE color:", colors['WHITE'])
print("RED color:", colors['RED'])

'''
