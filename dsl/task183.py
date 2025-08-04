ORIGIN = (0, 0)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
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
def box(patch):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def color(obj):
 return next(iter(obj))[0]
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
def llcorner(patch):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def corners(patch):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def hconcat(a,b):
 return tuple(i + j for i, j in zip(a, b))
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
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
def first(container):
 return next(iter(container))
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def replace(grid,replacee,replacer):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def righthalf(grid):
 return rot270(bottomhalf(rot90(grid)))
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
def toivec(i):
 return (i, 0)
def tojvec(j):
 return (0, j)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def trim(grid):
 return tuple(r[1:-1] for r in grid[1:-1])
def vconcat(a,b):
 return a + b
def verify_task183(I):
 x0 = trim(I)
 x1 = trim(x0)
 x2 = tophalf(x1)
 x3 = lefthalf(x2)
 x4 = tophalf(x1)
 x5 = righthalf(x4)
 x6 = bottomhalf(x1)
 x7 = lefthalf(x6)
 x8 = bottomhalf(x1)
 x9 = righthalf(x8)
 x10 = index(I, ORIGIN)
 x11 = width(I)
 x12 = decrement(x11)
 x13 = tojvec(x12)
 x14 = index(I, x13)
 x15 = height(I)
 x16 = decrement(x15)
 x17 = toivec(x16)
 x18 = index(I, x17)
 x19 = shape(I)
 x20 = decrement(x19)
 x21 = index(I, x20)
 x22 = compress(I)
 x23 = asindices(x22)
 x24 = box(x23)
 x25 = corners(x23)
 x26 = difference(x24, x25)
 x27 = toobject(x26, x22)
 x28 = color(x27)
 x29 = palette(x1)
 x30 = other(x29, x28)
 x31 = replace(x3, x30, x10)
 x32 = replace(x5, x30, x14)
 x33 = replace(x7, x30, x18)
 x34 = replace(x9, x30, x21)
 x35 = hconcat(x31, x32)
 x36 = hconcat(x33, x34)
 x37 = vconcat(x35, x36)
 return x37
def p(g):
 return [list(r)for r in verify_task183(tuple(tuple(r) for r in g))]