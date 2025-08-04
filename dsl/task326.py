ORIGIN = (0, 0)
TWO_BY_TWO = (2, 2)
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def verify_task326(I):
 x0 = crop(I, ORIGIN, TWO_BY_TWO)
 return x0
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]