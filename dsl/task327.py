UNITY = (1, 1)
def apply(function,container):
 return type(container)(function(e) for e in container)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def center(patch):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def color(obj):
 return next(iter(obj))[0]
def compose(outer,inner):
 return lambda x: outer(inner(x))
def double(n):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
def first(container):
 return next(iter(container))
def flip(b):
 return not b
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def initset(value):
 return frozenset({value})
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shape(piece):
 return (height(piece), width(piece))
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
def verify_task327(I):
 x0 = asobject(I)
 x1 = mostcolor(I)
 x2 = matcher(first, x1)
 x3 = compose(flip, x2)
 x4 = sfilter(x0, x3)
 x5 = apply(initset, x4)
 x6 = rbind(shoot, UNITY)
 x7 = compose(x6, center)
 x8 = fork(recolor, color, x7)
 x9 = mapply(x8, x5)
 x10 = shape(I)
 x11 = double(x10)
 x12 = mostcolor(I)
 x13 = canvas(x12, x11)
 x14 = paint(x13, x9)
 return x14
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]