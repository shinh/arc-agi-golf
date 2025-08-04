ONE = 1
ORIGIN = (0, 0)
THREE = 3
TWO = 2
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def divide(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(patch):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def height(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def intersection(a,b):
 return a & b
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def tojvec(j):
 return (0, j)
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def verify_task321(I):
 x0 = width(I)
 x1 = increment(x0)
 x2 = divide(x1, THREE)
 x3 = decrement(x2)
 x4 = height(I)
 x5 = astuple(x4, x3)
 x6 = crop(I, ORIGIN, x5)
 x7 = add(x3, ONE)
 x8 = tojvec(x7)
 x9 = crop(I, x8, x5)
 x10 = double(x3)
 x11 = add(x10, TWO)
 x12 = tojvec(x11)
 x13 = crop(I, x12, x5)
 x14 = palette(x6)
 x15 = palette(x9)
 x16 = palette(x13)
 x17 = intersection(x14, x15)
 x18 = intersection(x17, x16)
 x19 = first(x18)
 x20 = other(x14, x19)
 x21 = other(x15, x19)
 x22 = other(x16, x19)
 x23 = canvas(x19, x5)
 x24 = ofcolor(x6, x20)
 x25 = ofcolor(x9, x21)
 x26 = ofcolor(x13, x22)
 x27 = fill(x23, x22, x26)
 x28 = fill(x27, x21, x25)
 x29 = fill(x28, x20, x24)
 return x29
def p(g):
 return [list(r)for r in verify_task321(tuple(tuple(r) for r in g))]