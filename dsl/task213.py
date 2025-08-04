ONE = 1
def apply(function,container):
 return type(container)(function(e) for e in container)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def color(obj):
 return next(iter(obj))[0]
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
def either(a,b):
 return a or b
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
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
def identity(x):
 return x
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def matcher(function,target):
 return lambda x: function(x) == target
def order(container,compfunc):
 return tuple(sorted(container, key=compfunc))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def repeat(item,num):
 return tuple(item for i in range(num))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def size(container):
 return len(container)
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def verify_task213(I):
 x0 = partition(I)
 x1 = matcher(height, ONE)
 x2 = matcher(width, ONE)
 x3 = fork(either, x1, x2)
 x4 = sfilter(x0, x3)
 x5 = matcher(height, ONE)
 x6 = sfilter(x4, x5)
 x7 = size(x6)
 x8 = matcher(width, ONE)
 x9 = sfilter(x4, x8)
 x10 = size(x9)
 x11 = greater(x7, x10)
 x12 = branch(x11, dmirror, identity)
 x13 = branch(x11, uppermost, leftmost)
 x14 = order(x4, x13)
 x15 = apply(color, x14)
 x16 = size(x4)
 x17 = repeat(x15, x16)
 x18 = x12(x17)
 return x18
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]