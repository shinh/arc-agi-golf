def p(g):
 n=len(g);p={};s=[]
 for a in range(n):
  for b in range(n):
   c=g[a][b]
   if 1<c<4:
    l=[(a,b)]
    for i,j in l:
     for x in-1,0,1:
      for y in-1,0,1:
       r=i+x;q=j+y
       if n>r>-1<q<n and g[r][q]and(r,q)not in l:l+=(r,q),
    if l[1:]:p[c]=[(i-a,j-b,g[i][j])for i,j in l]
    else:s+=[(a,b,c)]
 for a,b,c in s:
  for x,y,v in p[c]:g[a+x][b+(c*2-5)*y]=v
 return g
