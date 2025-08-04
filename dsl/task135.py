ORIGIN = (0, 0)
THREE_BY_THREE = (3, 3)
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def verify_task135(I):
 x0 = rot270(I)
 x1 = crop(x0, ORIGIN, THREE_BY_THREE)
 x2 = rot90(x1)
 return x2
def p(g):
 return [list(r)for r in verify_task135(tuple(tuple(r) for r in g))]