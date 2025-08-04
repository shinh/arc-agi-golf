import dsl.task018 as t

def rot90(p):
    if isinstance(p,tuple):return tuple(zip(*p[::-1]))
    q=frozenset((v,(j,-i))for v,(i,j) in p) if isinstance(next(iter(p))[1],tuple) else frozenset((j,-i)for i,j in p)
    return t.normalize(q)
rot180=lambda p:rot90(rot90(p))
rot270=lambda p:rot90(rot180(p))
t.rot90=rot90;t.rot180=rot180;t.rot270=rot270

def p(g):
    return [list(r) for r in t.verify_task018(tuple(map(tuple,g)))]
