# extend colors to 3
p=lambda g,n=3,u=0:-n*g or p([[(u:=(c!=3)*(3 in r[x:])*(c or u)) or c for x,c in enumerate(r)]for r in zip(*g[::-1])],n-1)

