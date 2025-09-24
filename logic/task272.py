# halve cell if no nonzero neighbors
p=lambda g,z=[0]:[[v>>1-any(t)for v,t in zip(r,zip(z+r,r[1:]+z,pr,nr))]for r,pr,nr in zip(g,[z*9]+g,g[1:]+[z*9])]

