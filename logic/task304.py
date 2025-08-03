def p(g):
 f=sum(g,[]);c=max(f,key=f.count)
 o=create(9,9)
 for i in range(3):
  for j in range(3):
   if g[i][j]==c:
    for k in range(3):o[i*3+k][j*3:j*3+3]=g[k]
 return o
