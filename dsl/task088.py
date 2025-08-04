def asindices(
 grid
):
 return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def switch(
 grid,
 a,
 b
):
 return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
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
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def last(
 container
):
 return max(enumerate(container))[1]
def first(
 container
):
 return next(iter(container))
def order(
 container,
 compfunc
):
 return tuple(sorted(container, key=compfunc))
def ulcorner(
 patch
):
 return tuple(map(min, zip(*toindices(patch))))
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def llcorner(
 patch
):
 return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def corners(
 patch
):
 return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})
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
def crop(
 grid,
 start,
 dims
):
 return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])
def subgrid(
 patch,
 grid
):
 return crop(grid, ulcorner(patch), shape(patch))
def identity(
 x
):
 return x
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def verify_task088(I):
 x0 = asindices(I)
 x1 = corners(x0)
 x2 = mapply(dneighbors, x1)
 x3 = toobject(x2, I)
 x4 = mostcolor(x3)
 x5 = palette(I)
 x6 = remove(x4, x5)
 x7 = order(x6, identity)
 x8 = first(x7)
 x9 = last(x7)
 x10 = ofcolor(I, x8)
 x11 = ofcolor(I, x9)
 x12 = switch(I, x9, x8)
 x13 = combine(x10, x11)
 x14 = subgrid(x13, x12)
 x15 = trim(x14)
 return x15
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]