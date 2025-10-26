# tile period fill
R=range(21)
p=lambda g,a=1:(len(d:=dict((t:={((i%a,j%a),v)for i in R for j in R if(v:=g[i][j])})))^len(t)and p(g,a+1)or[[g[i][j]or d[i%a,j%a]for j in R]for i in R])
