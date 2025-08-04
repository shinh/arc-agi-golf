DOWN_LEFT = (1, -1)
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
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
ONE = 1
def initset(
 value
):
 return frozenset({value})
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
LEFT = (0, -1)
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
ZERO = 0
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
def add(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def astuple(
 a,
 b
):
 return (a, b)
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
def invert(
 n
):
 return -n if isinstance(n, int) else (-n[0], -n[1])
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
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
THREE = 3
UP_RIGHT = (-1, 1)
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
def verify_task256(I):
 x0 = astuple(identity, rot90)
 x1 = astuple(rot180, rot270)
 x2 = combine(x0, x1)
 x3 = astuple(identity, rot270)
 x4 = astuple(rot180, rot90)
 x5 = combine(x3, x4)
 x6 = pair(x2, x5)
 x7 = leastcolor(I)
 x8 = rbind(ofcolor, x7)
 x9 = rbind(rapply, I)
 x10 = chain(first, x9, initset)
 x11 = chain(hline, x8, x10)
 x12 = rbind(ofcolor, x7)
 x13 = rbind(rapply, I)
 x14 = chain(first, x13, initset)
 x15 = chain(leftmost, x12, x14)
 x16 = matcher(x15, ZERO)
 x17 = fork(both, x11, x16)
 x18 = compose(x17, first)
 x19 = extract(x6, x18)
 x20 = first(x19)
 x21 = last(x19)
 x22 = x20(I)
 x23 = ofcolor(x22, x7)
 x24 = argmax(x23, last)
 x25 = add(x24, UP_RIGHT)
 x26 = shoot(x25, UP_RIGHT)
 x27 = add(x24, DOWN_LEFT)
 x28 = shoot(x27, DOWN_LEFT)
 x29 = rbind(shoot, LEFT)
 x30 = mapply(x29, x26)
 x31 = rbind(shoot, LEFT)
 x32 = mapply(x31, x28)
 x33 = width(x22)
 x34 = invert(x33)
 x35 = tojvec(x34)
 x36 = shift(x30, x35)
 x37 = combine(x30, x36)
 x38 = fill(x22, THREE, x37)
 x39 = shift(x32, x35)
 x40 = combine(x32, x39)
 x41 = fill(x38, ONE, x40)
 x42 = x21(x41)
 return x42
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]