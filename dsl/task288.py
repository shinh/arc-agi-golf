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
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def underfill(
 grid,
 value,
 patch
):
 h, w = len(grid), len(grid[0])
 bg = mostcolor(grid)
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   if grid_filled[i][j] == bg:
    grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
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
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def initset(
 value
):
 return frozenset({value})
NEG_UNITY = (-1, -1)
def first(
 container
):
 return next(iter(container))
def equality(
 a,
 b
):
 return a == b
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
def astuple(
 a,
 b
):
 return (a, b)
UP = (-1, 0)
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
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
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
UP_RIGHT = (-1, 1)
def verify_task288(I):
 x0 = leastcolor(I)
 x1 = astuple(dmirror, cmirror)
 x2 = astuple(hmirror, identity)
 x3 = combine(x1, x2)
 x4 = rbind(rapply, I)
 x5 = chain(first, x4, initset)
 x6 = rbind(ofcolor, x0)
 x7 = chain(lowermost, x6, x5)
 x8 = chain(decrement, height, x5)
 x9 = fork(equality, x7, x8)
 x10 = extract(x3, x9)
 x11 = x10(I)
 x12 = ofcolor(x11, x0)
 x13 = shift(x12, UP)
 x14 = ulcorner(x13)
 x15 = urcorner(x13)
 x16 = shoot(x14, NEG_UNITY)
 x17 = shoot(x15, UP_RIGHT)
 x18 = combine(x16, x17)
 x19 = underfill(x11, x0, x18)
 x20 = x10(x19)
 return x20
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]