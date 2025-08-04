n={}
exec(open('dsl/task046.py').read().rsplit('def p',1)[0],n)
f=n['verify_task046']
def p(g):
    return [list(r)for r in f(tuple(map(tuple,g)))]
