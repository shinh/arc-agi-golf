def p(g):
 # merge blocks separated by empty rows/cols, keep first colors
 a=sum;C=[];k=n=0
 for c in zip(*g):C+=k,;k+=a(c)<1;a(c)and(n:=k+1)
 o=[];k=0
 for r in g:
  if a(r):
   o+=[[0]*n]*(k==len(o))
   for c,v in zip(C,r):o[k][c]=o[k][c]or v
  else:k+=1
 return o

