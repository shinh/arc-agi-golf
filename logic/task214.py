def p(g):# rot+mirror
 h=g[::-1]
 for r,t,u in zip(g,h,zip(*h)):
  r[4:7],r[8:]=u,t[2::-1]
 return g
