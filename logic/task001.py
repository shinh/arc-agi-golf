# 61 - pairwise AND of rows/cols
p=lambda g:[[a&b for a in r for b in s]for r in g for s in g]

