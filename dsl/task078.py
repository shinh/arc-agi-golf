ONE = 1
TWO = 2
ZERO = 0
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
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def color(
 obj
):
 return next(iter(obj))[0]
def index(
 grid,
 loc
):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
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
def equality(
 a,
 b
):
 return a == b
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
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
def greater(
 a,
 b
):
 return a > b
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
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
def last(
 container
):
 return max(enumerate(container))[1]
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
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
def size(
 container
):
 return len(container)
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def verify_task078(I):
 x0 = first(I)
 x1 = dedupe(x0)
 x2 = size(x1)
 x3 = equality(ONE, x2)
 x4 = branch(x3, dmirror, identity)
 x5 = x4(I)
 x6 = first(x5)
 x7 = first(x6)
 x8 = first(x5)
 x9 = matcher(identity, x7)
 x10 = sfilter(x8, x9)
 x11 = size(x10)
 x12 = last(x5)
 x13 = sfilter(x12, x9)
 x14 = size(x13)
 x15 = greater(x11, x14)
 x16 = branch(x15, hmirror, identity)
 x17 = x16(x5)
 x18 = partition(x17)
 x19 = matcher(color, x7)
 x20 = extract(x18, x19)
 x21 = remove(x20, x18)
 x22 = argmin(x21, uppermost)
 x23 = other(x21, x22)
 x24 = color(x22)
 x25 = color(x23)
 x26 = fill(x17, TWO, x20)
 x27 = fill(x26, ONE, x23)
 x28 = fill(x27, ZERO, x22)
 x29 = rbind(order, identity)
 x30 = dmirror(x28)
 x31 = apply(x29, x30)
 x32 = dmirror(x31)
 x33 = x16(x32)
 x34 = x4(x33)
 x35 = ofcolor(x34, TWO)
 x36 = fill(x34, x7, x35)
 x37 = ofcolor(x34, ONE)
 x38 = fill(x36, x25, x37)
 x39 = ofcolor(x34, ZERO)
 x40 = fill(x38, x24, x39)
 return x40
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]