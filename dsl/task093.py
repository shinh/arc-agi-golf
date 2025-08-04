def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
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
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
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
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def frontiers(
 grid
):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def last(
 container
):
 return max(enumerate(container))[1]
def equality(
 a,
 b
):
 return a == b
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
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
def shape(
 piece
):
 return (height(piece), width(piece))
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
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
def positive(
 x
):
 return x > 0
def greater(
 a,
 b
):
 return a > b
def identity(
 x
):
 return x
def hconcat(
 a,
 b
):
 return tuple(i + j for i, j in zip(a, b))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def verify_task093(I):
 x0 = frontiers(I)
 x1 = merge(x0)
 x2 = palette(x1)
 x3 = fork(multiply, height, width)
 x4 = lbind(ofcolor, I)
 x5 = compose(x3, x4)
 x6 = argmin(x2, x5)
 x7 = palette(I)
 x8 = remove(x6, x7)
 x9 = lbind(colorcount, I)
 x10 = argmin(x8, x9)
 x11 = ofcolor(I, x6)
 x12 = leftmost(x11)
 x13 = positive(x12)
 x14 = branch(x13, identity, dmirror)
 x15 = x14(I)
 x16 = ofcolor(x15, x6)
 x17 = subgrid(x16, x15)
 x18 = leftmost(x16)
 x19 = rightmost(x16)
 x20 = lbind(greater, x18)
 x21 = compose(x20, last)
 x22 = rbind(greater, x19)
 x23 = compose(x22, last)
 x24 = asindices(x15)
 x25 = sfilter(x24, x21)
 x26 = subgrid(x25, x15)
 x27 = asindices(x15)
 x28 = sfilter(x27, x23)
 x29 = subgrid(x28, x15)
 x30 = rbind(equality, x10)
 x31 = rbind(order, x30)
 x32 = apply(x31, x26)
 x33 = vmirror(x29)
 x34 = apply(x31, x33)
 x35 = vmirror(x34)
 x36 = hconcat(x32, x17)
 x37 = hconcat(x36, x35)
 x38 = x14(x37)
 x39 = replace(x38, x10, x6)
 return x39
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]