def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
def index(
 grid,
 loc
):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(
 patch
):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def mostcommon(
 container
):
 return max(set(container), key=container.count)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def lbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def subtract(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
ONE = 1
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def rbind(
 function,
 fixed
):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def astuple(
 a,
 b
):
 return (a, b)
def size(
 container
):
 return len(container)
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def identity(
 x
):
 return x
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def verify_task010(I):
 x0 = first(I)
 x1 = mostcommon(x0)
 x2 = dmirror(I)
 x3 = matcher(identity, x1)
 x4 = rbind(sfilter, x3)
 x5 = compose(size, x4)
 x6 = apply(x5, x2)
 x7 = dedupe(x6)
 x8 = order(x7, identity)
 x9 = size(x8)
 x10 = increment(x9)
 x11 = increment(x10)
 x12 = interval(ONE, x11, ONE)
 x13 = pair(x8, x12)
 x14 = height(I)
 x15 = astuple(x14, x1)
 x16 = repeat(x15, ONE)
 x17 = combine(x16, x13)
 x18 = lbind(extract, x17)
 x19 = lbind(matcher, first)
 x20 = chain(last, x18, x19)
 x21 = compose(x20, x5)
 x22 = fork(subtract, height, x5)
 x23 = fork(repeat, x21, x22)
 x24 = lbind(repeat, x1)
 x25 = compose(x24, x5)
 x26 = fork(combine, x25, x23)
 x27 = apply(x26, x2)
 x28 = dmirror(x27)
 return x28
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]