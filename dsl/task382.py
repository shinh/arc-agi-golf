ONE = 1
TWO = 2
ZERO = 0
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
def astuple(a,b):
 return (a, b)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def chain(h,g,f):
 return lambda x: h(g(f(x)))
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
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(piece):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def cmirror(piece):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
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
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def equality(a,b):
 return a == b
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
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def hmirror(piece):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def insert(value,container):
 return container.union(frozenset({value}))
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
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def ofcolor(grid,value):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def order(container,compfunc):
 return tuple(sorted(container, key=compfunc))
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def pair(a,b):
 return tuple(zip(a, b))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def size(container):
 return len(container)
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def width(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece[0])
 return rightmost(piece) - leftmost(piece) + 1
def verify_task382(I):
 x0 = rbind(ofcolor, TWO)
 x1 = compose(lowermost, x0)
 x2 = matcher(x1, ZERO)
 x3 = astuple(identity, dmirror)
 x4 = astuple(cmirror, hmirror)
 x5 = combine(x3, x4)
 x6 = rbind(rapply, I)
 x7 = compose(first, x6)
 x8 = chain(x2, x7, initset)
 x9 = extract(x5, x8)
 x10 = x9(I)
 x11 = mostcolor(I)
 x12 = palette(I)
 x13 = remove(x11, x12)
 x14 = other(x13, TWO)
 x15 = ofcolor(x10, x14)
 x16 = rightmost(x15)
 x17 = equality(x16, ZERO)
 x18 = branch(x17, identity, vmirror)
 x19 = x18(x10)
 x20 = ofcolor(x19, x14)
 x21 = ofcolor(x19, TWO)
 x22 = apply(last, x21)
 x23 = insert(ZERO, x22)
 x24 = width(x19)
 x25 = insert(x24, x23)
 x26 = order(x25, identity)
 x27 = last(x26)
 x28 = remove(x27, x26)
 x29 = first(x26)
 x30 = remove(x29, x26)
 x31 = pair(x28, x30)
 x32 = size(x28)
 x33 = interval(ZERO, x32, ONE)
 x34 = pair(x33, x31)
 x35 = lbind(fork, connect)
 x36 = compose(first, last)
 x37 = chain(decrement, last, last)
 x38 = lbind(lbind, add)
 x39 = compose(x38, first)
 x40 = lbind(rbind, astuple)
 x41 = rbind(chain, first)
 x42 = compose(x40, x36)
 x43 = compose(x40, x37)
 x44 = fork(x41, x42, x39)
 x45 = fork(x41, x43, x39)
 x46 = fork(x35, x44, x45)
 x47 = rbind(mapply, x20)
 x48 = compose(x47, x46)
 x49 = mapply(x48, x34)
 x50 = fill(x19, x14, x49)
 x51 = x18(x50)
 x52 = x9(x51)
 return x52
def p(g):
 return [list(r)for r in verify_task382(tuple(tuple(r) for r in g))]