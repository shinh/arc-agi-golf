def p(g):#frame 5-rect via set
 for i in (s:={i+i//10 for i in range(100)if sum(g,[])[i]>4}):g[i//11][i%11]=len({i-1,i+1,i-11,i+11}&s)*3%5
 return g
