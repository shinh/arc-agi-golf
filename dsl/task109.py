def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(a,b):
 return (a, b)
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def color(obj):
 return next(iter(obj))[0]
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
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def compress(grid):
 ri = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 ci = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 return tuple(tuple(v for j, v in enumerate(r) if j not in ci) for i, r in enumerate(grid) if i not in ri)
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def frontiers(grid):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def hmirror(piece):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def vconcat(a,b):
 return a + b
def vmirror(piece):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def verify_task109(I):
 x0 = frontiers(I)
 x1 = merge(x0)
 x2 = color(x1)
 x3 = compress(I)
 x4 = mostcolor(x3)
 x5 = tophalf(I)
 x6 = lefthalf(x5)
 x7 = vmirror(x6)
 x8 = hconcat(x6, x7)
 x9 = hmirror(x8)
 x10 = vconcat(x8, x9)
 x11 = tophalf(I)
 x12 = righthalf(x11)
 x13 = vmirror(x12)
 x14 = hconcat(x13, x12)
 x15 = hmirror(x14)
 x16 = vconcat(x14, x15)
 x17 = bottomhalf(I)
 x18 = lefthalf(x17)
 x19 = vmirror(x18)
 x20 = hconcat(x18, x19)
 x21 = hmirror(x20)
 x22 = vconcat(x21, x20)
 x23 = bottomhalf(I)
 x24 = righthalf(x23)
 x25 = vmirror(x24)
 x26 = hconcat(x25, x24)
 x27 = hmirror(x26)
 x28 = vconcat(x27, x26)
 x29 = astuple(x10, x16)
 x30 = astuple(x22, x28)
 x31 = combine(x29, x30)
 x32 = argmax(x31, numcolors)
 x33 = asindices(x32)
 x34 = ofcolor(x32, x4)
 x35 = difference(x33, x34)
 x36 = fill(x32, x2, x35)
 return x36
def p(g):
 return [list(r)for r in verify_task109(tuple(tuple(r) for r in g))]