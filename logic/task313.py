def p(g):#tile shift
 s=range(len(g));return[[g[i%g.index(r:=g[0],1)][-~j%~-len({*r})]for j in s]for i in s]

