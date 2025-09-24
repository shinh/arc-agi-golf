def p(g,e=enumerate):
 s=sum(i*60+j for i,r in e(g)for j,v in e(r)if v)//2;y=s//60;x=s%30
 for i in-1,0,1:g[y+i][x]=g[y][x+i]=3
 return g#cross
