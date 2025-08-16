# draw lines
def p(g):
 r=range(9)
 (a,b,c),(d,e,f)=[(i,j,g[i][j])for i in r for j in r if g[i][j]]
 o=[[c*(i==a or j==b)+f*(i==d or j==e)for j in r]for i in r];o[a][e]=o[d][b]=2
 return o
