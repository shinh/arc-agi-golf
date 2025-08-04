def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(a,b):
 return (a, b)
def color(obj):
 return next(iter(obj))[0]
def colorcount(element,value):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def combine(a,b):
 return type(a)((*a, *b))
def difference(a,b):
 return type(a)(e for e in a if e not in b)
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
def hfrontier(location):
 return frozenset((location[0], j) for j in range(30))
def initset(value):
 return frozenset({value})
def leastcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def center(patch):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def position(a,b):
 ia, ja = center(toindices(a))
 ib, jb = center(toindices(b))
 if ia == ib:
  return (0, 1 if ja < jb else -1)
 elif ja == jb:
  return (1 if ia < ib else -1, 0)
 elif ia < ib:
  return (1, 1 if ja < jb else -1)
 elif ia > ib:
  return (-1, 1 if ja < jb else -1)
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
def verify_task362(I):
 x0 = frontiers(I)
 x1 = merge(x0)
 x2 = color(x1)
 x3 = asobject(I)
 x4 = difference(x3, x1)
 x5 = leastcolor(x4)
 x6 = colorcount(I, x5)
 x7 = mostcolor(x4)
 x8 = ofcolor(I, x5)
 x9 = toindices(x1)
 x10 = combine(x9, x8)
 x11 = fill(I, x7, x10)
 x12 = argmax(x0, width)
 x13 = uppermost(x12)
 x14 = argmax(x0, height)
 x15 = leftmost(x14)
 x16 = astuple(x13, x15)
 x17 = initset(x16)
 x18 = position(x8, x17)
 x19 = multiply(x18, x6)
 x20 = add(x16, x19)
 x21 = hfrontier(x20)
 x22 = vfrontier(x20)
 x23 = combine(x21, x22)
 x24 = fill(x11, x2, x23)
 return x24
def p(g):
 return [list(r)for r in verify_task362(tuple(tuple(r) for r in g))]