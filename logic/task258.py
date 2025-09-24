# fill between nonzero neighbors
p=lambda g:[[[b,2][a*c>0]for a,b,c in zip([0]+r,r,r[1:]+[0])]for r in g]
