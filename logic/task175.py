def p(g,a=441):
 while a:a-=1;b=a//21;c=a%21;g[b][c]=g[b][c]or g[c][b]or g[b+1][c+1]
 return g