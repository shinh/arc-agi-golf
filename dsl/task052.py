FIVE = 5
ONE = 1
ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
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
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
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
def repeat(
 item,
 num
):
 return tuple(item for i in range(num))
def size(
 container
):
 return len(container)
def toindices(
 patch
):
 if len(patch) == 0:
  return frozenset()
 if isinstance(next(iter(patch))[1], tuple):
  return frozenset(index for value, index in patch)
 return patch
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
def verify_task052(I):
 x0 = width(I)
 x1 = rbind(branch, ZERO)
 x2 = rbind(x1, FIVE)
 x3 = compose(size, dedupe)
 x4 = matcher(x3, ONE)
 x5 = compose(x2, x4)
 x6 = rbind(repeat, x0)
 x7 = compose(x6, x5)
 x8 = apply(x7, I)
 return x8
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]