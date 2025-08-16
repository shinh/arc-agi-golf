def p(g):# rot+mirror
 for r,t,u in zip(g,h:=g[::-1],zip(*h)):r[4:7],r[8:]=u,t[2::-1]
 return g
