def p(g):
 # bridge shapes with 8
 def b(k):
  y=[i for i,r in enumerate(g) if k in r]
  x=[i for i,c in enumerate(zip(*g)) if k in c]
  return y[0],y[-1],x[0],x[-1]
 a,b=[b(c) for c in {v for r in g for v in r if v}]
 c=a[3]<b[2] or b[3]<a[2]
 if a[c*2]>b[c*2]:a,b=b,a
 s,t,u,v=[(a[1]+1,b[0],max(a[2],b[2])+1,min(a[3],b[3])),(max(a[0],b[0])+1,min(a[1],b[1]),a[3]+1,b[2])][c]
 for r in g[s:t]:r[u:v]=[8]*(v-u)
 return g
