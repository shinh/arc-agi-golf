def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def both(
 a,
 b
):
 return a and b
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def color(
 obj
):
 return next(iter(obj))[0]
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
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
def divide(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a // b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] // b[0], a[1] // b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a // b[0], a // b[1])
 return (a[0] // b, a[1] // b)
def either(
 a,
 b
):
 return a or b
def equality(
 a,
 b
):
 return a == b
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
def frontiers(
 grid
):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def width(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def identity(
 x
):
 return x
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
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
def multiply(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
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
def size(
 container
):
 return len(container)
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
def vline(
 patch
):
 return height(patch) == len(patch) and width(patch) == 1
def verify_task314(I):
 x0 = frontiers(I)
 x1 = merge(x0)
 x2 = color(x1)
 x3 = palette(I)
 x4 = remove(x2, x3)
 x5 = lbind(colorcount, I)
 x6 = argmax(x4, x5)
 x7 = remove(x6, x4)
 x8 = height(I)
 x9 = increment(x8)
 x10 = frontiers(I)
 x11 = sfilter(x10, hline)
 x12 = size(x11)
 x13 = increment(x12)
 x14 = divide(x9, x13)
 x15 = width(I)
 x16 = increment(x15)
 x17 = frontiers(I)
 x18 = sfilter(x17, vline)
 x19 = size(x18)
 x20 = increment(x19)
 x21 = divide(x16, x20)
 x22 = rbind(multiply, x14)
 x23 = rbind(divide, x14)
 x24 = compose(x22, x23)
 x25 = fork(equality, identity, x24)
 x26 = rbind(multiply, x21)
 x27 = rbind(divide, x21)
 x28 = compose(x26, x27)
 x29 = fork(equality, identity, x28)
 x30 = lbind(fork, both)
 x31 = rbind(compose, first)
 x32 = lbind(compose, x25)
 x33 = lbind(rbind, subtract)
 x34 = compose(x33, uppermost)
 x35 = chain(x31, x32, x34)
 x36 = rbind(compose, last)
 x37 = lbind(compose, x29)
 x38 = lbind(rbind, subtract)
 x39 = compose(x38, leftmost)
 x40 = chain(x36, x37, x39)
 x41 = fork(x30, x35, x40)
 x42 = fork(sfilter, identity, x41)
 x43 = fork(connect, first, last)
 x44 = lbind(apply, x43)
 x45 = lbind(ofcolor, I)
 x46 = fork(product, x45, x45)
 x47 = fork(either, vline, hline)
 x48 = rbind(sfilter, x47)
 x49 = chain(x48, x44, x46)
 x50 = lbind(mapply, x42)
 x51 = compose(x50, x49)
 x52 = fork(recolor, identity, x51)
 x53 = mapply(x52, x7)
 x54 = paint(I, x53)
 return x54
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]