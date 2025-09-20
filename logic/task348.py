# alt cols
p=lambda g:(x:=g[0].index(7),h:=sum(r[x]>0for r in g),[[(abs(j-x)+y<h)*(7+(j+x&1))for j in range(len(r))]for y,r in enumerate(g)])[-1]
