EIGHT = 8
FOUR = 4
ONE = 1
SIX = 6
THREE = 3
TWO = 2
def astuple(a,b):
 return (a, b)
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def initset(value):
 return frozenset({value})
def insert(value,container):
 return container.union(frozenset({value}))
def last(container):
 return max(enumerate(container))[1]
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def ineighbors(loc):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def neighbors(loc):
 return dneighbors(loc) | ineighbors(loc)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
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
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
def verify_task220(I):
 x0 = lbind(ofcolor, I)
 x1 = lbind(mapply, neighbors)
 x2 = chain(x1, x0, last)
 x3 = fork(recolor, first, x2)
 x4 = astuple(SIX, THREE)
 x5 = astuple(FOUR, EIGHT)
 x6 = astuple(ONE, TWO)
 x7 = initset(x4)
 x8 = insert(x5, x7)
 x9 = insert(x6, x8)
 x10 = mapply(x3, x9)
 x11 = paint(I, x10)
 return x11
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]