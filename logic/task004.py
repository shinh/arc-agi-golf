# Shift each color right except bottom and right edges.
def p(g):
 S={};i=len(g)
 while i:
  r=g[i:=i-1];j=len(r)
  while j:
   if(v:=r[j:=j-1]):b,m=S[v]=S.get(v,(i,j));k=i<b;k&=j<m;r[j+k]=v;r[j]-=v*k
 return g
