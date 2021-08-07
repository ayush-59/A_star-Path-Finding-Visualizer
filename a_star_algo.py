import pygame

YELLOW = (255, 255, 0)

# heuristic function which estimates distance of goal from given node
def heuristic(pos1, pos2):
    y1, x1 = pos1
    y2, x2 = pos2
    return abs(x1-x2) + abs(y1-y2)

# function that returns node in open list having lowest f_score
def choose_best_node(open_list):
    best_node = open_list[0]

    for spot in open_list:
        if spot['f_score'] < best_node['f_score']:
            best_node = spot

    return best_node

# Returns Path found using backtracking
def get_path(start, goal, grid):
    path = []
    current = goal
    while True:
        if current == None:
            break
        col, row = current.get_pos()
        if current != start and current != goal:
            grid[row][col].set_color(YELLOW)
        path.append(current.get_pos())
        if current == start:
            break
        current = current.get_prev()
    return path


def run_algo(draw, grid, start, goal):
    open_list = []

    g = 0
    h = heuristic(start.get_pos(), goal.get_pos())
    f = g + h

    current = {'pos': start.get_pos(), 'f_score': f, 'g_score': g, 'h_score': h}
    open_list.append(current)

    while current['pos'] != goal.get_pos():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        open_list.remove(current)

        col, row = current['pos']
        grid[row][col].set_visited()
        neighbours = grid[row][col].get_neighbours()

        for node in neighbours:
            if node.has_visited():
                continue
            if len(list(filter(lambda ele: ele['pos'] == node.get_pos(), open_list))) > 0:
                continue
            g = current['g_score'] + 1
            h = heuristic(node.get_pos(), goal.get_pos())
            f = g + h
            node.set_open()
            node.set_prev(grid[row][col])
            node_info = {'pos': node.get_pos(), 'f_score': f, 'g_score': g, 'h_score': h}
            open_list.append(node_info)


        draw()
        pygame.display.update()
        if not open_list:
            break
        current = choose_best_node(open_list)



    if current['pos'] != goal.get_pos():
        print("No Valid Path")
    else:
        path = get_path(start, goal, grid)
        print(path)
