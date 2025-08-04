exec(open('dsl/task400.py').read(),globals())
def p(g):return[list(r)for r in verify_task400(tuple(map(tuple,g)))]

