# row/col empty ->3.
def p(g):
 _,*t,_=g;_,*b,_=map(any,zip(*t))
 for r in t:_,*a,_=r;r[1:-1]=(x or-3*any(a)*y+3 for x,y in zip(a,b))
 return g
