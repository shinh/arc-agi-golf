def p(a):
 r=next(filter(any,a));s=r.index(v:=max(r))+15-r[::-1].index(v)
 return [[v*(v in r[x:x+1]+r[s-x:s-x+1])for x in range(16)]for r in a]