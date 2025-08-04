FOUR = 4
ONE = 1
SIX = 6
THREE = 3
TWO = 2
TWO_BY_TWO = (2, 2)
UP = (-1, 0)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def astuple(
 a,
 b
):
 return (a, b)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
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
def contained(
 value,
 container
):
 return value in container
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
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
def fill(
 grid,
 value,
 patch
):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(
 container
):
 return next(iter(container))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def identity(
 x
):
 return x
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def initset(
 value
):
 return frozenset({value})
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def intersection(
 a,
 b
):
 return a & b
def last(
 container
):
 return max(enumerate(container))[1]
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
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def positive(
 x
):
 return x > 0
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def shoot(
 start,
 direction
):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def size(
 container
):
 return len(container)
def toivec(
 i
):
 return (i, 0)
def tojvec(
 j
):
 return (0, j)
def valmax(
 container,
 compfunc
):
 return compfunc(max(container, key=compfunc, default=0))
def verify_task165(I):
 x0 = astuple(ONE, THREE)
 x1 = astuple(TWO, FOUR)
 x2 = initset(x1)
 x3 = insert(TWO_BY_TWO, x2)
 x4 = insert(x0, x3)
 x5 = tojvec(THREE)
 x6 = toivec(THREE)
 x7 = connect(x5, x6)
 x8 = astuple(THREE, SIX)
 x9 = connect(x5, x8)
 x10 = combine(x7, x9)
 x11 = combine(x4, x10)
 x12 = lbind(contained, x11)
 x13 = compose(normalize, toindices)
 x14 = lbind(apply, x13)
 x15 = chain(x12, x14, partition)
 x16 = astuple(identity, identity)
 x17 = astuple(rot90, rot270)
 x18 = astuple(x16, x17)
 x19 = astuple(rot180, rot180)
 x20 = astuple(rot270, rot90)
 x21 = astuple(x19, x20)
 x22 = combine(x18, x21)
 x23 = rbind(rapply, I)
 x24 = compose(initset, first)
 x25 = chain(first, x23, x24)
 x26 = compose(x15, x25)
 x27 = extract(x22, x26)
 x28 = first(x27)
 x29 = last(x27)
 x30 = x28(I)
 x31 = palette(I)
 x32 = lbind(ofcolor, x30)
 x33 = compose(normalize, x32)
 x34 = matcher(x33, x11)
 x35 = extract(x31, x34)
 x36 = remove(x35, x31)
 x37 = lbind(colorcount, x30)
 x38 = argmin(x36, x37)
 x39 = ofcolor(x30, x38)
 x40 = ofcolor(x30, x35)
 x41 = compose(positive, size)
 x42 = rbind(intersection, x40)
 x43 = rbind(shoot, UP)
 x44 = chain(x41, x42, x43)
 x45 = sfilter(x39, x44)
 x46 = height(x30)
 x47 = rbind(valmax, first)
 x48 = lbind(sfilter, x40)
 x49 = lbind(matcher, last)
 x50 = chain(x48, x49, last)
 x51 = chain(increment, x47, x50)
 x52 = fork(astuple, x51, last)
 x53 = decrement(x46)
 x54 = lbind(astuple, x53)
 x55 = compose(x54, last)
 x56 = fork(connect, x52, x55)
 x57 = mapply(x56, x45)
 x58 = fill(x30, x38, x57)
 x59 = x29(x58)
 return x59
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]