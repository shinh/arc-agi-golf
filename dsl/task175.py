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
DOWN_LEFT = (1, -1)
def recolor(
 value,
 patch
):
 return frozenset((value, index) for index in toindices(patch))
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
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
def lrcorner(
 patch
):
 return tuple(map(max, zip(*toindices(patch))))
def vmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(row[::-1] for row in piece)
 d = ulcorner(piece)[1] + lrcorner(piece)[1]
 if isinstance(next(iter(piece))[1], tuple):
  return frozenset((v, (i, d - j)) for v, (i, j) in piece)
 return frozenset((i, d - j) for i, j in piece)
def cmirror(
 piece
):
 if isinstance(piece, tuple):
  return tuple(zip(*(r[::-1] for r in piece[::-1])))
 return vmirror(dmirror(vmirror(piece)))
def product(
 a,
 b
):
 return frozenset((i, j) for j in b for i in a)
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
def insert(
 value,
 container
):
 return container.union(frozenset({value}))
def toobject(
 patch,
 grid
):
 h, w = len(grid), len(grid[0])
 return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
def branch(
 condition,
 if_value,
 else_value
):
 return if_value if condition else else_value
def ofcolor(
 grid,
 value
):
 return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def dneighbors(
 loc
):
 return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
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
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def initset(
 value
):
 return frozenset({value})
def argmin(
 container,
 compfunc
):
 return min(container, key=compfunc, default=None)
def first(
 container
):
 return next(iter(container))
def last(
 container
):
 return max(enumerate(container))[1]
def equality(
 a,
 b
):
 return a == b
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def flip(
 b
):
 return not b
ORIGIN = (0, 0)
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
def astuple(
 a,
 b
):
 return (a, b)
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
def shoot(
 start,
 direction
):
 return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))
def urcorner(
 patch
):
 return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))
def size(
 container
):
 return len(container)
def positive(
 x
):
 return x > 0
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
def difference(
 a,
 b
):
 return type(a)(e for e in a if e not in b)
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def asobject(
 grid
):
 return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))
def verify_task175(I):
 x0 = palette(I)
 x1 = asindices(I)
 x2 = urcorner(x1)
 x3 = index(I, ORIGIN)
 x4 = shoot(ORIGIN, UNITY)
 x5 = recolor(x3, x4)
 x6 = index(I, x2)
 x7 = shoot(x2, DOWN_LEFT)
 x8 = recolor(x6, x7)
 x9 = astuple(dmirror, x5)
 x10 = astuple(cmirror, x8)
 x11 = initset(x10)
 x12 = insert(x9, x11)
 x13 = product(x0, x12)
 x14 = asobject(I)
 x15 = lbind(sfilter, x14)
 x16 = lbind(compose, flip)
 x17 = lbind(matcher, first)
 x18 = chain(x15, x16, x17)
 x19 = lbind(paint, I)
 x20 = compose(last, last)
 x21 = compose(first, last)
 x22 = lbind(fork, equality)
 x23 = rbind(x22, identity)
 x24 = compose(x18, first)
 x25 = compose(x23, x21)
 x26 = compose(initset, x21)
 x27 = fork(rapply, x26, x24)
 x28 = compose(first, x27)
 x29 = compose(x19, x28)
 x30 = fork(paint, x29, x20)
 x31 = compose(initset, x25)
 x32 = fork(rapply, x31, x30)
 x33 = compose(first, x32)
 x34 = sfilter(x13, x33)
 x35 = lbind(colorcount, I)
 x36 = compose(x35, first)
 x37 = argmin(x34, x36)
 x38 = first(x37)
 x39 = last(x37)
 x40 = first(x39)
 x41 = last(x37)
 x42 = last(x41)
 x43 = x18(x38)
 x44 = x40(x43)
 x45 = paint(I, x44)
 x46 = paint(x45, x42)
 x47 = ofcolor(x46, x38)
 x48 = mapply(dneighbors, x47)
 x49 = difference(x48, x47)
 x50 = toobject(x49, x46)
 x51 = size(x50)
 x52 = positive(x51)
 x53 = rbind(astuple, x38)
 x54 = compose(last, x53)
 x55 = branch(x52, mostcolor, x54)
 x56 = x55(x50)
 x57 = replace(x46, x38, x56)
 return x57
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]