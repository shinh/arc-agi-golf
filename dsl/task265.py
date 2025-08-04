ORIGIN = (0, 0)
TWO = 2
ZERO = 0
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
def fill(grid,value,patch):
 h, w = len(grid), len(grid[0])
 grid_filled = list(list(row) for row in grid)
 for i, j in toindices(patch):
  if 0 <= i < h and 0 <= j < w:
   grid_filled[i][j] = value
 return tuple(tuple(row) for row in grid_filled)
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
def leftmost(patch):
 return min(j for i, j in toindices(patch))
def shift(patch,directions):
 if len(patch) == 0:
  return patch
 di, dj = directions
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
 return frozenset((i + di, j + dj) for i, j in patch)
def uppermost(patch):
 return min(i for i, j in toindices(patch))
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
def recolor(value,patch):
 return frozenset((value, index) for index in toindices(patch))
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
def verify_task265(I):
 x0 = initset(ORIGIN)
 x1 = recolor(ZERO, x0)
 x2 = upscale(x1, TWO)
 x3 = occurrences(I, x2)
 x4 = lbind(shift, x2)
 x5 = mapply(x4, x3)
 x6 = fill(I, TWO, x5)
 return x6
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]