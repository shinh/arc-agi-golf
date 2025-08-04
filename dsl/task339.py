ONE = 1
ZERO = 0
def astuple(
 a,
 b
):
 return (a, b)
def canvas(
 value,
 dimensions
):
 return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))
def colorcount(
 element,
 value
):
 if isinstance(element, tuple):
  return sum(row.count(value) for row in element)
 return sum(v == value for v, _ in element)
def first(
 container
):
 return next(iter(container))
def remove(
 value,
 container
):
 return type(container)(e for e in container if e != value)
def other(
 container,
 value
):
 return first(remove(value, container))
def palette(
 element
):
 if isinstance(element, tuple):
  return frozenset({v for r in element for v in r})
 return frozenset({v for v, _ in element})
def verify_task339(I):
 x0 = palette(I)
 x1 = other(x0, ZERO)
 x2 = colorcount(I, x1)
 x3 = astuple(ONE, x2)
 x4 = canvas(x1, x3)
 return x4
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]