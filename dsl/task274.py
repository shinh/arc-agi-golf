NINE = 9
ONE = 1
THREE = 3
TWO = 2
ZERO = 0
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def color(obj):
 return next(iter(obj))[0]
def combine(a,b):
 return type(a)((*a, *b))
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
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def equality(a,b):
 return a == b
def extract(container,condition):
 return next(e for e in container if condition(e))
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
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
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def hsplit(grid,n):
 h, w = len(grid), len(grid[0]) // n
 offset = len(grid[0]) % n != 0
 return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def last(container):
 return max(enumerate(container))[1]
def llcorner(patch):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(patch):
 return tuple(map(max, zip(*toindices(patch))))
def matcher(function,target):
 return lambda x: function(x) == target
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def pair(a,b):
 return tuple(zip(a, b))
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def remove(value,container):
 return type(container)(e for e in container if e != value)
def repeat(item,num):
 return tuple(item for i in range(num))
def size(container):
 return len(container)
def subtract(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def urcorner(patch):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def vconcat(a,b):
 return a + b
def vmirror(piece):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
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
def verify_task274(I):
 x0 = partition(I)
 x1 = fork(multiply, height, width)
 x2 = argmax(x0, x1)
 x3 = remove(x2, x0)
 x4 = argmin(x3, x1)
 x5 = argmax(x3, x1)
 x6 = ulcorner(x5)
 x7 = llcorner(x5)
 x8 = connect(x6, x7)
 x9 = urcorner(x5)
 x10 = lrcorner(x5)
 x11 = connect(x9, x10)
 x12 = combine(x8, x11)
 x13 = toindices(x5)
 x14 = difference(x12, x13)
 x15 = size(x14)
 x16 = equality(x15, ZERO)
 x17 = branch(x16, height, width)
 x18 = x17(x5)
 x19 = x17(x4)
 x20 = subtract(x18, x19)
 x21 = decrement(x20)
 x22 = color(x4)
 x23 = color(x2)
 x24 = repeat(x22, x21)
 x25 = subtract(NINE, x21)
 x26 = repeat(x23, x25)
 x27 = combine(x24, x26)
 x28 = repeat(x27, ONE)
 x29 = hsplit(x28, THREE)
 x30 = interval(ZERO, THREE, ONE)
 x31 = pair(x30, x29)
 x32 = matcher(first, ZERO)
 x33 = extract(x31, x32)
 x34 = last(x33)
 x35 = matcher(first, ONE)
 x36 = extract(x31, x35)
 x37 = last(x36)
 x38 = matcher(first, TWO)
 x39 = extract(x31, x38)
 x40 = last(x39)
 x41 = vmirror(x37)
 x42 = vconcat(x34, x41)
 x43 = vconcat(x42, x40)
 return x43
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]