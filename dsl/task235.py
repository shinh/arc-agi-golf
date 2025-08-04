DOWN = (1, 0)
EIGHT = 8
FIVE = 5
FOUR = 4
NEG_ONE = -1
ONE = 1
THREE = 3
TWO = 2
ZERO = 0
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(
 a,
 b
):
 return (a, b)
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def flip(
 b
):
 return not b
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(
 x
):
 return x
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(
 element
):
 return len(palette(element))
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
def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
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
def tojvec(
 j
):
 return (0, j)
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
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
def verify_task235(I):
 x0 = width(I)
 x1 = increment(x0)
 x2 = divide(x1, FIVE)
 x3 = astuple(FOUR, FOUR)
 x4 = canvas(NEG_ONE, x3)
 x5 = asindices(x4)
 x6 = rbind(toobject, I)
 x7 = lbind(shift, x5)
 x8 = compose(x6, x7)
 x9 = multiply(x2, FIVE)
 x10 = interval(ZERO, x9, FIVE)
 x11 = apply(tojvec, x10)
 x12 = apply(x8, x11)
 x13 = matcher(numcolors, ONE)
 x14 = fork(equality, identity, hmirror)
 x15 = compose(flip, x14)
 x16 = lbind(index, I)
 x17 = compose(x16, ulcorner)
 x18 = lbind(add, DOWN)
 x19 = chain(x16, x18, ulcorner)
 x20 = fork(equality, x17, x19)
 x21 = compose(flip, x20)
 x22 = fork(either, x13, x15)
 x23 = fork(either, x22, x21)
 x24 = compose(flip, x23)
 x25 = lbind(multiply, TWO)
 x26 = compose(x25, x13)
 x27 = lbind(multiply, FOUR)
 x28 = compose(x27, x15)
 x29 = fork(add, x26, x28)
 x30 = lbind(multiply, THREE)
 x31 = compose(x30, x21)
 x32 = lbind(multiply, EIGHT)
 x33 = compose(x32, x24)
 x34 = fork(add, x31, x33)
 x35 = fork(add, x29, x34)
 x36 = apply(x35, x12)
 x37 = rbind(repeat, x2)
 x38 = apply(x37, x36)
 return x38
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]