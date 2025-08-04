def p(g):
 n={};exec(open('dsl/task191.py').read(),n);
 return [list(r)for r in n['verify_task191'](tuple(map(tuple,g)))]
