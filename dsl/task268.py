DOWN = (1, 0)
DOWN_LEFT = (1, -1)
FOUR = 4
LEFT = (0, -1)
NEG_UNITY = (-1, -1)
RIGHT = (0, 1)
UNITY = (1, 1)
UP = (-1, 0)
UP_RIGHT = (-1, 1)
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
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def combine(a,b):
 return type(a)((*a, *b))
def backdrop(patch):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def delta(patch):
 if len(patch) == 0:
  return frozenset({})
 return backdrop(patch) - toindices(patch)
def equality(a,b):
 return a == b
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def intersection(a,b):
 return a & b
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def llcorner(patch):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def connect(a,b):
 ai, aj = a
 bi, bj = b
 si = min(ai, bi)
 ei = max(ai, bi) + 1
 sj = min(aj, bj)
 ej = max(aj, bj) + 1
 if ai == bi:
  return frozenset((ai, j) for j in range(sj, ej))
 elif aj == bj:
  return frozenset((i, aj) for i in range(si, ei))
 elif bi - ai == bj - aj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
 elif bi - ai == aj - bj:
  return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
 return frozenset()
def shoot(start,direction):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def verify_task268(I):
 x0 = fgpartition(I)
 x1 = merge(x0)
 x2 = delta(x1)
 x3 = fill(I, FOUR, x2)
 x4 = delta(x1)
 x5 = box(x1)
 x6 = intersection(x4, x5)
 x7 = uppermost(x6)
 x8 = uppermost(x1)
 x9 = equality(x7, x8)
 x10 = leftmost(x6)
 x11 = leftmost(x1)
 x12 = equality(x10, x11)
 x13 = lowermost(x6)
 x14 = lowermost(x1)
 x15 = equality(x13, x14)
 x16 = rightmost(x6)
 x17 = rightmost(x1)
 x18 = equality(x16, x17)
 x19 = urcorner(x6)
 x20 = ulcorner(x6)
 x21 = llcorner(x6)
 x22 = lrcorner(x6)
 x23 = branch(x15, x21, x22)
 x24 = branch(x12, x20, x23)
 x25 = branch(x9, x19, x24)
 x26 = branch(x15, x22, x19)
 x27 = branch(x12, x21, x26)
 x28 = branch(x9, x20, x27)
 x29 = branch(x15, DOWN_LEFT, UNITY)
 x30 = branch(x12, NEG_UNITY, x29)
 x31 = branch(x9, UP_RIGHT, x30)
 x32 = branch(x15, UNITY, UP_RIGHT)
 x33 = branch(x12, DOWN_LEFT, x32)
 x34 = branch(x9, NEG_UNITY, x33)
 x35 = branch(x15, DOWN, RIGHT)
 x36 = branch(x12, LEFT, x35)
 x37 = branch(x9, UP, x36)
 x38 = shoot(x25, x31)
 x39 = shoot(x28, x34)
 x40 = combine(x38, x39)
 x41 = rbind(shoot, x37)
 x42 = mapply(x41, x6)
 x43 = combine(x42, x40)
 x44 = fill(x3, FOUR, x43)
 return x44
def p(g):
 return [list(r)for r in verify_task268(tuple(tuple(r) for r in g))]