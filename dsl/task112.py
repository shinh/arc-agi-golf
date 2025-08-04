FOUR = 4
def both(
 a,
 b
):
 return a and b
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def color(
 obj
):
 return next(iter(obj))[0]
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def fgpartition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid) - {mostcolor(grid)}
 )
def first(
 container
):
 return next(iter(container))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def identity(
 x
):
 return x
def initset(
 value
):
 return frozenset({value})
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
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
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
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
def size(
 container
):
 return len(container)
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
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
def square(
 piece
):
 return len(piece) == len(piece[0]) if isinstance(piece, tuple) else height(piece) * width(piece) == len(piece) and height(piece) == width(piece)
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
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def verify_task112(I):
 x0 = fgpartition(I)
 x1 = matcher(size, FOUR)
 x2 = fork(both, square, x1)
 x3 = extract(x0, x2)
 x4 = color(x3)
 x5 = merge(x0)
 x6 = compose(hmirror, vmirror)
 x7 = initset(x6)
 x8 = insert(vmirror, x7)
 x9 = insert(hmirror, x8)
 x10 = rapply(x9, x5)
 x11 = ulcorner(x3)
 x12 = lbind(subtract, x11)
 x13 = matcher(first, x4)
 x14 = rbind(sfilter, x13)
 x15 = chain(x12, ulcorner, x14)
 x16 = fork(shift, identity, x15)
 x17 = mapply(x16, x10)
 x18 = paint(I, x17)
 return x18
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]