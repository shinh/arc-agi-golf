# copy colors to horizontal neighbors then repeat rows
p=lambda g:(a:=[0,*g[0],0])and(g[0],[*map(sum,zip(a,a[2:]))])*3
