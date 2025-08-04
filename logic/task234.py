n={}
exec(open('dsl/task234.py').read(),n)
def p(g):return [list(r)for r in n['verify_task234'](tuple(map(tuple,g)))]
