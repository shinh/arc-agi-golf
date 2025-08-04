DOWN = (1, 0)
EIGHT = 8
FIVE = 5
FOUR = 4
LEFT = (0, -1)
ONE = 1
RIGHT = (0, 1)
T = True
TWO = 2
UP = (-1, 0)
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def apply(function,container):
 return type(container)(function(e) for e in container)
def both(a,b):
 return a and b
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
def center(patch):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
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
def contained(value,container):
 return value in container
def either(a,b):
 return a or b
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def halve(n):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def hline(patch):
 return width(patch) == len(patch) and height(patch) == 1
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def intersection(a,b):
 return a & b
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def leastcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return min(set(values), key=values.count)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def maximum(container):
 return max(container, default=0)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def dneighbors(loc):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def power(function,n):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
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
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
def replace(grid,replacee,replacer):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shape(piece):
 return (height(piece), width(piece))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def size(container):
 return len(container)
def toivec(i):
 return (i, 0)
def tojvec(j):
 return (0, j)
def vline(patch):
 return height(patch) == len(patch) and width(patch) == 1
def verify_task118(I):
 x0 = leastcolor(I)
 x1 = ofcolor(I, x0)
 x2 = interval(TWO, FIVE, ONE)
 x3 = rbind(shift, RIGHT)
 x4 = rbind(shift, LEFT)
 x5 = rbind(shift, UP)
 x6 = rbind(shift, DOWN)
 x7 = lbind(fork, intersection)
 x8 = lbind(x7, identity)
 x9 = lbind(rbind, shift)
 x10 = compose(x8, x9)
 x11 = compose(x10, tojvec)
 x12 = chain(x10, tojvec, invert)
 x13 = compose(x10, toivec)
 x14 = chain(x10, toivec, invert)
 x15 = lbind(compose, initset)
 x16 = lbind(rbind, rapply)
 x17 = lbind(chain, first)
 x18 = lbind(compose, x4)
 x19 = x15(x11)
 x20 = rbind(x17, x19)
 x21 = chain(x18, x20, x16)
 x22 = lbind(compose, x3)
 x23 = x15(x12)
 x24 = rbind(x17, x23)
 x25 = chain(x22, x24, x16)
 x26 = lbind(compose, x5)
 x27 = x15(x13)
 x28 = rbind(x17, x27)
 x29 = chain(x26, x28, x16)
 x30 = lbind(compose, x6)
 x31 = x15(x14)
 x32 = rbind(x17, x31)
 x33 = chain(x30, x32, x16)
 x34 = rbind(ofcolor, x0)
 x35 = compose(x21, x34)
 x36 = compose(x25, x34)
 x37 = compose(x29, x34)
 x38 = compose(x33, x34)
 x39 = lbind(fork, combine)
 x40 = fork(x39, x35, x36)
 x41 = fork(x39, x37, x38)
 x42 = fork(x39, x40, x41)
 x43 = lbind(recolor, x0)
 x44 = rbind(mapply, x2)
 x45 = chain(x43, x44, x42)
 x46 = fork(paint, identity, x45)
 x47 = power(x46, FOUR)
 x48 = x47(I)
 x49 = objects(x48, T, T, T)
 x50 = colorfilter(x49, x0)
 x51 = compose(maximum, shape)
 x52 = apply(x51, x50)
 x53 = maximum(x52)
 x54 = ofcolor(x48, x0)
 x55 = rbind(contained, x54)
 x56 = rbind(add, RIGHT)
 x57 = compose(x55, x56)
 x58 = rbind(add, LEFT)
 x59 = compose(x55, x58)
 x60 = fork(either, x57, x59)
 x61 = rbind(add, DOWN)
 x62 = compose(x55, x61)
 x63 = rbind(add, UP)
 x64 = compose(x55, x63)
 x65 = fork(either, x62, x64)
 x66 = fork(both, x60, x65)
 x67 = matcher(size, x53)
 x68 = fork(either, vline, hline)
 x69 = fork(both, x67, x68)
 x70 = sfilter(x50, x69)
 x71 = apply(center, x70)
 x72 = sfilter(x54, x66)
 x73 = combine(x72, x71)
 x74 = halve(x53)
 x75 = invert(x74)
 x76 = toivec(x75)
 x77 = rbind(add, x76)
 x78 = toivec(x74)
 x79 = rbind(add, x78)
 x80 = fork(connect, x77, x79)
 x81 = invert(x74)
 x82 = tojvec(x81)
 x83 = rbind(add, x82)
 x84 = tojvec(x74)
 x85 = rbind(add, x84)
 x86 = fork(connect, x83, x85)
 x87 = fork(combine, x80, x86)
 x88 = mapply(x87, x73)
 x89 = fill(x48, x0, x88)
 x90 = replace(x89, x0, EIGHT)
 x91 = fill(x90, x0, x1)
 return x91
def p(g):
 return [list(r)for r in verify_task118(tuple(tuple(r) for r in g))]