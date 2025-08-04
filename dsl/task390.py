DOWN = (1, 0)
UNITY = (1, 1)
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
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def backdrop(patch):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
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
def identity(x):
 return x
def inbox(patch):
 ai, aj = uppermost(patch) + 1, leftmost(patch) + 1
 bi, bj = lowermost(patch) - 1, rightmost(patch) - 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
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
def first(container):
 return next(iter(container))
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def positive(x):
 return x > 0
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def righthalf(grid):
 return rot270(bottomhalf(rot90(grid)))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def size(container):
 return len(container)
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def shape(piece):
 return (height(piece), width(piece))
def subgrid(patch,grid):
 return crop(grid, ulcorner(patch), shape(patch))
def tojvec(j):
 return (0, j)
def trim(grid):
 return tuple(r[1:-1] for r in grid[1:-1])
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def vmirror(piece):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def verify_task390(I):
 x0 = partition(I)
 x1 = fork(multiply, height, width)
 x2 = argmin(x0, x1)
 x3 = argmax(x0, x1)
 x4 = remove(x2, x0)
 x5 = other(x4, x3)
 x6 = subgrid(x5, I)
 x7 = frontiers(x6)
 x8 = sfilter(x7, hline)
 x9 = size(x8)
 x10 = positive(x9)
 x11 = branch(x10, dmirror, identity)
 x12 = x11(I)
 x13 = color(x5)
 x14 = ofcolor(x12, x13)
 x15 = subgrid(x14, x12)
 x16 = trim(x15)
 x17 = lefthalf(x16)
 x18 = vmirror(x17)
 x19 = asobject(x18)
 x20 = righthalf(x16)
 x21 = vmirror(x20)
 x22 = asobject(x21)
 x23 = color(x3)
 x24 = inbox(x14)
 x25 = backdrop(x24)
 x26 = fill(x12, x23, x25)
 x27 = urcorner(x14)
 x28 = add(x27, UNITY)
 x29 = shift(x22, x28)
 x30 = ulcorner(x14)
 x31 = width(x19)
 x32 = invert(x31)
 x33 = tojvec(x32)
 x34 = add(DOWN, x33)
 x35 = add(x30, x34)
 x36 = shift(x19, x35)
 x37 = combine(x29, x36)
 x38 = paint(x26, x37)
 x39 = x11(x38)
 return x39
def p(g):
 return [list(r)for r in verify_task390(tuple(tuple(r) for r in g))]