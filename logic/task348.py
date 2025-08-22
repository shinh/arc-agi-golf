# alternate columns expanding from marker
p=lambda g:(x:=g[0].index(7),h:=sum(r[x]>0 for r in g),[len(g[0])>x+j>=0 and g[y].__setitem__(x+j,7+j%2)for y in range(h)for j in range(y-h+1,h-y)])and g
