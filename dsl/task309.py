FIVE = 5
SEVEN = 7
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def verify_task309(I):
 x0 = replace(I, SEVEN, FIVE)
 return x0
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]