def p(g):
 # bridge shapes with 8
 f=sum(g,[]);w=len(g[0])
 a,b=[(i:=f.index(c),j:=len(f)-1-f[::-1].index(c))and(i//w,j//w,i%w,j%w)for c in set(f)-{0}]
 c=a[3]<b[2]or b[3]<a[2]
 if a[c*2]>b[c*2]:a,b=b,a
 s,t,u,v=[(a[1]+1,b[0],max(a[2],b[2])+1,min(a[3],b[3])),(max(a[0],b[0])+1,min(a[1],b[1]),a[3]+1,b[2])][c]
 for r in g[s:t]:r[u:v]=[8]*(v-u)
 return g
