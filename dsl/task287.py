FOUR = 4
NEG_ONE = -1
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
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
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
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
def maximum(
 container
):
 return max(container, default=0)
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def papply(
 function,
 a,
 b
):
 return tuple(function(i, j) for i, j in zip(a, b))
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def verify_task287(I):
 x0 = replace(I, FOUR, NEG_ONE)
 x1 = dmirror(x0)
 x2 = papply(pair, x0, x1)
 x3 = lbind(apply, maximum)
 x4 = apply(x3, x2)
 x5 = cmirror(x4)
 x6 = papply(pair, x4, x5)
 x7 = apply(x3, x6)
 x8 = hmirror(x7)
 x9 = papply(pair, x7, x8)
 x10 = apply(x3, x9)
 x11 = vmirror(x10)
 x12 = papply(pair, x11, x10)
 x13 = apply(x3, x12)
 return x13
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]