THREE = 3
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def combine(a,b):
 return type(a)((*a, *b))
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
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def frontiers(grid):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
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
def hline(patch):
 return width(patch) == len(patch) and height(patch) == 1
def intersection(a,b):
 return a & b
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
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
def positive(x):
 return x > 0
def righthalf(grid):
 return rot270(bottomhalf(rot90(grid)))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shape(piece):
 return (height(piece), width(piece))
def size(container):
 return len(container)
def verify_task318(I):
 x0 = frontiers(I)
 x1 = sfilter(x0, hline)
 x2 = size(x1)
 x3 = positive(x2)
 x4 = branch(x3, tophalf, lefthalf)
 x5 = branch(x3, bottomhalf, righthalf)
 x6 = x4(I)
 x7 = x5(I)
 x8 = palette(x6)
 x9 = palette(x7)
 x10 = intersection(x8, x9)
 x11 = first(x10)
 x12 = shape(x6)
 x13 = canvas(x11, x12)
 x14 = palette(x6)
 x15 = other(x14, x11)
 x16 = palette(x7)
 x17 = other(x16, x11)
 x18 = ofcolor(x6, x15)
 x19 = ofcolor(x7, x17)
 x20 = combine(x18, x19)
 x21 = fill(x13, THREE, x20)
 return x21
def p(g):
 return [list(r)for r in verify_task318(tuple(tuple(r) for r in g))]