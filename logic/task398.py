def p(g):#expand
 r=g[0];n=25-5*r.count(0);return[([0]*n+r+[0]*n)[i+1:i+1+n]for i in range(n)]
