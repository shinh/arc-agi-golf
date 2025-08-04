def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
T = True
def toivec(
 i
):
 return (i, 0)
NEG_ONE = -1
def tojvec(
 j
):
 return (0, j)
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
def frontiers(
 grid
):
 h, w = len(grid), len(grid[0])
 row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
 column_indices = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
 hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
 vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
 return hfrontiers | vfrontiers
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
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
def hline(
 patch
):
 return width(patch) == len(patch) and height(patch) == 1
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
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
def crement(
 x
):
 if isinstance(x, int):
  return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
 return (
  0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),
  0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
 )
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
def leastcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def vmatching(
 a,
 b
):
 return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0
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
def gravitate(
 source,
 destination
):
 source_i, source_j = center(source)
 destination_i, destination_j = center(destination)
 i, j = 0, 0
 if vmatching(source, destination):
  i = 1 if source_i < destination_i else -1
 else:
  j = 1 if source_j < destination_j else -1
 direction = (i, j)
 gravitation_i, gravitation_j = i, j
 maxcount = 42
 c = 0
 while not adjacent(source, destination) and c < maxcount:
  c += 1
  gravitation_i += i
  gravitation_j += j
  source = shift(source, direction)
 return (gravitation_i - i, gravitation_j - j)
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
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
def size(
 container
):
 return len(container)
def positive(
 x
):
 return x > 0
def hfrontier(
 location
):
 return frozenset((location[0], j) for j in range(30))
def colorfilter(
 objs,
 value
):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
def vfrontier(
 location
):
 return frozenset((i, location[1]) for i in range(30))
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
def contained(
 value,
 container
):
 return value in container
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
F = False
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
def verify_task379(I):
 x0 = leastcolor(I)
 x1 = objects(I, T, F, T)
 x2 = merge(x1)
 x3 = palette(x2)
 x4 = other(x3, x0)
 x5 = ofcolor(I, x0)
 x6 = frontiers(I)
 x7 = colorfilter(x6, x4)
 x8 = sfilter(x7, hline)
 x9 = size(x8)
 x10 = positive(x9)
 x11 = height(I)
 x12 = toivec(x11)
 x13 = hfrontier(x12)
 x14 = toivec(NEG_ONE)
 x15 = hfrontier(x14)
 x16 = insert(x15, x7)
 x17 = insert(x13, x16)
 x18 = width(I)
 x19 = tojvec(x18)
 x20 = vfrontier(x19)
 x21 = tojvec(NEG_ONE)
 x22 = vfrontier(x21)
 x23 = insert(x22, x7)
 x24 = insert(x20, x23)
 x25 = branch(x10, x17, x24)
 x26 = lbind(argmin, x25)
 x27 = lbind(rbind, manhattan)
 x28 = compose(x27, initset)
 x29 = compose(x26, x28)
 x30 = rbind(remove, x25)
 x31 = compose(x30, x29)
 x32 = fork(argmin, x31, x28)
 x33 = fork(gravitate, initset, x29)
 x34 = compose(crement, x33)
 x35 = fork(add, identity, x34)
 x36 = fork(gravitate, initset, x32)
 x37 = compose(crement, x36)
 x38 = fork(add, identity, x37)
 x39 = ofcolor(I, x4)
 x40 = backdrop(x39)
 x41 = fork(connect, x35, x38)
 x42 = rbind(contained, x40)
 x43 = rbind(extract, x42)
 x44 = fork(astuple, x35, x38)
 x45 = compose(x43, x44)
 x46 = fork(connect, identity, x45)
 x47 = rbind(branch, x46)
 x48 = rbind(x47, x41)
 x49 = rbind(contained, x40)
 x50 = compose(x48, x49)
 x51 = compose(initset, x50)
 x52 = fork(rapply, x51, identity)
 x53 = compose(first, x52)
 x54 = mapply(x53, x5)
 x55 = fill(I, x0, x54)
 x56 = intersection(x39, x54)
 x57 = mapply(neighbors, x56)
 x58 = fill(x55, x4, x57)
 return x58
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]