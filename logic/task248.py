def p(g):
 #bounce bottom-left
 m=len(g[0])-1;k=len(g)
 for r in g:k-=1;r[~abs(k%(m*2)-m)]=1
 return g
