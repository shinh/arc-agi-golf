from importlib.machinery import SourceFileLoader as L
f=L('y','dsl/task074.py').load_module().verify_task074
def p(g):
 return [list(r)for r in f(tuple(map(tuple,g)))]
