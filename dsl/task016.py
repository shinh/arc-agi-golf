TWO = 2
SIX = 6
def switch(
 grid,
 a,
 b
):
 return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)
THREE = 3
FOUR = 4
EIGHT = 8
ONE = 1
FIVE = 5
NINE = 9
def verify_task016(I):
 x0 = switch(I, THREE, FOUR)
 x1 = switch(x0, EIGHT, NINE)
 x2 = switch(x1, TWO, SIX)
 x3 = switch(x2, ONE, FIVE)
 return x3
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]