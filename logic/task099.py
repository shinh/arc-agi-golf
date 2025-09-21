def p(g):
 #expand color cells to their surrounding frame of 1's
 for y,R in enumerate(g):
  for x,c in enumerate(R):
   if c>1:
    l=r=x;u=d=y
    while R[l]-1:l-=1
    while R[r]-1:r+=1
    while u and 1 in g[u-1][l:r+1]:u-=1
    while d-9 and 1 in g[d+1][l:r+1]:d+=1
    for S in g[u-(u>0):d+1]:S[l:r+1]=[v==1 or c for v in S[l:r+1]]
 return g
