# draw lines
def p(g):
 r=range(9)
 (a,b,c),(d,e,f)=[(i,j,v)for i in r for j in r if(v:=g[i][j])]
 for i in r:g[a][i]=g[i][b]=c;g[d][i]=g[i][e]=f;g[a][e]=g[d][b]=2
 return g
