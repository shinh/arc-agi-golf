TWO = 2
TWO_BY_TWO = (2, 2)
def apply(function,container):
 return type(container)(function(e) for e in container)
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def extract(container,condition):
 return next(e for e in container if condition(e))
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
def first(container):
 return next(iter(container))
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(grid,n):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
def initset(value):
 return frozenset({value})
def intersection(a,b):
 return a & b
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
def matcher(function,target):
 return lambda x: function(x) == target
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(element):
 return len(palette(element))
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def rapply(functions,value):
 return type(functions)(function(value) for function in functions)
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
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
def vsplit(grid,n):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def verify_task227(I):
 x0 = astuple(vsplit, hsplit)
 x1 = rbind(rbind, TWO)
 x2 = rbind(rapply, I)
 x3 = initset(x1)
 x4 = lbind(rapply, x3)
 x5 = chain(first, x2, x4)
 x6 = lbind(apply, numcolors)
 x7 = compose(x6, x5)
 x8 = matcher(x7, TWO_BY_TWO)
 x9 = extract(x0, x8)
 x10 = x9(I, TWO)
 x11 = first(x10)
 x12 = last(x10)
 x13 = palette(x11)
 x14 = palette(x12)
 x15 = intersection(x13, x14)
 x16 = first(x15)
 x17 = shape(x11)
 x18 = canvas(x16, x17)
 x19 = ofcolor(x11, x16)
 x20 = ofcolor(x12, x16)
 x21 = intersection(x19, x20)
 x22 = fill(x18, TWO, x21)
 return x22
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]