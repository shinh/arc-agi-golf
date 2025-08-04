NEG_ONE = -1
ONE = 1
ORIGIN = (0, 0)
SEVEN = 7
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
def argmin(container,compfunc):
 return min(container, key=compfunc, default=None)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def backdrop(patch):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def both(a,b):
 return a and b
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
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
def colorcount(element,value):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def decrement(x):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def equality(a,b):
 return a == b
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(element):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(grid):
 return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
def greater(a,b):
 return a > b
def halve(n):
 return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)
def identity(x):
 return x
def increment(x):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def initset(value):
 return frozenset({value})
def insert(value,container):
 return container.union(frozenset({value}))
def interval(start,stop,step):
 return tuple(range(start, stop, step))
def invert(n):
 return -n if isinstance(n, int) else (-n[0], -n[1])
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
def manhattan(a,b):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
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
F = False
T = True
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def normalize(patch):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
def occurrences(grid,obj):
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
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def product(a,b):
 return frozenset((i, j) for j in b for i in a)
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
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
def shape(piece):
 return (height(piece), width(piece))
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(patch,grid):
 return crop(grid, ulcorner(patch), shape(patch))
def subtract(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def valmax(container,compfunc):
 return compfunc(max(container, key=compfunc, default=0))
def verify_task361(I):
 x0 = fgpartition(I)
 x1 = merge(x0)
 x2 = mostcolor(I)
 x3 = uppermost(x1)
 x4 = leftmost(x1)
 x5 = height(x1)
 x6 = width(x1)
 x7 = interval(SEVEN, ONE, NEG_ONE)
 x8 = add(x3, x5)
 x9 = increment(x8)
 x10 = lbind(subtract, x9)
 x11 = add(x4, x6)
 x12 = increment(x11)
 x13 = lbind(subtract, x12)
 x14 = lbind(interval, x3)
 x15 = rbind(x14, ONE)
 x16 = compose(x15, x10)
 x17 = lbind(interval, x4)
 x18 = rbind(x17, ONE)
 x19 = compose(x18, x13)
 x20 = fork(product, x16, x19)
 x21 = fork(equality, identity, rot90)
 x22 = fork(equality, identity, rot180)
 x23 = fork(equality, identity, rot270)
 x24 = fork(both, x22, x23)
 x25 = fork(both, x21, x24)
 x26 = fork(astuple, identity, identity)
 x27 = fork(multiply, identity, identity)
 x28 = compose(decrement, x27)
 x29 = initset(ORIGIN)
 x30 = difference(x29, x29)
 x31 = rbind(branch, x30)
 x32 = rbind(colorcount, x2)
 x33 = rbind(subgrid, I)
 x34 = lbind(compose, backdrop)
 x35 = lbind(fork, insert)
 x36 = lbind(x35, identity)
 x37 = lbind(compose, initset)
 x38 = chain(x34, x36, x37)
 x39 = lbind(rbind, add)
 x40 = chain(x38, x39, decrement)
 x41 = lbind(fork, x31)
 x42 = lbind(fork, both)
 x43 = lbind(x42, x25)
 x44 = rbind(compose, shape)
 x45 = compose(x43, x44)
 x46 = rbind(compose, x32)
 x47 = lbind(lbind, greater)
 x48 = chain(x46, x47, x28)
 x49 = lbind(rbind, equality)
 x50 = chain(x45, x49, x26)
 x51 = fork(x42, x48, x50)
 x52 = lbind(compose, x33)
 x53 = compose(x52, x40)
 x54 = fork(compose, x51, x53)
 x55 = lbind(compose, initset)
 x56 = lbind(rbind, astuple)
 x57 = compose(x55, x56)
 x58 = fork(x41, x54, x57)
 x59 = fork(mapply, x58, x20)
 x60 = center(x1)
 x61 = astuple(x60, ONE)
 x62 = repeat(x61, ONE)
 x63 = mapply(x59, x7)
 x64 = combine(x62, x63)
 x65 = valmax(x64, last)
 x66 = matcher(last, x65)
 x67 = sfilter(x64, x66)
 x68 = center(x1)
 x69 = initset(x68)
 x70 = rbind(manhattan, x69)
 x71 = compose(halve, last)
 x72 = fork(add, first, x71)
 x73 = compose(initset, x72)
 x74 = compose(x70, x73)
 x75 = argmin(x67, x74)
 x76 = first(x75)
 x77 = last(x75)
 x78 = decrement(x77)
 x79 = add(x76, x78)
 x80 = initset(x79)
 x81 = insert(x76, x80)
 x82 = backdrop(x81)
 x83 = subgrid(x82, I)
 x84 = asobject(x83)
 x85 = rot90(I)
 x86 = fgpartition(x85)
 x87 = merge(x86)
 x88 = rot180(I)
 x89 = fgpartition(x88)
 x90 = merge(x89)
 x91 = rot270(I)
 x92 = fgpartition(x91)
 x93 = merge(x92)
 x94 = rot90(I)
 x95 = occurrences(x94, x84)
 x96 = first(x95)
 x97 = invert(x96)
 x98 = shift(x87, x97)
 x99 = shift(x98, x76)
 x100 = rot180(I)
 x101 = occurrences(x100, x84)
 x102 = first(x101)
 x103 = invert(x102)
 x104 = shift(x90, x103)
 x105 = shift(x104, x76)
 x106 = rot270(I)
 x107 = occurrences(x106, x84)
 x108 = first(x107)
 x109 = invert(x108)
 x110 = shift(x93, x109)
 x111 = shift(x110, x76)
 x112 = combine(x99, x105)
 x113 = combine(x112, x111)
 x114 = paint(I, x113)
 return x114
def p(g):
 return [list(r)for r in verify_task361(tuple(tuple(r) for r in g))]