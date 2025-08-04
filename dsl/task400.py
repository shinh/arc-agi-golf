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
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
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
def cmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
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
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def initset(
 value
):
 return frozenset({value})
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def first(
 container
):
 return next(iter(container))
def equality(
 a,
 b
):
 return a == b
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
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task400(I):
 x0 = palette(I)
 x1 = lbind(rbind, sfilter)
 x2 = lbind(compose, flip)
 x3 = lbind(matcher, first)
 x4 = chain(x1, x2, x3)
 x5 = lbind(paint, I)
 x6 = rbind(compose, asobject)
 x7 = dmirror(I)
 x8 = rbind(rapply, x7)
 x9 = chain(first, x8, initset)
 x10 = chain(x9, x6, x4)
 x11 = compose(x5, x10)
 x12 = compose(x6, x4)
 x13 = compose(cmirror, x11)
 x14 = compose(initset, x12)
 x15 = fork(rapply, x14, x13)
 x16 = compose(first, x15)
 x17 = fork(paint, x11, x16)
 x18 = chain(initset, x6, x4)
 x19 = compose(hmirror, x17)
 x20 = fork(rapply, x18, x19)
 x21 = compose(first, x20)
 x22 = fork(paint, x17, x21)
 x23 = chain(initset, x6, x4)
 x24 = compose(vmirror, x22)
 x25 = fork(rapply, x23, x24)
 x26 = compose(first, x25)
 x27 = fork(paint, x22, x26)
 x28 = fork(equality, identity, hmirror)
 x29 = fork(equality, identity, vmirror)
 x30 = fork(equality, identity, cmirror)
 x31 = fork(equality, identity, dmirror)
 x32 = fork(both, x28, x29)
 x33 = fork(both, x30, x31)
 x34 = fork(both, x32, x33)
 x35 = compose(x34, x27)
 x36 = sfilter(x0, x35)
 x37 = lbind(colorcount, I)
 x38 = argmin(x36, x37)
 x39 = x27(x38)
 x40 = ofcolor(I, x38)
 x41 = subgrid(x40, x39)
 return x41
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]