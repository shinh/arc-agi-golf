def apply(function,container):
 return type(container)(function(e) for e in container)
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
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
def backdrop(patch):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def color(obj):
 return next(iter(obj))[0]
def compose(outer,inner):
 return lambda x: outer(inner(x))
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def cover(grid,patch):
 return fill(grid, mostcolor(grid), toindices(patch))
def equality(a,b):
 return a == b
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def initset(value):
 return frozenset({value})
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def manhattan(a,b):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def first(container):
 return next(iter(container))
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def outbox(patch):
 ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
 bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def size(container):
 return len(container)
def verify_task250(I):
 x0 = fgpartition(I)
 x1 = fork(equality, toindices, backdrop)
 x2 = sfilter(x0, x1)
 x3 = argmax(x2, size)
 x4 = other(x0, x3)
 x5 = color(x4)
 x6 = toindices(x4)
 x7 = outbox(x3)
 x8 = lbind(argmin, x7)
 x9 = lbind(lbind, manhattan)
 x10 = rbind(compose, initset)
 x11 = chain(x8, x10, x9)
 x12 = compose(x11, initset)
 x13 = apply(x12, x6)
 x14 = cover(I, x4)
 x15 = fill(x14, x5, x13)
 return x15
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]