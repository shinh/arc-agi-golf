# fill row if ends match
p=lambda g:[r[:1]*10*(r[0]==r[9]>0)or r for r in g]
