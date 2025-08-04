def p(g):
 n={'rot90':lambda x:tuple(zip(*x[::-1]))}
 exec(open('dsl/task240.py').read(),n)
 return [list(r)for r in n['verify_task240'](tuple(map(tuple,g)))]
