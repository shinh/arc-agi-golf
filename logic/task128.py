# rot90 -> shift -> rot270
p=lambda g:[*map(list,zip(*(([0]*r.index(0)+[*r])[:15]for r in zip(*g[::-1]))))][::-1]
