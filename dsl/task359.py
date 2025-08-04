ONE = 1
def apply(function,container):
 return type(container)(function(e) for e in container)
def branch(condition,if_value,else_value):
 return if_value if condition else else_value
def compose(outer,inner):
 return lambda x: outer(inner(x))
def index(grid,loc):
 i, j = loc
 h, w = len(grid), len(grid[0])
 if not (0 <= i < h and 0 <= j < w):
  return None
 return grid[loc[0]][loc[1]]
def dedupe(iterable):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def greater(a,b):
 return a > b
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
def hupscale(grid,factor):
 upscaled_grid = tuple()
 for row in grid:
  upscaled_row = tuple()
  for value in row:
   upscaled_row = upscaled_row + tuple(value for num in range(factor))
  upscaled_grid = upscaled_grid + (upscaled_row,)
 return upscaled_grid
def mostcommon(container):
 return max(set(container), key=container.count)
def repeat(item,num):
 return tuple(item for i in range(num))
def size(container):
 return len(container)
def vupscale(grid,factor):
 upscaled_grid = tuple()
 for row in grid:
  upscaled_grid = upscaled_grid + tuple(row for num in range(factor))
 return upscaled_grid
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
def verify_task359(I):
 x0 = rot90(I)
 x1 = apply(mostcommon, I)
 x2 = apply(mostcommon, x0)
 x3 = repeat(x1, ONE)
 x4 = repeat(x2, ONE)
 x5 = compose(size, dedupe)
 x6 = x5(x1)
 x7 = x5(x2)
 x8 = greater(x7, x6)
 x9 = branch(x8, height, width)
 x10 = x9(I)
 x11 = rot90(x3)
 x12 = branch(x8, x4, x11)
 x13 = branch(x8, vupscale, hupscale)
 x14 = x13(x12, x10)
 return x14
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]