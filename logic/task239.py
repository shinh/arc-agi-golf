def p(g):
 # histogram
 t=sum(g,[]);q=t.count;d=sorted({*t}-{0},key=q)[::-1]
 return[[c*(i<q(c))for c in d]for i in range(q(d[0]))]
