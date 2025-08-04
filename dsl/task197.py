ONE = 1
def apply(function,container):
 return type(container)(function(e) for e in container)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def contained(value,container):
 return value in container
def difference(a,b):
 return type(a)(e for e in a if e not in b)
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
def first(container):
 return next(iter(container))
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
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
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
def positive(x):
 return x > 0
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
def repeat(item,num):
 return tuple(item for i in range(num))
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
def toivec(i):
 return (i, 0)
def totuple(container):
 return tuple(container)
def verify_task197(I):
 x0 = frontiers(I)
 x1 = sfilter(x0, hline)
 x2 = size(x1)
 x3 = positive(x2)
 x4 = branch(x3, identity, dmirror)
 x5 = x4(I)
 x6 = frontiers(I)
 x7 = merge(x6)
 x8 = mostcolor(x7)
 x9 = matcher(identity, x8)
 x10 = rbind(sfilter, x9)
 x11 = compose(size, x10)
 x12 = argmin(x5, x11)
 x13 = repeat(x12, ONE)
 x14 = asobject(x13)
 x15 = palette(x14)
 x16 = totuple(x15)
 x17 = first(x16)
 x18 = last(x16)
 x19 = fgpartition(x5)
 x20 = merge(x19)
 x21 = toindices(x20)
 x22 = apply(first, x21)
 x23 = lbind(sfilter, x20)
 x24 = compose(first, last)
 x25 = lbind(matcher, x24)
 x26 = compose(x23, x25)
 x27 = apply(x26, x22)
 x28 = lbind(shift, x14)
 x29 = chain(x28, toivec, uppermost)
 x30 = matcher(first, x17)
 x31 = rbind(sfilter, x30)
 x32 = rbind(compose, last)
 x33 = lbind(rbind, contained)
 x34 = chain(toindices, x31, x29)
 x35 = chain(x32, x33, x34)
 x36 = fork(sfilter, identity, x35)
 x37 = compose(color, x36)
 x38 = compose(x31, x29)
 x39 = fork(recolor, x37, x38)
 x40 = fork(other, palette, x37)
 x41 = compose(x31, x29)
 x42 = fork(difference, x29, x41)
 x43 = fork(recolor, x40, x42)
 x44 = fork(combine, x39, x43)
 x45 = mapply(x44, x27)
 x46 = paint(x5, x45)
 x47 = x4(x46)
 return x47
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]