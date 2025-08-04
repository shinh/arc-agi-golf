DOWN = (1, 0)
FOUR = 4
ONE = 1
TWO = 2
ZERO = 0
def apply(function,container):
 return type(container)(function(e) for e in container)
def asindices(grid):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def astuple(a,b):
 return (a, b)
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def chain(h,g,f):
 return lambda x: h(g(f(x)))
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(iterable):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def extract(container,condition):
 return next(e for e in container if condition(e))
def toindices(patch):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def first(container):
 return next(iter(container))
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
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def last(container):
 return max(enumerate(container))[1]
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
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def pair(a,b):
 return tuple(zip(a, b))
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
def repeat(item,num):
 return tuple(item for i in range(num))
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
def shape(piece):
 return (height(piece), width(piece))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
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
def shoot(start,direction):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def verify_task084(I):
 x0 = astuple(identity, identity)
 x1 = astuple(rot90, rot270)
 x2 = astuple(x0, x1)
 x3 = astuple(rot180, rot180)
 x4 = astuple(rot270, rot90)
 x5 = astuple(x3, x4)
 x6 = combine(x2, x5)
 x7 = leastcolor(I)
 x8 = repeat(x7, ONE)
 x9 = rbind(rapply, I)
 x10 = chain(x9, initset, first)
 x11 = compose(first, x10)
 x12 = chain(dedupe, first, x11)
 x13 = matcher(x12, x8)
 x14 = extract(x6, x13)
 x15 = first(x14)
 x16 = last(x14)
 x17 = x15(I)
 x18 = ofcolor(x17, x7)
 x19 = height(x18)
 x20 = interval(ZERO, x19, ONE)
 x21 = lbind(astuple, x19)
 x22 = apply(x21, x20)
 x23 = rbind(shoot, DOWN)
 x24 = mapply(x23, x22)
 x25 = fill(x17, FOUR, x24)
 x26 = astuple(x19, x19)
 x27 = canvas(ZERO, x26)
 x28 = asindices(x27)
 x29 = shift(x28, x26)
 x30 = shape(I)
 x31 = maximum(x30)
 x32 = lbind(shift, x29)
 x33 = interval(ZERO, x31, x19)
 x34 = pair(x33, x33)
 x35 = mapply(x32, x34)
 x36 = fill(x25, TWO, x35)
 x37 = x16(x36)
 return x37
def p(g):
 return [list(r)for r in verify_task084(tuple(tuple(r) for r in g))]