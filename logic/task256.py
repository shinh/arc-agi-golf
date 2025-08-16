# grow triangles above and below the 2 row
def p(g,R=range):
 a=sum(g[i:=next(zip(*g)).index(2)])>>1
 for x in R(a+i):
  t=a+i-x;g[x][:t]=[2+(i>x)-(x>i)]*t
 return g

