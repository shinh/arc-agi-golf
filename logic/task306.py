def p(g):
 for a,b in zip(g,g[10:]):d=max((s:=max(a,b))[:9],s[10:19],s[~8:]);b[:]=a[:]=d+([4]+d)*s.count(4)
 return g
