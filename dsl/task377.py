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
def vconcat(
 a,
 b
):
 return a + b
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def hmirror(
 piece
):
 if isinstance(piece, tuple):
  return piece[::-1]
 d = ulcorner(piece)[0] + lrcorner(piece)[0]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (d - i, j)) for v, (i, j) in piece)
 return frozenset((d - i, j) for i, j in piece)
def dedupe(
 iterable
):
 return tuple(e for i, e in enumerate(iterable) if iterable.index(e) == i)
def last(
 container
):
 return max(enumerate(container))[1]
def identity(
 x
):
 return x
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def verify_task377(I):
 x0 = compose(dmirror, dedupe)
 x1 = x0(I)
 x2 = x0(x1)
 x3 = fork(remove, last, identity)
 x4 = compose(hmirror, x3)
 x5 = fork(vconcat, identity, x4)
 x6 = x5(x2)
 x7 = dmirror(x6)
 x8 = x5(x7)
 return x8
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]