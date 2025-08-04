F = False
ONE = 1
T = True
TWO = 2
UNITY = (1, 1)
UP = (-1, 0)
def apply(function,container):
 return type(container)(function(e) for e in container)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(a,b):
 return (a, b)
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
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def box(patch):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def colorfilter(objs,value):
 return frozenset(obj for obj in objs if next(iter(obj))[0] == value)
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
def dedupe(iterable):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def extract(container,condition):
 return next(e for e in container if condition(e))
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def greater(a,b):
 return a > b
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def last(container):
 return max(enumerate(container))[1]
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def mfilter(container,function):
 return merge(sfilter(container, function))
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(element):
 return len(palette(element))
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
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
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def prapply(function,a,b):
 return frozenset(function(i, j) for j in b for i in a)
def rapply(functions,value):
 return type(functions)(function(value) for function in functions)
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def rot180(grid):
 return tuple(tuple(row[::-1]) for row in grid[::-1])
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def shoot(start,direction):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def size(container):
 return len(container)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def trim(grid):
 return tuple(r[1:-1] for r in grid[1:-1])
def underfill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 bg = mostcolor(grid)
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   if grid_filled[i][j] == bg:
    grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def vfrontier(location):
 return frozenset((i, location[1]) for i in range(30))
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
def vline(patch):
 return height(patch) == len(patch) and width(patch) == 1
def verify_task345(I):
 x0 = astuple(identity, identity)
 x1 = astuple(rot90, rot270)
 x2 = astuple(x0, x1)
 x3 = astuple(rot180, rot180)
 x4 = astuple(rot270, rot90)
 x5 = astuple(x3, x4)
 x6 = combine(x2, x5)
 x7 = rbind(greater, ONE)
 x8 = chain(size, dedupe, last)
 x9 = compose(x7, x8)
 x10 = rbind(rapply, I)
 x11 = compose(initset, first)
 x12 = chain(first, x10, x11)
 x13 = compose(x9, x12)
 x14 = extract(x6, x13)
 x15 = first(x14)
 x16 = last(x14)
 x17 = x15(I)
 x18 = mostcolor(I)
 x19 = trim(I)
 x20 = palette(x19)
 x21 = other(x20, x18)
 x22 = asindices(I)
 x23 = box(x22)
 x24 = toobject(x23, I)
 x25 = palette(x24)
 x26 = other(x25, x18)
 x27 = ofcolor(x17, x26)
 x28 = ofcolor(x17, x21)
 x29 = prapply(connect, x27, x28)
 x30 = mfilter(x29, vline)
 x31 = underfill(x17, x26, x30)
 x32 = matcher(numcolors, TWO)
 x33 = objects(x31, F, F, T)
 x34 = sfilter(x33, x32)
 x35 = difference(x33, x34)
 x36 = colorfilter(x35, x26)
 x37 = mapply(toindices, x36)
 x38 = apply(urcorner, x34)
 x39 = shift(x38, UNITY)
 x40 = rbind(shoot, UP)
 x41 = mapply(x40, x39)
 x42 = fill(x31, x26, x41)
 x43 = mapply(vfrontier, x37)
 x44 = fill(x42, x26, x43)
 x45 = x16(x44)
 return x45
def p(g):
 return [list(r)for r in verify_task345(tuple(tuple(r) for r in g))]