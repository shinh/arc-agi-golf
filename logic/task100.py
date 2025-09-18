#bbox rows*cols
def p(g):
 return[[max({*sum(g,[])}-{0},key=lambda c:sum(c in r for r in g)*sum(c in col for col in zip(*g)))]*2]*2

