def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def either(
 a,
 b
):
 return a or b
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def vsplit(
 grid,
 n
):
 h, w = len(grid) // n, len(grid[0])
 offset = len(grid) % n != 0
 return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
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
def flip(
 b
):
 return not b
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
FOUR = 4
def both(
 a,
 b
):
 return a and b
def greater(
 a,
 b
):
 return a > b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
THREE = 3
TWO = 2
def verify_task262(I):
 x0 = leastcolor(I)
 x1 = height(I)
 x2 = vsplit(I, x1)
 x3 = rbind(ofcolor, x0)
 x4 = compose(leftmost, x3)
 x5 = width(I)
 x6 = divide(x5, THREE)
 x7 = multiply(x6, TWO)
 x8 = lbind(greater, x6)
 x9 = compose(x8, x4)
 x10 = lbind(greater, x7)
 x11 = compose(x10, x4)
 x12 = compose(flip, x9)
 x13 = fork(both, x11, x12)
 x14 = fork(either, x9, x13)
 x15 = compose(flip, x14)
 x16 = rbind(multiply, TWO)
 x17 = compose(x16, x9)
 x18 = rbind(multiply, FOUR)
 x19 = compose(x18, x13)
 x20 = rbind(multiply, THREE)
 x21 = compose(x20, x15)
 x22 = fork(add, x17, x19)
 x23 = fork(add, x22, x21)
 x24 = width(I)
 x25 = rbind(repeat, x24)
 x26 = compose(x25, x23)
 x27 = apply(x26, x2)
 return x27
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]