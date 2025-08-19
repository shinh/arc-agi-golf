# 121
# boundary via neighbor xor
p=lambda g,h=[[0]*99]:[[a*(a^b|a^c|a^d|a^e>0)for a,b,c,d,e in zip(r,r[1:]+[0],[0]+r,u,d)]for r,u,d in zip(g,g[1:]+h,h+g)]
