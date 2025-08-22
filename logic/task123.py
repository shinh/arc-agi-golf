# expand with repeating diagonal colors
p=lambda g,R=range(10):[[g[(m:=max(y,x)%(4+(g[4][4]>0)))][m]for x in R]for y in R]
