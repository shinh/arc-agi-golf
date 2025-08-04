def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
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
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
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
F = False
def occurrences(
 grid,
 obj
):
 occurrences = set()
 normed = normalize(obj)
 h, w = len(grid), len(grid[0])
 for i in range(h):
  for j in range(w):
   occurs = True
   for v, (a, b) in shift(normed, (i, j)):
    if 0 <= a < h and 0 <= b < w:
     if grid[a][b] != v:
      occurs = False
      break
    else:
     occurs = False
     break
   if occurs:
    occurrences.add((i, j))
 return frozenset(occurrences)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
ONE = 1
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
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def equality(
 a,
 b
):
 return a == b
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
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
def invert(
 n
):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def contained(
 value,
 container
):
 return value in container
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
def verify_task076(I):
 x0 = objects(I, F, T, T)
 x1 = argmax(x0, size)
 x2 = remove(x1, x0)
 x3 = merge(x2)
 x4 = palette(x3)
 x5 = repeat(identity, ONE)
 x6 = astuple(cmirror, dmirror)
 x7 = astuple(vmirror, hmirror)
 x8 = combine(x6, x7)
 x9 = combine(x5, x8)
 x10 = fork(compose, first, last)
 x11 = product(x9, x9)
 x12 = apply(x10, x11)
 x13 = rbind(contained, x4)
 x14 = compose(x13, first)
 x15 = rbind(sfilter, x14)
 x16 = lbind(chain, ulcorner)
 x17 = lbind(x16, x15)
 x18 = lbind(fork, shift)
 x19 = lbind(lbind, shift)
 x20 = lbind(occurrences, I)
 x21 = rbind(rapply, x1)
 x22 = chain(first, x21, initset)
 x23 = lbind(compose, invert)
 x24 = compose(x23, x17)
 x25 = lbind(compose, x15)
 x26 = fork(x18, x25, x24)
 x27 = compose(x22, x26)
 x28 = rbind(rapply, x1)
 x29 = chain(first, x28, initset)
 x30 = rbind(rapply, x1)
 x31 = compose(initset, x17)
 x32 = chain(first, x30, x31)
 x33 = compose(invert, x32)
 x34 = fork(shift, x29, x33)
 x35 = compose(x19, x34)
 x36 = compose(x20, x27)
 x37 = fork(mapply, x35, x36)
 x38 = rbind(astuple, x37)
 x39 = compose(last, x38)
 x40 = rbind(astuple, x12)
 x41 = compose(last, x40)
 x42 = fork(mapply, x39, x41)
 x43 = fork(paint, identity, x42)
 x44 = rbind(contained, x4)
 x45 = compose(x44, first)
 x46 = sfilter(x1, x45)
 x47 = size(x46)
 x48 = equality(x47, ZERO)
 x49 = branch(x48, identity, x43)
 x50 = x49(I)
 return x50
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]