def tophalf(
 grid
):
 return grid[:len(grid) // 2]
def lefthalf(
 grid
):
 return rot270(tophalf(rot90(grid)))
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def bottomhalf(
 grid
):
 return grid[len(grid) // 2 + len(grid) % 2:]
def righthalf(
 grid
):
 return rot270(bottomhalf(rot90(grid)))
def equality(
 a,
 b
):
 return a == b
def verify_task188(I):
 x0 = lefthalf(I)
 x1 = righthalf(I)
 x2 = equality(x0, x1)
 x3 = branch(x2, lefthalf, tophalf)
 x4 = x3(I)
 return x4
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]