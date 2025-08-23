# halve cell if no nonzero neighbors
p=lambda g,z=[0]:[[v>>(l|r|u|d<1)for v,l,r,u,d in zip(r,r[1:]+z,z+r,pr,nr)]for r,pr,nr in zip(g,[z*9]+g,g[1:]+[z*9])]

