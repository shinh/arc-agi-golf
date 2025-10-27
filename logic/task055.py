def p(g,d=0,b=b'020463010'):
 # fill empty cells from template using counts of dividers
 for r in g:d+=r[0]>0;x=d*3;r[:]=[(x:=x+(v>0))and v or b[x]^48for v in r]
 return g
