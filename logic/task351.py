# Note task242 and task351 are very similar but best scores are quite different.
# Task242 53 bytes from theirs: 107 vs 54
# Task351 37 bytes from theirs: 107 vs 70
# Task400 37 bytes from theirs: 107 vs 70
p=lambda g:[e for r in g*1if(e:=[d for c,d in zip(r,g.pop()[::-1])if c==3])]
