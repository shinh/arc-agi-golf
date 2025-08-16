p=lambda g:next([[v]]for i,r in enumerate(g)for j,v in enumerate(r)if(k:=r[j-1])and sum(g[i+di][j-1:j+2].count(k)for di in(-1,0,1))>7)# find intruder's center color
