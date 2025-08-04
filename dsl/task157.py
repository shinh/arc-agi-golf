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
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
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
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
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
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def cover(
 grid,
 patch
):
 return fill(grid, mostcolor(grid), toindices(patch))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
ONE = 1
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def initset(
 value
):
 return frozenset({value})
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
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
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
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
def both(
 a,
 b
):
 return a and b
def size(
 container
):
 return len(container)
def greater(
 a,
 b
):
 return a > b
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def identity(
 x
):
 return x
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
def color(
 obj
):
 return next(iter(obj))[0]
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
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
DOWN = (1, 0)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task157(I):
 x0 = astuple(identity, dmirror)
 x1 = astuple(cmirror, hmirror)
 x2 = combine(x0, x1)
 x3 = fork(vsplit, identity, height)
 x4 = chain(asobject, first, x3)
 x5 = mostcolor(I)
 x6 = lbind(chain, numcolors)
 x7 = lbind(x6, x4)
 x8 = lbind(chain, color)
 x9 = lbind(x8, x4)
 x10 = rbind(rapply, I)
 x11 = compose(initset, x7)
 x12 = chain(first, x10, x11)
 x13 = rbind(rapply, I)
 x14 = compose(initset, x9)
 x15 = chain(first, x13, x14)
 x16 = matcher(x12, ONE)
 x17 = matcher(x15, x5)
 x18 = compose(flip, x17)
 x19 = fork(both, x16, x18)
 x20 = argmax(x2, x19)
 x21 = x20(I)
 x22 = x4(x21)
 x23 = color(x22)
 x24 = palette(x21)
 x25 = remove(x23, x24)
 x26 = other(x25, x5)
 x27 = objects(x21, T, T, T)
 x28 = colorfilter(x27, x26)
 x29 = ofcolor(x21, x23)
 x30 = ofcolor(x21, x5)
 x31 = mapply(neighbors, x30)
 x32 = mapply(neighbors, x31)
 x33 = lowermost(x29)
 x34 = dneighbors(ORIGIN)
 x35 = remove(DOWN, x34)
 x36 = rbind(mapply, x35)
 x37 = lbind(chain, x36)
 x38 = lbind(lbind, add)
 x39 = rbind(x37, x38)
 x40 = lbind(lbind, compose)
 x41 = lbind(lbind, shift)
 x42 = chain(x39, x40, x41)
 x43 = lbind(chain, size)
 x44 = rbind(intersection, x29)
 x45 = lbind(x43, x44)
 x46 = rbind(matcher, ZERO)
 x47 = lbind(lbind, shift)
 x48 = chain(x46, x45, x47)
 x49 = rbind(chain, first)
 x50 = rbind(x49, decrement)
 x51 = lbind(greater, x33)
 x52 = x50(x51)
 x53 = rbind(sfilter, x52)
 x54 = lbind(compose, x53)
 x55 = lbind(chain, size)
 x56 = rbind(difference, x30)
 x57 = lbind(x55, x56)
 x58 = rbind(matcher, ZERO)
 x59 = lbind(lbind, shift)
 x60 = chain(x58, x57, x59)
 x61 = lbind(chain, size)
 x62 = rbind(intersection, x30)
 x63 = lbind(x61, x62)
 x64 = lbind(fork, difference)
 x65 = compose(x54, x42)
 x66 = lbind(lbind, shift)
 x67 = fork(x64, x65, x66)
 x68 = compose(x63, x67)
 x69 = rbind(matcher, ZERO)
 x70 = compose(x69, x68)
 x71 = lbind(fork, both)
 x72 = fork(x71, x70, x60)
 x73 = lbind(fork, both)
 x74 = fork(x73, x48, x72)
 x75 = compose(normalize, toindices)
 x76 = lbind(sfilter, x32)
 x77 = chain(x76, x74, x75)
 x78 = rbind(argmin, first)
 x79 = compose(x78, x77)
 x80 = fork(shift, x75, x79)
 x81 = mapply(x80, x28)
 x82 = merge(x28)
 x83 = cover(x21, x82)
 x84 = fill(x83, ONE, x81)
 x85 = x20(x84)
 return x85
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]