import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
SKY_BLUE = (36, 167, 237)
PINK = (219, 7, 219)

class Node:
    def __init__(self, x, y, width, total_rows):
        self.x = x
        self.y = y
        self.width = width
        self.total_rows = total_rows
        self.color = WHITE
        self.prev = None
        self.is_visited = False
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        self.neighbours = []


    def has_visited(self):
        return self.is_visited

    def set_visited(self):
        self.is_visited = True
        if not self.is_start and not self.is_end:
            self.set_color(SKY_BLUE)

    def get_pos(self):
        return (self.x, self.y)

    def set_color(self, color):
        self.color = color

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node

    def set_open(self):
        if not self.is_start and not self.is_end:
            self.color = PINK

    def set_wall(self):
        self.is_wall = True
        self.set_color(BLACK)

    def remove_wall(self):
        self.is_wall = False
        self.set_color(WHITE)

    def has_wall(self):
        return self.is_wall

    def set_start(self):
        self.is_start = True
        self.set_color(BLUE)

    def remove_start(self):
        self.is_start = False
        self.set_color(WHITE)

    def set_end(self):
        self.is_end = True
        self.set_color(GREEN)

    def remove_end(self):
        self.is_end = False
        self.set_color(WHITE)

    def update_neighbours(self, grid):
        row = self.y
        col = self.x
        if col != 0 and not grid[row][col - 1].has_wall():   #UP
            self.neighbours.append(grid[row][col - 1])
        if col < self.total_rows - 1 and not grid[row][col + 1].has_wall():   #DOWN
            self.neighbours.append(grid[row][col + 1])
        if row != 0 and not grid[row - 1][col].has_wall():   #LEFT
            self.neighbours.append(grid[row - 1][col])
        if row < self.total_rows - 1  and not grid[row + 1][col].has_wall():   #RIGHT
            self.neighbours.append(grid[row + 1][col])

    def get_neighbours(self):
        return self.neighbours

    def draw_node(self, surface):
        block = pygame.Rect(self.x*self.width + 1, self.y*self.width + 1, self.width -2, self.width -2)
        pygame.draw.rect(surface, self.color, block)
