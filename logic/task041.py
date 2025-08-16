def p(g,z=0):
 for r in g:r[:]=[(z:=x*(z<1)) or x if x else z for x in r]#toggle fill
 return g