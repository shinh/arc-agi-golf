def fork(
 outer,
 a,
 b
):
 return lambda x: outer(a(x), b(x))
def matcher(
 function,
 target
):
 return lambda x: function(x) == target
def apply(
 function,
 container
):
 return type(container)(function(e) for e in container)
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
def compose(
 outer,
 inner
):
 return lambda x: outer(inner(x))
def flip(
 b
):
 return not b
def combine(
 a,
 b
):
 return type(a)((*a, *b))
def mostcolor(
 element
):
 values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
 return max(set(values), key=values.count)
def identity(
 x
):
 return x
def verify_task032(I):
 x0 = mostcolor(I)
 x1 = rot270(I)
 x2 = matcher(identity, x0)
 x3 = rbind(sfilter, x2)
 x4 = compose(flip, x2)
 x5 = rbind(sfilter, x4)
 x6 = fork(combine, x3, x5)
 x7 = apply(x6, x1)
 x8 = rot90(x7)
 return x8
def p(g):
 return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]