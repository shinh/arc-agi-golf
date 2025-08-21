# def p(g):
#     # +g[:5] is to workaround a single corner case.
#     #f=lambda x:[*map(list,zip(*filter(lambda r:min(f:=[c for r in g+g[:5]for c in{*r}],key=f.count)in r,x)))]
#     #return f(f(g))
#     return(f:=lambda x:[*map(list,zip(*filter(lambda r:min(f:=[c for r in g+g[:5]for c in{*r}],key=f.count)in r,x)))])(f(g))
#     #return[*map(list,eval('zip(*filter(lambda r:min(f:=[c for r in g+g[:5]for c in{*r}],key=f.count)in r,'*2+'g))))'))]

p=lambda g:(f:=lambda x:[*zip(*[r for r in x if min(f:=[c for r in g+g[:5]for c in{*r}],key=f.count)in r])])(f(g))
