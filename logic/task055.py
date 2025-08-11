def p(g,d=0,b=b'\0\2\0\4\6\3\0\1\0'):
 for r in g:
  d+=r[0]>0;x=0
  for i,v in enumerate(r):
   r[i]=v or b[d*3+x];x+=v>0
 return g
