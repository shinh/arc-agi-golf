# tile period fill
R=range(21)
def p(g,a=1):
 t={((i%a,j%a),v)for i in R for j in R if(v:=g[i][j])}
 return(len((d:=dict(t)))^len(t)and p(g,a+1)or[[g[i][j]or d[i%a,j%a]for j in R]for i in R])
