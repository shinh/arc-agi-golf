p=lambda g:next([[r[j]]]for i,r in enumerate(g)for j in range(len(r)-1)if r[j-1]and sum(g[i+di][j+dj]==r[j-1]for di in(-1,0,1)for dj in(-1,0,1))>7)# find intruder's center color
