EIGHT = 8
TWO = 2
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def color(obj):
 return next(iter(obj))[0]
def compose(outer,inner):
 return lambda x: outer(inner(x))
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
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def cover(grid,patch):
 return fill(grid, mostcolor(grid), toindices(patch))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def extract(container,condition):
 return next(e for e in container if condition(e))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def flip(b):
 return not b
def greater(a,b):
 return a > b
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
def identity(x):
 return x
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def manhattan(a,b):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def matcher(function,target):
 return lambda x: function(x) == target
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def tojvec(j):
 return (0, j)
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
def verify_task131(I):
 x0 = ofcolor(I, TWO)
 x1 = hline(x0)
 x2 = branch(x1, dmirror, identity)
 x3 = x2(I)
 x4 = fgpartition(x3)
 x5 = matcher(color, TWO)
 x6 = compose(flip, x5)
 x7 = extract(x4, x6)
 x8 = ofcolor(x3, TWO)
 x9 = leftmost(x8)
 x10 = leftmost(x7)
 x11 = greater(x9, x10)
 x12 = manhattan(x7, x8)
 x13 = decrement(x12)
 x14 = branch(x11, identity, invert)
 x15 = branch(x11, decrement, increment)
 x16 = branch(x11, leftmost, rightmost)
 x17 = x14(x13)
 x18 = tojvec(x17)
 x19 = shift(x7, x18)
 x20 = x16(x19)
 x21 = x15(x20)
 x22 = tojvec(x21)
 x23 = vfrontier(x22)
 x24 = cover(x3, x7)
 x25 = paint(x24, x19)
 x26 = fill(x25, EIGHT, x23)
 x27 = x2(x26)
 return x27
def p(g):
 return [list(r)for r in verify_task131(tuple(tuple(r) for r in g))]