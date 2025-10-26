def p(g):
 A=sum(g,[]);b=min(A,key=A.count)
 d=[sum({*r}&{x[i]for x in g})-b for r in g for i,v in enumerate(r)if v==b]
 return [[max(d,key=d.count)]]