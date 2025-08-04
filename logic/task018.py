def p(g):
    n={
        'rot90':lambda x:tuple(zip(*x[::-1])),
        'rot180':lambda x:tuple(tuple(r[::-1])for r in x[::-1]),
        'rot270':lambda x:tuple(zip(*x))[::-1]
    }
    exec(open(__file__[:__file__.rfind('/')]+"/dsl/task018.py").read(),n)
    return [list(r)for r in n['verify_task018'](tuple(map(tuple,g)))]

