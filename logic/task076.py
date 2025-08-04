exec(open('dsl/task076.py').read(),globals())
def p(g):
 return [list(r)for r in verify_task076(tuple(map(tuple,g)))]
