def p(g,d=0,b='020463010'):
 # fill empty cells from template using counts of dividers
 for r in g:
  d+=r[0]>0;x=0
  r[:]=[(x:=x+(v>0))and v or int(b[d*3+x])for v in r]
 return g
