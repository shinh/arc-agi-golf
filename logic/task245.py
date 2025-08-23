# shift 2s below-right of the top-left 3
def p(g):
 e=enumerate
 P=[(y,x)for y,r in e(g)for x,v in e(r)if v==2]
 a,b=min((y,x)for y,r in e(g)for x,v in e(r)if v==3)
 c,d=map(min,zip(*P))
 o=[[3*(v==3)for v in r]for r in g]
 for y,x in P:o[y+a-c+1][x+b-d+1]=2
 return o
