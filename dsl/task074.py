ORIGIN = (0, 0)
TWO_BY_TWO = (2, 2)
TWO_BY_ZERO = (2, 0)
ZERO_BY_TWO = (0, 2)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def cmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def equality(
 a,
 b
):
 return a == b
def first(
 container
):
 return next(iter(container))
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
def initset(
 value
):
 return frozenset({value})
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
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
def verify_task074(I):
 x0 = lbind(compose, flip)
 x1 = lbind(matcher, first)
 x2 = compose(x0, x1)
 x3 = rbind(compose, asobject)
 x4 = lbind(rbind, sfilter)
 x5 = chain(x3, x4, x2)
 x6 = rbind(shift, ORIGIN)
 x7 = compose(x6, dmirror)
 x8 = rbind(shift, TWO_BY_TWO)
 x9 = compose(x8, cmirror)
 x10 = rbind(shift, TWO_BY_ZERO)
 x11 = compose(x10, hmirror)
 x12 = rbind(shift, ZERO_BY_TWO)
 x13 = compose(x12, vmirror)
 x14 = lbind(fork, paint)
 x15 = lbind(x14, identity)
 x16 = lbind(compose, x7)
 x17 = chain(x15, x16, x5)
 x18 = lbind(compose, x9)
 x19 = chain(x15, x18, x5)
 x20 = lbind(compose, x11)
 x21 = chain(x15, x20, x5)
 x22 = lbind(compose, x13)
 x23 = chain(x15, x22, x5)
 x24 = rbind(rapply, I)
 x25 = chain(first, x24, initset)
 x26 = fork(compose, x23, x21)
 x27 = fork(compose, x19, x17)
 x28 = fork(compose, x26, x27)
 x29 = compose(x25, x28)
 x30 = palette(I)
 x31 = fork(equality, identity, dmirror)
 x32 = compose(x31, x29)
 x33 = argmax(x30, x32)
 x34 = x29(x33)
 return x34
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]