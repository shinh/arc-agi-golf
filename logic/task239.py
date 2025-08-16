def p(g):
 # histogram
 t=sum(g,[]);d=sorted((-t.count(c),c)for c in{*t}-{0})
 return [[c*(-n>i)for n,c in d]for i in range(-d[0][0])]
