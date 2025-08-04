FOUR = 4
ONE = 1
TEN = 10
THREE = 3
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
def chain(
 h,
 g,
 f
):
 return lambda x: h(g(f(x)))
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
def equality(
 a,
 b
):
 return a == b
def first(
 container
):
 return next(iter(container))
def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def identity(
 x
):
 return x
def initset(
 value
):
 return frozenset({value})
def interval(
 start,
 stop,
 step
):
 return tuple(range(start, stop, step))
def last(
 container
):
 return max(enumerate(container))[1]
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
def tophalf(
 grid
):
 return grid[:len(grid) // 2]
def lefthalf(
 grid
):
 return rot270(tophalf(rot90(grid)))
def multiply(
 a,
 b
):
 if isinstance(a, int) and isinstance(b, int):
  return a * b
 elif isinstance(a, tuple) and isinstance(b, tuple):
  return (a[0] * b[0], a[1] * b[1])
 elif isinstance(a, int) and isinstance(b, tuple):
  return (a * b[0], a * b[1])
 return (a[0] * b, a[1] * b)
def pair(
 a,
 b
):
 return tuple(zip(a, b))
def positive(
 x
):
 return x > 0
def power(
 function,
 n
):
 if n == 1:
  return function
 return compose(function, power(function, n - 1))
def rapply(
 functions,
 value
):
 return type(functions)(function(value) for function in functions)
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
def sfilter(
 container,
 condition
):
 return type(container)(e for e in container if condition(e))
def size(
 container
):
 return len(container)
def verify_task039(I):
 x0 = lbind(apply, last)
 x1 = compose(positive, first)
 x2 = lbind(interval, ZERO)
 x3 = rbind(x2, ONE)
 x4 = rbind(sfilter, x1)
 x5 = compose(x3, size)
 x6 = fork(pair, x5, identity)
 x7 = chain(x0, x4, x6)
 x8 = rbind(branch, identity)
 x9 = rbind(x8, x7)
 x10 = chain(size, dedupe, first)
 x11 = lbind(equality, ONE)
 x12 = chain(x9, x11, x10)
 x13 = compose(initset, x12)
 x14 = fork(rapply, x13, identity)
 x15 = compose(first, x14)
 x16 = rbind(branch, identity)
 x17 = rbind(x16, x15)
 x18 = chain(x17, positive, size)
 x19 = compose(initset, x18)
 x20 = fork(rapply, x19, identity)
 x21 = compose(first, x20)
 x22 = multiply(TEN, THREE)
 x23 = power(x21, x22)
 x24 = compose(rot90, x23)
 x25 = power(x24, FOUR)
 x26 = x25(I)
 x27 = lefthalf(x26)
 x28 = tophalf(x27)
 return x28
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]