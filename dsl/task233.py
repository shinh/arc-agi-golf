F = False
NEG_ONE = -1
T = True
TWO = 2
def argmax(container,compfunc):
 return max(container, key=compfunc, default=None)
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def astuple(a,b):
 return (a, b)
def both(a,b):
 return a and b
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
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
def combine(a,b):
 return type(a)((*a, *b))
def compose(outer,inner):
 return lambda x: outer(inner(x))
def difference(a,b):
 return type(a)(e for e in a if e not in b)
def equality(a,b):
 return a == b
def first(container):
 return next(iter(container))
def fork(outer,a,b):
 return lambda x: outer(a(x), b(x))
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
def identity(x):
 return x
def initset(value):
 return frozenset({value})
def lbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda y: function(fixed, y)
 elif n == 3:
  return lambda y, z: function(fixed, y, z)
 else:
  return lambda y, z, a: function(fixed, y, z, a)
def apply(function,container):
 return type(container)(function(e) for e in container)
def merge(containers):
 return type(containers)(e for c in containers for e in c)
def mapply(function,container):
 return merge(apply(function, container))
def matcher(function,target):
 return lambda x: function(x) == target
def mostcolor(element):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def multiply(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def leftmost(patch):
 return min(j for i, j in toindices(patch))
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
def remove(value,container):
 return type(container)(e for e in container if e != value)
def other(container,value):
 return first(remove(value, container))
def paint(grid,obj):
 h, w = len(grid), len(grid[0])
 grid_painted = list(list(row) for row in grid)
 for value, (i, j) in obj:
  if 0 <= i < h and 0 <= j < w:
   grid_painted[i][j] = value
 return tuple(tuple(row) for row in grid_painted)
def positive(x):
 return x > 0
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
def replace(grid,replacee,replacer):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def rot180(grid):
 return tuple(tuple(row[::-1]) for row in grid[::-1])
def rot270(grid):
 return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]
def rot90(grid):
 return tuple(row for row in zip(*grid[::-1]))
def sfilter(container,condition):
 return type(container)(e for e in container if condition(e))
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
def crop(grid,start,dims):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(patch,grid):
 return crop(grid, ulcorner(patch), shape(patch))
def verify_task233(I):
 x0 = objects(I, F, F, T)
 x1 = fork(multiply, height, width)
 x2 = fork(equality, size, x1)
 x3 = matcher(numcolors, TWO)
 x4 = fork(both, x2, x3)
 x5 = sfilter(x0, x4)
 x6 = difference(x0, x5)
 x7 = merge(x6)
 x8 = color(x7)
 x9 = mostcolor(I)
 x10 = subgrid(x7, I)
 x11 = astuple(hmirror, vmirror)
 x12 = astuple(cmirror, dmirror)
 x13 = combine(x11, x12)
 x14 = astuple(identity, rot180)
 x15 = astuple(rot90, rot270)
 x16 = combine(x14, x15)
 x17 = combine(x16, x13)
 x18 = lbind(canvas, NEG_ONE)
 x19 = compose(x18, shape)
 x20 = fork(paint, x19, normalize)
 x21 = rbind(other, x8)
 x22 = compose(x21, palette)
 x23 = lbind(occurrences, x10)
 x24 = chain(positive, size, x23)
 x25 = compose(x24, asobject)
 x26 = rbind(replace, x8)
 x27 = rbind(replace, x9)
 x28 = rbind(x27, x8)
 x29 = compose(x28, x20)
 x30 = fork(x26, x29, x22)
 x31 = rbind(chain, initset)
 x32 = compose(x25, first)
 x33 = lbind(x31, x32)
 x34 = lbind(rbind, rapply)
 x35 = chain(x33, x34, x30)
 x36 = lbind(occurrences, x10)
 x37 = chain(first, x36, asobject)
 x38 = lbind(argmax, x17)
 x39 = compose(x38, x35)
 x40 = compose(initset, x39)
 x41 = fork(rapply, x40, x20)
 x42 = compose(first, x41)
 x43 = compose(initset, x39)
 x44 = fork(rapply, x43, x30)
 x45 = compose(first, x44)
 x46 = compose(asobject, x42)
 x47 = compose(x37, x45)
 x48 = fork(shift, x46, x47)
 x49 = mapply(x48, x5)
 x50 = paint(x10, x49)
 return x50
def p(g):
 return [list(r)for r in verify_task233(tuple(tuple(r) for r in g))]