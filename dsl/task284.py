DOWN = (1, 0)
F = False
NEG_TWO = -2
T = True
UP = (-1, 0)
ZERO = 0
ZERO_BY_TWO = (0, 2)
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def astuple(a,b):
 return (a, b)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def toindices(patch):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def centerofmass(patch):
 return tuple(map(lambda x: sum(x) // len(patch), zip(*toindices(patch))))
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def connect(a,b):
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
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def cover(grid,patch):
 return fill(grid, mostcolor(grid), toindices(patch))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def first(container):
 return next(iter(container))
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def insert(value,container):
 return container.union(frozenset({value}))
def last(container):
 return max(enumerate(container))[1]
def llcorner(patch):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def ineighbors(loc):
 return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def neighbors(loc):
 return dneighbors(loc) | ineighbors(loc)
def objects(grid,univalued,diagonal,without_bg):
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
def order(container,compfunc):
 return tuple(sorted(container, key=compfunc))
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def height(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def portrait(piece):
 return height(piece) > width(piece)
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def verify_task284(I):
 x0 = objects(I, T, F, T)
 x1 = merge(x0)
 x2 = portrait(x1)
 x3 = branch(x2, identity, dmirror)
 x4 = x3(I)
 x5 = objects(x4, T, F, T)
 x6 = order(x5, uppermost)
 x7 = first(x6)
 x8 = last(x6)
 x9 = color(x7)
 x10 = color(x8)
 x11 = compose(first, toindices)
 x12 = x11(x7)
 x13 = x11(x8)
 x14 = connect(x12, x13)
 x15 = centerofmass(x14)
 x16 = connect(x12, x15)
 x17 = fill(x4, x10, x14)
 x18 = fill(x17, x9, x16)
 x19 = add(x15, DOWN)
 x20 = initset(x15)
 x21 = insert(x19, x20)
 x22 = toobject(x21, x18)
 x23 = astuple(ZERO, NEG_TWO)
 x24 = shift(x22, ZERO_BY_TWO)
 x25 = shift(x22, x23)
 x26 = combine(x24, x25)
 x27 = ulcorner(x26)
 x28 = urcorner(x26)
 x29 = connect(x27, x28)
 x30 = shift(x29, UP)
 x31 = llcorner(x26)
 x32 = lrcorner(x26)
 x33 = connect(x31, x32)
 x34 = shift(x33, DOWN)
 x35 = paint(x18, x26)
 x36 = fill(x35, x9, x30)
 x37 = fill(x36, x10, x34)
 x38 = cover(x37, x21)
 x39 = x3(x38)
 return x39
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]