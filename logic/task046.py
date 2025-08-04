from importlib.machinery import SourceFileLoader as L
f=L('x','dsl/task046.py').load_module().verify_task046
def p(g):
 return [list(r)for r in f(tuple(map(tuple,g)))]
