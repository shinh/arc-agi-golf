# Shift each color right except bottom and right edges.

def p(g):
 S={};i=len(g)
 while i:
  i-=1;r=g[i];j=len(r)
  while j:
   j-=1
   if(v:=r[j]):b,m=S.setdefault(v,(i,j));k=i<b and j<m;r[j],r[j+k]=v*(1-k),v
 return g
