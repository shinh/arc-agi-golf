# extend colors to 3
p=lambda g,n=3,u=0:-n*g or p([[[c,u:=[u,c,0][((e:=3 in r[x:])*(c>0))+(c==3)]][c<1and e]for x,c in enumerate(r)]for r in zip(*g[::-1])],n-1)
