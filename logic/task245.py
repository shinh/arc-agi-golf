# shift 2s below-right of the top-left 3
def p(g):
 R=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==3]
 P=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2]
 a,b=min(R);c,d=map(min,zip(*P))
 o=[[v*(v==3)for v in r]for r in g]
 for y,x in P:o[y+a-c+1][x+b-d+1]=2
 return o
