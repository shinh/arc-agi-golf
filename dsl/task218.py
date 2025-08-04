FOUR = 4
ZERO = 0
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def compose(outer,inner):
 return lambda x: outer(inner(x))
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
def flip(b):
 return not b
def identity(x):
 return x
def matcher(function,target):
 return lambda x: function(x) == target
def positive(x):
 return x > 0
def power(function,n):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
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
def verify_task218(I):
 x0 = matcher(identity, ZERO)
 x1 = compose(flip, x0)
 x2 = rbind(sfilter, x1)
 x3 = chain(positive, size, x2)
 x4 = rbind(sfilter, x3)
 x5 = compose(dmirror, x4)
 x6 = power(x5, FOUR)
 x7 = x6(I)
 x8 = dedupe(x7)
 x9 = dmirror(x8)
 x10 = dedupe(x9)
 x11 = dmirror(x10)
 return x11
def p(g):
 return [list(r)for r in verify_task218(tuple(tuple(r) for r in g))]