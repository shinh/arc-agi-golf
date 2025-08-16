# boundary via neighbor xor
p=lambda g,z=zip:(h:=[0]*len(g[0]),[[a*((a^b|a^c|a^d|a^e)>0)for a,b,c,d,e in z(r,r[1:]+[0],[0]+r,u,d)]for r,u,d in z(g,g[1:]+[h],[h]+g)])[1]
