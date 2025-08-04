exec(open('dsl/task090.py').read(),globals())
def p(g):
 return [list(r)for r in verify_task090(tuple(map(tuple,g)))]
