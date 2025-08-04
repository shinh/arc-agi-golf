ZERO = 0
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
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
def center(
 patch
):
 return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)
def color(
 obj
):
 return next(iter(obj))[0]
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def decrement(
 x
):
 return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)
def either(
 a,
 b
):
 return a or b
def equality(
 a,
 b
):
 return a == b
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
def initset(
 value
):
 return frozenset({value})
def last(
 container
):
 return max(enumerate(container))[1]
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
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
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
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def verify_task045(I):
 x0 = mostcolor(I)
 x1 = asobject(I)
 x2 = matcher(first, x0)
 x3 = compose(flip, x2)
 x4 = sfilter(x1, x3)
 x5 = apply(initset, x4)
 x6 = product(x5, x5)
 x7 = compose(color, first)
 x8 = compose(color, last)
 x9 = fork(equality, x7, x8)
 x10 = sfilter(x6, x9)
 x11 = compose(leftmost, first)
 x12 = compose(leftmost, last)
 x13 = fork(equality, x11, x12)
 x14 = compose(uppermost, first)
 x15 = compose(uppermost, last)
 x16 = fork(equality, x14, x15)
 x17 = fork(either, x13, x16)
 x18 = sfilter(x10, x17)
 x19 = compose(color, first)
 x20 = compose(center, first)
 x21 = compose(center, last)
 x22 = fork(connect, x20, x21)
 x23 = fork(recolor, x19, x22)
 x24 = height(I)
 x25 = width(I)
 x26 = matcher(last, ZERO)
 x27 = decrement(x25)
 x28 = matcher(last, x27)
 x29 = fork(either, x26, x28)
 x30 = matcher(first, ZERO)
 x31 = decrement(x24)
 x32 = matcher(first, x31)
 x33 = fork(either, x30, x32)
 x34 = toindices(x4)
 x35 = sfilter(x34, x29)
 x36 = equality(x34, x35)
 x37 = mapply(x23, x18)
 x38 = paint(I, x37)
 x39 = branch(x36, x29, x33)
 x40 = asindices(I)
 x41 = sfilter(x40, x39)
 x42 = toobject(x41, I)
 x43 = paint(x38, x42)
 return x43
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]