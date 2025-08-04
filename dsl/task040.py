ONE = 1
ORIGIN = (0, 0)
def astuple(a,b):
 return (a, b)
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(iterable):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
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
def equality(a,b):
 return a == b
def even(n):
 return n % 2 == 0
def first(container):
 return next(iter(container))
def flip(b):
 return not b
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
def identity(x):
 return x
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def remove(value,container):
 return type(container)(e for e in container if e != value)
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
def size(container):
 return len(container)
def vconcat(a,b):
 return a + b
def verify_task040(I):
 x0 = first(I)
 x1 = dedupe(x0)
 x2 = size(x1)
 x3 = equality(x2, ONE)
 x4 = flip(x3)
 x5 = branch(x4, lefthalf, tophalf)
 x6 = branch(x4, righthalf, bottomhalf)
 x7 = branch(x4, hconcat, vconcat)
 x8 = x5(I)
 x9 = x6(I)
 x10 = index(x8, ORIGIN)
 x11 = shape(x9)
 x12 = decrement(x11)
 x13 = index(x9, x12)
 x14 = mostcolor(I)
 x15 = mostcolor(I)
 x16 = palette(I)
 x17 = remove(x10, x16)
 x18 = remove(x13, x17)
 x19 = remove(x15, x18)
 x20 = first(x19)
 x21 = replace(x8, x20, x10)
 x22 = branch(x4, dmirror, identity)
 x23 = branch(x4, height, width)
 x24 = x23(I)
 x25 = astuple(ONE, x24)
 x26 = canvas(x14, x25)
 x27 = x22(x26)
 x28 = replace(x9, x20, x13)
 x29 = x7(x21, x27)
 x30 = branch(x4, width, height)
 x31 = x30(I)
 x32 = even(x31)
 x33 = branch(x32, x21, x29)
 x34 = x7(x33, x28)
 return x34
def p(g):
 return [list(r)for r in verify_task040(tuple(tuple(r) for r in g))]