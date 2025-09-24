# cross
def p(g):
 a,b,c,d,e,f=sum(((i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v),())
 t=(a-d)**2<(b-e)**2
 if t:g=[*map(list,zip(*g))];a,b,d,e=b,a,e,d
 if a>d:a,b,c,d,e,f=d,e,f,a,b,c
 x,m=b,a+d>>1
 for i in range(a,d+1):g[i][x]=[c,0,f][(i>=m)+(i>m+1)]
 g[m-1][x-2:x+3]=[c]*5;g[m+2][x-2:x+3]=[f]*5
 g[m][x-2:x+3:4]=[c]*2;g[m+1][x-2:x+3:4]=[f]*2
 if t:g=[*map(list,zip(*g))]
 return g

