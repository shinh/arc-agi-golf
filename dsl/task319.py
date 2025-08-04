TWO = 2
def asobject(grid):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
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
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def lowermost(patch):
 return max(i for i, j in toindices(patch))
def rightmost(patch):
 return max(j for i, j in toindices(patch))
def uppermost(patch):
 return min(i for i, j in toindices(patch))
def bordering(patch,grid):
 return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or rightmost(patch) == len(grid[0]) - 1
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def canvas(value,dimensions):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def color(obj):
 return next(iter(obj))[0]
def downscale(grid,factor):
 h, w = len(grid), len(grid[0])
 downscaled_grid = tuple()
 for i in range(h):
  downscaled_row = tuple()
  for j in range(w):
   if j % factor == 0:
    downscaled_row = downscaled_row + (grid[i][j],)
  downscaled_grid = downscaled_grid + (downscaled_row, )
 h = len(downscaled_grid)
 downscaled_grid2 = tuple()
 for i in range(h):
  if i % factor == 0:
   downscaled_grid2 = downscaled_grid2 + (downscaled_grid[i],)
 return downscaled_grid2
def extract(container,condition):
 return next(e for e in container if condition(e))
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
def last(container):
 return max(enumerate(container))[1]
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
F = False
T = True
def add(a,b):
 if isinstance(a, int) and isinstance(b, int):
  return a + b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] + b[0], a[1] + b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a + b[0], a + b[1])
 return (a[0] + b, a[1] + b)
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
def positive(x):
 return x > 0
def rbind(function,fixed):
 n = function.__code__.co_argcount
 if n == 2:
  return lambda x: function(x, fixed)
 elif n == 3:
  return lambda x, y: function(x, y, fixed)
 else:
  return lambda x, y, z: function(x, y, z, fixed)
def remove(value,container):
 return type(container)(e for e in container if e != value)
def replace(grid,replacee,replacer):
 return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)
def height(piece):
 if len(piece) == 0:
  return 0
 if isinstance(piece, tuple):
  return len(piece)
 return lowermost(piece) - uppermost(piece) + 1
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
def totuple(container):
 return tuple(container)
def ulcorner(patch):
 return tuple(map(min, zip(*toindices(patch))))
def upscale(element,factor):
 if isinstance(element, tuple):
  upscaled_grid = tuple()
  for row in element:
   upscaled_row = tuple()
   for value in row:
    upscaled_row = upscaled_row + tuple(value for num in range(factor))
   upscaled_grid = upscaled_grid + tuple(upscaled_row for num in range(factor))
  return upscaled_grid
 else:
  if len(element) == 0:
   return frozenset()
  di_inv, dj_inv = ulcorner(element)
  di, dj = (-di_inv, -dj_inv)
  normed_obj = shift(element, (di, dj))
  upscaled_obj = set()
  for value, (i, j) in normed_obj:
   for io in range(factor):
    for jo in range(factor):
     upscaled_obj.add((value, (i * factor + io, j * factor + jo)))
  return shift(frozenset(upscaled_obj), (di_inv, dj_inv))
def verify_task319(I):
 x0 = fgpartition(I)
 x1 = rbind(bordering, I)
 x2 = extract(x0, x1)
 x3 = remove(x2, x0)
 x4 = totuple(x3)
 x5 = first(x4)
 x6 = last(x4)
 x7 = color(x5)
 x8 = mostcolor(I)
 x9 = shape(x5)
 x10 = canvas(x8, x9)
 x11 = normalize(x5)
 x12 = paint(x10, x11)
 x13 = upscale(x12, TWO)
 x14 = shape(x6)
 x15 = canvas(x8, x14)
 x16 = normalize(x6)
 x17 = paint(x15, x16)
 x18 = upscale(x17, TWO)
 x19 = shape(x2)
 x20 = canvas(x8, x19)
 x21 = normalize(x2)
 x22 = paint(x20, x21)
 x23 = color(x2)
 x24 = replace(x22, x23, x7)
 x25 = asobject(x24)
 x26 = occurrences(x13, x25)
 x27 = size(x26)
 x28 = positive(x27)
 x29 = downscale(x13, TWO)
 x30 = downscale(x18, TWO)
 x31 = branch(x28, x29, x30)
 return x31
def p(g):
 return [list(r)for r in verify_task319(tuple(tuple(r) for r in g))]