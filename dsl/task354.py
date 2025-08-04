def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
T = True
def toivec(
 i
):
 return (i, 0)
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
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def tojvec(
 j
):
 return (0, j)
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
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
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
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
def hmatching(
 a,
 b
):
 return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
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
def vmatching(
 a,
 b
):
 return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def box(
 patch
):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def either(
 a,
 b
):
 return a or b
ONE = 1
TEN = 10
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
def initset(
 value
):
 return frozenset({value})
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
def last(
 container
):
 return max(enumerate(container))[1]
def first(
 container
):
 return next(iter(container))
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def flip(
 b
):
 return not b
ORIGIN = (0, 0)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def astuple(
 a,
 b
):
 return (a, b)
def size(
 container
):
 return len(container)
def sizefilter(
 container,
 n
):
 return frozenset(item for item in container if len(item) == n)
def intersection(
 a,
 b
):
 return a & b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def color(
 obj
):
 return next(iter(obj))[0]
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
F = False
def verify_task354(I):
 x0 = width(I)
 x1 = decrement(x0)
 x2 = tojvec(x1)
 x3 = connect(ORIGIN, x2)
 x4 = height(I)
 x5 = decrement(x4)
 x6 = toivec(x5)
 x7 = connect(ORIGIN, x6)
 x8 = width(I)
 x9 = decrement(x8)
 x10 = tojvec(x9)
 x11 = shape(I)
 x12 = decrement(x11)
 x13 = connect(x10, x12)
 x14 = height(I)
 x15 = decrement(x14)
 x16 = toivec(x15)
 x17 = shape(I)
 x18 = decrement(x17)
 x19 = connect(x16, x18)
 x20 = asindices(I)
 x21 = box(x20)
 x22 = toobject(x21, I)
 x23 = mostcolor(x22)
 x24 = matcher(color, x23)
 x25 = compose(flip, x24)
 x26 = rbind(sfilter, x25)
 x27 = rbind(sizefilter, ONE)
 x28 = rbind(objects, F)
 x29 = rbind(x28, F)
 x30 = rbind(x29, T)
 x31 = rbind(subgrid, I)
 x32 = chain(x26, x30, x31)
 x33 = chain(size, x27, x32)
 x34 = astuple(x3, x7)
 x35 = astuple(x13, x19)
 x36 = combine(x34, x35)
 x37 = argmax(x36, x33)
 x38 = rbind(toobject, I)
 x39 = compose(x38, initset)
 x40 = ofcolor(I, x23)
 x41 = difference(x37, x40)
 x42 = apply(x39, x41)
 x43 = rbind(intersection, x37)
 x44 = chain(size, x43, toindices)
 x45 = matcher(x44, ZERO)
 x46 = objects(I, T, F, T)
 x47 = sfilter(x46, x45)
 x48 = lbind(fork, either)
 x49 = lbind(lbind, hmatching)
 x50 = lbind(lbind, vmatching)
 x51 = fork(x48, x49, x50)
 x52 = lbind(chain, size)
 x53 = rbind(x52, x51)
 x54 = lbind(lbind, sfilter)
 x55 = compose(last, last)
 x56 = chain(x53, x54, x55)
 x57 = rbind(compose, x51)
 x58 = lbind(lbind, extract)
 x59 = compose(last, last)
 x60 = chain(x57, x58, x59)
 x61 = compose(first, last)
 x62 = rbind(matcher, ONE)
 x63 = compose(x62, x56)
 x64 = fork(sfilter, x61, x63)
 x65 = lbind(fork, recolor)
 x66 = lbind(x65, color)
 x67 = compose(x66, x60)
 x68 = fork(mapply, x67, x64)
 x69 = fork(combine, first, x68)
 x70 = compose(first, last)
 x71 = fork(difference, x70, x64)
 x72 = compose(last, last)
 x73 = fork(apply, x60, x64)
 x74 = fork(difference, x72, x73)
 x75 = fork(astuple, x71, x74)
 x76 = fork(astuple, x69, x75)
 x77 = difference(x42, x42)
 x78 = power(x76, TEN)
 x79 = astuple(x42, x47)
 x80 = astuple(x77, x79)
 x81 = x78(x80)
 x82 = first(x81)
 x83 = paint(I, x82)
 return x83
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]