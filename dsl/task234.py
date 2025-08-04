def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
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
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def dmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*piece))
 a, b = ulcorner(piece)
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
 return frozenset((j - b + a, i - a + b) for i, j in piece)
def replace(
 grid,
 replacee,
 replacer
):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def combine(
 a,
 b
):
 return type(a)((*a, *b))
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
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def height(
 piece
):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
def shape(
 piece
):
 return (height(piece), width(piece))
ZERO_BY_TWO = (0, 2)
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
UNITY = (1, 1)
def first(
 container
):
 return next(iter(container))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def mapply(
 function,
 container
):
 return merge(apply(function, container))
def trim(
 grid
):
 return tuple(r[1:-1] for r in grid[1:-1])
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
T = True
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
F = False
def occurrences(
 grid,
 obj
):
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
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def box(
 patch
):
 if len(patch) == 0:
  return patch
 ai, aj = ulcorner(patch)
 bi, bj = lrcorner(patch)
 si, sj = min(ai, bi), min(aj, bj)
 ei, ej = max(ai, bi), max(aj, bj)
 vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
 hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
 return frozenset(vlines | hlines)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
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
def initset(
 value
):
 return frozenset({value})
def equality(
 a,
 b
):
 return a == b
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def vmatching(
 a,
 b
):
 return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0
def manhattan(
 a,
 b
):
 return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
def adjacent(
 a,
 b
):
 return manhattan(a, b) == 1
def gravitate(
 source,
 destination
):
 source_i, source_j = center(source)
 destination_i, destination_j = center(destination)
 i, j = 0, 0
 if vmatching(source, destination):
  i = 1 if source_i < destination_i else -1
 else:
  j = 1 if source_j < destination_j else -1
 direction = (i, j)
 gravitation_i, gravitation_j = i, j
 maxcount = 42
 c = 0
 while not adjacent(source, destination) and c < maxcount:
  c += 1
  gravitation_i += i
  gravitation_j += j
  source = shift(source, direction)
 return (gravitation_i - i, gravitation_j - j)
ORIGIN = (0, 0)
def astuple(
 a,
 b
):
 return (a, b)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
RIGHT = (0, 1)
def identity(
 x
):
 return x
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def color(
 obj
):
 return next(iter(obj))[0]
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
TWO = 2
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def fill(
 grid,
 value,
 patch
):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
def verify_task234(I):
 x0 = asindices(I)
 x1 = box(x0)
 x2 = toobject(x1, I)
 x3 = mostcolor(x2)
 x4 = shape(I)
 x5 = add(TWO, x4)
 x6 = canvas(x3, x5)
 x7 = asobject(I)
 x8 = shift(x7, UNITY)
 x9 = paint(x6, x8)
 x10 = palette(x9)
 x11 = remove(x3, x10)
 x12 = lbind(ofcolor, x9)
 x13 = fork(recolor, identity, x12)
 x14 = apply(x13, x11)
 x15 = fork(equality, toindices, backdrop)
 x16 = extract(x14, x15)
 x17 = other(x14, x16)
 x18 = color(x17)
 x19 = astuple(x18, RIGHT)
 x20 = initset(ZERO_BY_TWO)
 x21 = insert(ORIGIN, x20)
 x22 = recolor(x3, x21)
 x23 = insert(x19, x22)
 x24 = dmirror(x23)
 x25 = lbind(shift, x23)
 x26 = occurrences(x9, x23)
 x27 = mapply(x25, x26)
 x28 = lbind(shift, x24)
 x29 = occurrences(x9, x24)
 x30 = mapply(x28, x29)
 x31 = combine(x27, x30)
 x32 = fill(x9, x3, x31)
 x33 = ofcolor(x32, x18)
 x34 = gravitate(x33, x16)
 x35 = replace(x9, x18, x3)
 x36 = shift(x33, x34)
 x37 = fill(x35, x18, x36)
 x38 = trim(x37)
 return x38
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]