def p(g,d=0,b=b'020463010'):
 # fill empty cells from template using counts of dividers
 for r in g:d+=r[0]>0;x=0;r[:]=[(x:=x+(v>0),v)[1]or b[d*3+x]^48for v in r]
 return g
