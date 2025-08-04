def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def tojvec(
 j
):
 return (0, j)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def double(
 n
):
 return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def paint(
 grid,
 obj
):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def last(
 container
):
 return max(enumerate(container))[1]
def first(
 container
):
 return next(iter(container))
def equality(
 a,
 b
):
 return a == b
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
def flip(
 b
):
 return not b
FOUR = 4
def connect(
 a,
 b
):
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
def shoot(
 start,
 direction
):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def both(
 a,
 b
):
 return a and b
RIGHT = (0, 1)
def greater(
 a,
 b
):
 return a > b
def halve(
 n
):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def identity(
 x
):
 return x
def intersection(
 a,
 b
):
 return a & b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
NEG_TWO = -2
def contained(
 value,
 container
):
 return value in container
def shift(
 patch,
 directions
):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def verify_task240(I):
 x0 = hmirror(I)
 x1 = fgpartition(x0)
 x2 = merge(x1)
 x3 = vmirror(I)
 x4 = fgpartition(x3)
 x5 = merge(x4)
 x6 = hmirror(I)
 x7 = vmirror(x6)
 x8 = fgpartition(x7)
 x9 = merge(x8)
 x10 = mostcolor(I)
 x11 = combine(x2, x5)
 x12 = combine(x11, x9)
 x13 = paint(I, x12)
 x14 = compose(increment, first)
 x15 = fork(greater, last, x14)
 x16 = tojvec(NEG_TWO)
 x17 = rbind(shift, x16)
 x18 = compose(x17, vmirror)
 x19 = rbind(sfilter, x15)
 x20 = compose(x19, asindices)
 x21 = compose(x18, x20)
 x22 = fork(intersection, x20, x21)
 x23 = rbind(shoot, RIGHT)
 x24 = compose(x23, last)
 x25 = matcher(first, x10)
 x26 = compose(flip, x25)
 x27 = rbind(sfilter, x26)
 x28 = compose(double, halve)
 x29 = fork(equality, x28, identity)
 x30 = chain(flip, x29, last)
 x31 = lbind(fork, both)
 x32 = rbind(x31, x30)
 x33 = lbind(fork, recolor)
 x34 = lbind(x33, first)
 x35 = rbind(compose, x24)
 x36 = lbind(rbind, contained)
 x37 = lbind(rbind, sfilter)
 x38 = chain(x34, x35, x37)
 x39 = chain(x38, x32, x36)
 x40 = fork(toobject, x22, identity)
 x41 = compose(x27, x40)
 x42 = compose(x39, x22)
 x43 = fork(mapply, x42, x41)
 x44 = fork(paint, identity, x43)
 x45 = compose(rot90, x44)
 x46 = power(x45, FOUR)
 x47 = x46(x13)
 return x47
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]