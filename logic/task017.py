def p(g,a=1):
 A=range(21);m={}
 return all((v:=g[i][j])<1 or m.setdefault((i%a,j%a),v)==v for i in A for j in A)and[[g[i][j]or m[i%a,j%a]for j in A]for i in A]or p(g,a+1)