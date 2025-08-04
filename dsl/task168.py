T = True
DOWN_LEFT = (1, -1)
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
UNITY = (1, 1)
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
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
NEG_UNITY = (-1, -1)
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
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
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
F = False
UP_RIGHT = (-1, 1)
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def verify_task168(I):
 x0 = objects(I, T, F, T)
 x1 = rbind(shoot, UNITY)
 x2 = rbind(add, UNITY)
 x3 = chain(x1, x2, lrcorner)
 x4 = fork(recolor, color, x3)
 x5 = rbind(shoot, UP_RIGHT)
 x6 = rbind(add, UP_RIGHT)
 x7 = chain(x5, x6, urcorner)
 x8 = fork(recolor, color, x7)
 x9 = rbind(shoot, NEG_UNITY)
 x10 = rbind(add, NEG_UNITY)
 x11 = chain(x9, x10, ulcorner)
 x12 = fork(recolor, color, x11)
 x13 = rbind(shoot, DOWN_LEFT)
 x14 = rbind(add, DOWN_LEFT)
 x15 = chain(x13, x14, llcorner)
 x16 = fork(recolor, color, x15)
 x17 = fork(remove, lrcorner, toindices)
 x18 = fork(equality, toindices, x17)
 x19 = sfilter(x0, x18)
 x20 = fork(remove, urcorner, toindices)
 x21 = fork(equality, toindices, x20)
 x22 = sfilter(x0, x21)
 x23 = fork(remove, ulcorner, toindices)
 x24 = fork(equality, toindices, x23)
 x25 = sfilter(x0, x24)
 x26 = fork(remove, llcorner, toindices)
 x27 = fork(equality, toindices, x26)
 x28 = sfilter(x0, x27)
 x29 = mapply(x4, x19)
 x30 = mapply(x8, x22)
 x31 = combine(x29, x30)
 x32 = mapply(x12, x25)
 x33 = mapply(x16, x28)
 x34 = combine(x32, x33)
 x35 = combine(x31, x34)
 x36 = paint(I, x35)
 return x36
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]