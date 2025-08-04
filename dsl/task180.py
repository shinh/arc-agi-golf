def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def bottomhalf(grid):
 return grid[len(grid) // 2 + len(grid) % 2:]
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def intersection(a,b):
 return a & b
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def tophalf(grid):
 return grid[:len(grid) // 2]
def lefthalf(grid):
 return rot270(tophalf(rot90(grid)))
def matcher(function,target):
 return lambda x: function(x) == target
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
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def righthalf(grid):
 return rot270(bottomhalf(rot90(grid)))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
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
def verify_task180(I):
 x0 = tophalf(I)
 x1 = lefthalf(x0)
 x2 = tophalf(I)
 x3 = righthalf(x2)
 x4 = bottomhalf(I)
 x5 = righthalf(x4)
 x6 = bottomhalf(I)
 x7 = lefthalf(x6)
 x8 = palette(x1)
 x9 = palette(x3)
 x10 = intersection(x8, x9)
 x11 = palette(x5)
 x12 = palette(x7)
 x13 = intersection(x11, x12)
 x14 = intersection(x10, x13)
 x15 = first(x14)
 x16 = shape(x1)
 x17 = canvas(x15, x16)
 x18 = matcher(first, x15)
 x19 = compose(flip, x18)
 x20 = rbind(sfilter, x19)
 x21 = compose(x20, asobject)
 x22 = x21(x1)
 x23 = x21(x5)
 x24 = x21(x7)
 x25 = x21(x3)
 x26 = paint(x17, x22)
 x27 = paint(x26, x23)
 x28 = paint(x27, x24)
 x29 = paint(x28, x25)
 return x29
def p(g):
 return [list(r)for r in verify_task180(tuple(tuple(r) for r in g))]