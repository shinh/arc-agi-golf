p=lambda g,e=enumerate:next([[v]]for i,r in e(g)for j,v in e(r)if 7<sum(g[i+d][j-1:j+2].count(x)for d in(-1,0,1)if(x:=r[j-1])))# find intruder's center color by counting left color in 3x3
