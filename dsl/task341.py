EIGHT = 8
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
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def astuple(
 a,
 b
):
 return (a, b)
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def backdrop(
 patch
):
 if len(patch) == 0:
  return frozenset({})
 indices = toindices(patch)
 si, sj = ulcorner(indices)
 ei, ej = lrcorner(patch)
 return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def contained(
 value,
 container
):
 return value in container
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def equality(
 a,
 b
):
 return a == b
def extract(
 container,
 condition
):
 return next(e for e in container if condition(e))
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
def first(
 container
):
 return next(iter(container))
def flip(
 b
):
 return not b
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def hmatching(
 a,
 b
):
 return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0
def increment(
 x
):
 return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)
def initset(
 value
):
 return frozenset({value})
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def last(
 container
):
 return max(enumerate(container))[1]
def leftmost(
 patch
):
 return min(j for i, j in toindices(patch))
def lowermost(
 patch
):
 return max(i for i, j in toindices(patch))
def maximum(
 container
):
 return max(container, default=0)
def merge(
 containers
):
 return type(containers)(e for c in containers for e in c)
def minimum(
 container
):
 return min(container, default=0)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def partition(
 grid
):
 return frozenset(
  frozenset(
   (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
  ) for value in palette(grid)
 )
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def rightmost(
 patch
):
 return max(j for i, j in toindices(patch))
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def totuple(
 container
):
 return tuple(container)
def uppermost(
 patch
):
 return min(i for i, j in toindices(patch))
def verify_task341(I):
 x0 = partition(I)
 x1 = product(x0, x0)
 x2 = fork(equality, first, last)
 x3 = compose(flip, x2)
 x4 = sfilter(x1, x3)
 x5 = fork(adjacent, first, last)
 x6 = compose(flip, x5)
 x7 = extract(x4, x6)
 x8 = totuple(x7)
 x9 = first(x8)
 x10 = last(x8)
 x11 = combine(x9, x10)
 x12 = leftmost(x11)
 x13 = increment(x12)
 x14 = rightmost(x11)
 x15 = decrement(x14)
 x16 = apply(uppermost, x8)
 x17 = maximum(x16)
 x18 = increment(x17)
 x19 = apply(lowermost, x8)
 x20 = minimum(x19)
 x21 = decrement(x20)
 x22 = apply(leftmost, x8)
 x23 = maximum(x22)
 x24 = increment(x23)
 x25 = apply(rightmost, x8)
 x26 = minimum(x25)
 x27 = decrement(x26)
 x28 = uppermost(x11)
 x29 = increment(x28)
 x30 = lowermost(x11)
 x31 = decrement(x30)
 x32 = hmatching(x9, x10)
 x33 = branch(x32, x13, x24)
 x34 = branch(x32, x15, x27)
 x35 = branch(x32, x21, x31)
 x36 = branch(x32, x18, x29)
 x37 = astuple(x35, x34)
 x38 = astuple(x36, x33)
 x39 = initset(x38)
 x40 = insert(x37, x39)
 x41 = backdrop(x40)
 x42 = merge(x7)
 x43 = toindices(x42)
 x44 = rbind(contained, x43)
 x45 = compose(flip, x44)
 x46 = sfilter(x41, x45)
 x47 = fill(I, EIGHT, x46)
 return x47
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]