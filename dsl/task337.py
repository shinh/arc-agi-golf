def switch(
 grid,
 a,
 b
):
 return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)
EIGHT = 8
FIVE = 5
def verify_task337(I):
 x0 = switch(I, FIVE, EIGHT)
 return x0
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]