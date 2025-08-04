ONE = 1
ORIGIN = (0, 0)
def astuple(a,b):
 return (a, b)
def both(a,b):
 return a and b
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
def color(obj):
 return next(iter(obj))[0]
def colorcount(element,value):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
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
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def halve(n):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
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
def hmirror(piece):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
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
def matcher(function,target):
 return lambda x: function(x) == target
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def numcolors(element):
 return len(palette(element))
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
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
def size(container):
 return len(container)
def toivec(i):
 return (i, 0)
def tojvec(j):
 return (0, j)
def toobject(patch,grid):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def verify_task241(I):
 x0 = shape(I)
 x1 = decrement(x0)
 x2 = connect(ORIGIN, x1)
 x3 = height(I)
 x4 = decrement(x3)
 x5 = toivec(x4)
 x6 = width(I)
 x7 = decrement(x6)
 x8 = tojvec(x7)
 x9 = connect(x5, x8)
 x10 = height(I)
 x11 = halve(x10)
 x12 = toivec(x11)
 x13 = width(I)
 x14 = decrement(x13)
 x15 = astuple(x11, x14)
 x16 = connect(x12, x15)
 x17 = width(I)
 x18 = halve(x17)
 x19 = tojvec(x18)
 x20 = height(I)
 x21 = decrement(x20)
 x22 = astuple(x21, x18)
 x23 = connect(x19, x22)
 x24 = astuple(x2, dmirror)
 x25 = astuple(x9, cmirror)
 x26 = astuple(x24, x25)
 x27 = astuple(x23, vmirror)
 x28 = astuple(x16, hmirror)
 x29 = astuple(x27, x28)
 x30 = combine(x26, x29)
 x31 = lbind(colorcount, I)
 x32 = rbind(toobject, I)
 x33 = compose(x32, first)
 x34 = chain(x31, color, x33)
 x35 = compose(size, first)
 x36 = fork(equality, x34, x35)
 x37 = rbind(toobject, I)
 x38 = chain(numcolors, x37, first)
 x39 = matcher(x38, ONE)
 x40 = fork(both, x39, x36)
 x41 = extract(x30, x40)
 x42 = last(x41)
 x43 = x42(I)
 return x43
def p(g):
 return [list(r)for r in verify_task241(tuple(tuple(r) for r in g))]