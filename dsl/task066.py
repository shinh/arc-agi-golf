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
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
T = True
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def mfilter(
 container,
 function
):
 return merge(sfilter(container, function))
def first(
 container
):
 return next(iter(container))
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
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def either(
 a,
 b
):
 return a or b
ONE = 1
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
def equality(
 a,
 b
):
 return a == b
LEFT = (0, -1)
def last(
 container
):
 return max(enumerate(container))[1]
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
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
def ineighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def neighbors(
 loc
):
 return dneighbors(loc) | ineighbors(loc)
def objects(
 grid,
 univalued,
 diagonal,
 without_bg
):
 bg = mostcolor(grid) if without_bg else None
 objs = set()
 occupied = set()
 h, w = len(grid), len(grid[0])
 unvisited = asindices(grid)
 diagfun = neighbors if diagonal else dneighbors
 for loc in unvisited:
  if loc in occupied:
   continue
  val = grid[loc[0]][loc[1]]
  if val == bg:
   continue
  obj = {(val, loc)}
  cands = {loc}
  while len(cands) > 0:
   neighborhood = set()
   for cand in cands:
    v = grid[cand[0]][cand[1]]
    if (val == v) if univalued else (v != bg):
     obj.add((v, cand))
     occupied.add(cand)
     neighborhood |= {
      (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
     }
   cands = neighborhood - occupied
  objs.add(frozenset(obj))
 return frozenset(objs)
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def corners(
 patch
):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
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
UP = (-1, 0)
def both(
 a,
 b
):
 return a and b
def hfrontier(
 location
):
 return frozenset((location[0], j) for j in range(30))
RIGHT = (0, 1)
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def identity(
 x
):
 return x
def manhattan(
 a,
 b
):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def adjacent(
 a,
 b
):
 return manhattan(a, b) == 1
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
TWO = 2
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
THREE = 3
DOWN = (1, 0)
F = False
def vline(
 patch
):
 return height(patch) == len(patch) and width(patch) == 1
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
def verify_task066(I):
 x0 = ofcolor(I, TWO)
 x1 = vline(x0)
 x2 = branch(x1, dmirror, identity)
 x3 = x2(I)
 x4 = ofcolor(x3, THREE)
 x5 = ofcolor(x3, TWO)
 x6 = center(x4)
 x7 = hfrontier(x6)
 x8 = center(x5)
 x9 = hfrontier(x8)
 x10 = mostcolor(I)
 x11 = palette(I)
 x12 = remove(THREE, x11)
 x13 = remove(TWO, x12)
 x14 = other(x13, x10)
 x15 = replace(x3, THREE, x10)
 x16 = difference(x7, x4)
 x17 = underfill(x15, THREE, x16)
 x18 = replace(x3, TWO, x10)
 x19 = difference(x9, x5)
 x20 = underfill(x18, TWO, x19)
 x21 = objects(x17, T, F, F)
 x22 = colorfilter(x21, THREE)
 x23 = rbind(adjacent, x4)
 x24 = sfilter(x22, x23)
 x25 = objects(x20, T, F, F)
 x26 = colorfilter(x25, TWO)
 x27 = rbind(adjacent, x5)
 x28 = sfilter(x26, x27)
 x29 = mapply(toindices, x24)
 x30 = rbind(equality, x14)
 x31 = lbind(index, x3)
 x32 = compose(x30, x31)
 x33 = rbind(add, LEFT)
 x34 = compose(x32, x33)
 x35 = rbind(add, RIGHT)
 x36 = compose(x32, x35)
 x37 = fork(either, x34, x36)
 x38 = rbind(add, UP)
 x39 = compose(x32, x38)
 x40 = rbind(add, DOWN)
 x41 = compose(x32, x40)
 x42 = fork(either, x39, x41)
 x43 = sfilter(x29, x37)
 x44 = mapply(toindices, x28)
 x45 = sfilter(x44, x42)
 x46 = fork(connect, first, last)
 x47 = product(x43, x45)
 x48 = compose(vline, x46)
 x49 = rbind(toobject, x3)
 x50 = chain(numcolors, x49, x46)
 x51 = matcher(x50, ONE)
 x52 = fork(both, x48, x51)
 x53 = extract(x47, x52)
 x54 = x46(x53)
 x55 = center(x4)
 x56 = center(x5)
 x57 = fork(either, hline, vline)
 x58 = lbind(connect, x55)
 x59 = corners(x54)
 x60 = apply(x58, x59)
 x61 = mfilter(x60, x57)
 x62 = lbind(connect, x56)
 x63 = corners(x54)
 x64 = apply(x62, x63)
 x65 = mfilter(x64, x57)
 x66 = combine(x61, x65)
 x67 = combine(x54, x66)
 x68 = fill(x3, THREE, x67)
 x69 = fill(x68, TWO, x5)
 x70 = x2(x69)
 return x70
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]