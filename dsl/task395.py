TWO = 2
def both(a,b):
 return a and b
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def equality(a,b):
 return a == b
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
def flip(b):
 return not b
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(grid,n):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
def intersection(a,b):
 return a & b
def last(container):
 return max(enumerate(container))[1]
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(element):
 return len(palette(element))
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def righthalf(grid):
 return rot270(bottomhalf(rot90(grid)))
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
def shape(piece):
 return (height(piece), width(piece))
def vsplit(grid,n):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task395(I):
 x0 = tophalf(I)
 x1 = numcolors(x0)
 x2 = equality(x1, TWO)
 x3 = bottomhalf(I)
 x4 = numcolors(x3)
 x5 = equality(x4, TWO)
 x6 = both(x2, x5)
 x7 = lefthalf(I)
 x8 = numcolors(x7)
 x9 = equality(x8, TWO)
 x10 = righthalf(I)
 x11 = numcolors(x10)
 x12 = equality(x11, TWO)
 x13 = both(x9, x12)
 x14 = flip(x13)
 x15 = both(x6, x14)
 x16 = branch(x15, vsplit, hsplit)
 x17 = x16(I, TWO)
 x18 = first(x17)
 x19 = last(x17)
 x20 = palette(x18)
 x21 = palette(x19)
 x22 = intersection(x20, x21)
 x23 = first(x22)
 x24 = shape(x18)
 x25 = canvas(x23, x24)
 x26 = ofcolor(x18, x23)
 x27 = ofcolor(x19, x23)
 x28 = intersection(x26, x27)
 x29 = fill(x25, TWO, x28)
 return x29
def p(g):
 return [list(r)for r in verify_task395(tuple(tuple(r) for r in g))]