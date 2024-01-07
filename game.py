import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np
from colors import colors

pygame.init()
font = pygame.font.Font('arial.ttf', 25)
#font = pygame.font.SysFont('arial', 25)

# reset
# reward
# play(action) -> computes the direction
# game_iteration -> keeping track of the game frames
# is_collision


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
SPEED = 30

class SnakeGameAI:
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()




    def reset(self):
        # init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, # (320, 240)
                      Point(self.head.x-BLOCK_SIZE, self.head.y),  # (320-20 , 240) --> (300, 240)
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y) # (320-40 , 240) --> (280, 240)
                    ]
        
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

        

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE ) *BLOCK_SIZE    # (0 to 31) * 20
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE ) *BLOCK_SIZE    # (0 to 23) * 20
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        



    def play_step(self, action):
        self.frame_iteration += 1
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

   
        # 2. move
        self._move(action) # update the head
        self.snake.insert(0, self.head)    #eg. my_list = [1, 2, 3, 4, 5] --> insert(2, 10) --> [1, 2, 10, 3, 4, 5]
        
        # 3. check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score
            
        # 4. place new food or just move { THIS MOVING EFFECT LOOKS BCOZ OF INSERT ! }
        if self.head == self.food:  # if ate the food, we're not popping the last element, & keep the snake moving
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()   # if we didn't eat food, we'll pop last element & keep the snake moving
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return reward, game_over, self.score
    



    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True
        
        return False
        



    def _update_ui(self):
        self.display.fill(colors.BLACK)
        
        for pt in self.snake:
            pygame.draw.circle(self.display, colors.GREEN1, (pt.x, pt.y), 12)
            pygame.draw.circle(self.display, colors.GREEN2, (pt.x, pt.y), 8)
            
        pygame.draw.rect(self.display, colors.RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, colors.WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        



    def _move(self, action):
        # [straight, right, left]

        clock_wise = [Direction.RIGHT,Direction.DOWN,Direction.LEFT,Direction.UP]
        idx = clock_wise.index(self.direction) # index of current direction
        
        if np.array_equal(action, [1,0,0]):
            new_dir = clock_wise[idx]   # if moving straight, keep moving. i.e. no change
        elif np.array_equal(action, [0,1,0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]   # if right turn r -> d -> l -> u   (clockwise)
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]   # if left turn r -> u -> l -> d   (counter-clockwise)

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)