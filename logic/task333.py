# extend colors to 3
p=lambda g,n=3,u=0:-n*g or p([[[c,(u:=(c*(e:=3 in r[x:])or u)*(c!=3))][e>c]for x,c in enumerate(r)]for r in zip(*g[::-1])],n-1)

