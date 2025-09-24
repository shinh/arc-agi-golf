# rot90 -> shift -> rot270
# 84 vs 72 vs 69
#p=lambda g:[*map(list,zip(*([*r[-r.index(0):],*r][:15]for r in zip(*g[::-1]))))][::-1]
# columns rotated upward by their zero counts
p=lambda g:[*zip(*(c[-(k:=c.count(0)):]+c[:-k]for c in zip(*g)))]
# relying on zip to trim
#p=lambda g:[*map(list,zip(*(([0]*r.index(0)+[*r])[:15]for r in zip(*g[::-1]))))][::-1]
