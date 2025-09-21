# copy colors to horizontal neighbors then repeat rows
p=lambda g:[g[0],[*map(sum,zip(a:=[0,*g[0],0],a[2:]))]]*3
