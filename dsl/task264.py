def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
T = True
def toivec(
 i
):
 return (i, 0)
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def tojvec(
 j
):
 return (0, j)
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def argmax(
 container,
 compfunc
):
 return max(container, key=compfunc, default=None)
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
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def subtract(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a - b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] - b[0], a[1] - b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a - b[0], a - b[1])
 return (a[0] - b, a[1] - b)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
ONE = 1
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
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
def equality(
 a,
 b
):
 return a == b
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def normalize(
 patch
):
 if len(patch) == 0:
  return patch
 return shift(patch, (-uppermost(patch), -leftmost(patch)))
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
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
ZERO = 0
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
def flip(
 b
):
 return not b
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def astuple(
 a,
 b
):
 return (a, b)
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def both(
 a,
 b
):
 return a and b
def size(
 container
):
 return len(container)
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
def color(
 obj
):
 return next(iter(obj))[0]
def contained(
 value,
 container
):
 return value in container
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
TWO = 2
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
F = False
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def verify_task264(I):
 x0 = objects(I, T, F, F)
 x1 = mostcolor(I)
 x2 = palette(I)
 x3 = remove(x1, x2)
 x4 = lbind(colorcount, I)
 x5 = argmax(x3, x4)
 x6 = astuple(x1, x5)
 x7 = rbind(contained, x6)
 x8 = chain(flip, x7, color)
 x9 = sfilter(x0, x8)
 x10 = fork(connect, ulcorner, urcorner)
 x11 = fork(connect, ulcorner, llcorner)
 x12 = fork(combine, x10, x11)
 x13 = fork(equality, toindices, x12)
 x14 = fork(connect, urcorner, ulcorner)
 x15 = fork(connect, urcorner, lrcorner)
 x16 = fork(combine, x14, x15)
 x17 = fork(equality, toindices, x16)
 x18 = fork(connect, llcorner, ulcorner)
 x19 = fork(connect, llcorner, lrcorner)
 x20 = fork(combine, x18, x19)
 x21 = fork(equality, toindices, x20)
 x22 = fork(connect, lrcorner, llcorner)
 x23 = fork(connect, lrcorner, urcorner)
 x24 = fork(combine, x22, x23)
 x25 = fork(equality, toindices, x24)
 x26 = fork(contained, lrcorner, toindices)
 x27 = compose(flip, x26)
 x28 = fork(contained, llcorner, toindices)
 x29 = compose(flip, x28)
 x30 = fork(contained, urcorner, toindices)
 x31 = compose(flip, x30)
 x32 = fork(contained, ulcorner, toindices)
 x33 = compose(flip, x32)
 x34 = fork(both, x27, x29)
 x35 = fork(both, x31, x33)
 x36 = fork(both, x31, x27)
 x37 = fork(both, x33, x29)
 x38 = lbind(matcher, first)
 x39 = compose(x38, lowermost)
 x40 = fork(sfilter, toindices, x39)
 x41 = compose(size, x40)
 x42 = matcher(x41, ONE)
 x43 = lbind(matcher, first)
 x44 = compose(x43, uppermost)
 x45 = fork(sfilter, toindices, x44)
 x46 = compose(size, x45)
 x47 = matcher(x46, ONE)
 x48 = lbind(matcher, last)
 x49 = compose(x48, rightmost)
 x50 = fork(sfilter, toindices, x49)
 x51 = compose(size, x50)
 x52 = matcher(x51, ONE)
 x53 = lbind(matcher, last)
 x54 = compose(x53, leftmost)
 x55 = fork(sfilter, toindices, x54)
 x56 = compose(size, x55)
 x57 = matcher(x56, ONE)
 x58 = fork(both, x34, x42)
 x59 = fork(both, x35, x47)
 x60 = fork(both, x36, x52)
 x61 = fork(both, x37, x57)
 x62 = fork(connect, ulcorner, urcorner)
 x63 = fork(difference, x62, toindices)
 x64 = compose(size, x63)
 x65 = matcher(x64, ZERO)
 x66 = fork(connect, llcorner, lrcorner)
 x67 = fork(difference, x66, toindices)
 x68 = compose(size, x67)
 x69 = matcher(x68, ZERO)
 x70 = fork(connect, ulcorner, llcorner)
 x71 = fork(difference, x70, toindices)
 x72 = compose(size, x71)
 x73 = matcher(x72, ZERO)
 x74 = fork(connect, urcorner, lrcorner)
 x75 = fork(difference, x74, toindices)
 x76 = compose(size, x75)
 x77 = matcher(x76, ZERO)
 x78 = fork(both, x65, x58)
 x79 = fork(both, x69, x59)
 x80 = fork(both, x73, x60)
 x81 = fork(both, x77, x61)
 x82 = argmax(x9, x13)
 x83 = argmax(x9, x17)
 x84 = argmax(x9, x21)
 x85 = argmax(x9, x25)
 x86 = argmax(x9, x78)
 x87 = argmax(x9, x79)
 x88 = argmax(x9, x80)
 x89 = argmax(x9, x81)
 x90 = height(x82)
 x91 = height(x84)
 x92 = add(x90, x91)
 x93 = height(x88)
 x94 = add(x93, TWO)
 x95 = add(x92, x94)
 x96 = width(x82)
 x97 = width(x83)
 x98 = add(x96, x97)
 x99 = width(x86)
 x100 = add(x99, TWO)
 x101 = add(x98, x100)
 x102 = ulcorner(x82)
 x103 = increment(x102)
 x104 = index(I, x103)
 x105 = astuple(x95, x101)
 x106 = canvas(x104, x105)
 x107 = normalize(x82)
 x108 = paint(x106, x107)
 x109 = normalize(x83)
 x110 = width(x83)
 x111 = subtract(x101, x110)
 x112 = tojvec(x111)
 x113 = shift(x109, x112)
 x114 = paint(x108, x113)
 x115 = normalize(x84)
 x116 = height(x84)
 x117 = subtract(x95, x116)
 x118 = toivec(x117)
 x119 = shift(x115, x118)
 x120 = paint(x114, x119)
 x121 = normalize(x85)
 x122 = height(x85)
 x123 = subtract(x95, x122)
 x124 = width(x85)
 x125 = subtract(x101, x124)
 x126 = astuple(x123, x125)
 x127 = shift(x121, x126)
 x128 = paint(x120, x127)
 x129 = normalize(x88)
 x130 = height(x82)
 x131 = increment(x130)
 x132 = toivec(x131)
 x133 = shift(x129, x132)
 x134 = paint(x128, x133)
 x135 = normalize(x86)
 x136 = width(x82)
 x137 = increment(x136)
 x138 = tojvec(x137)
 x139 = shift(x135, x138)
 x140 = paint(x134, x139)
 x141 = normalize(x89)
 x142 = height(x83)
 x143 = increment(x142)
 x144 = width(x89)
 x145 = subtract(x101, x144)
 x146 = astuple(x143, x145)
 x147 = shift(x141, x146)
 x148 = paint(x140, x147)
 x149 = normalize(x87)
 x150 = height(x87)
 x151 = subtract(x95, x150)
 x152 = width(x84)
 x153 = increment(x152)
 x154 = astuple(x151, x153)
 x155 = shift(x149, x154)
 x156 = paint(x148, x155)
 return x156
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]