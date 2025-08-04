def p(g):
 n={}
 exec(open('dsl/task242.py').read(),n)
 return [list(r)for r in n['verify_task242'](tuple(map(tuple,g)))]
