# fill rows or columns from first cell
p=lambda g,h=lambda g:[[r[0]or v for v in r]for r in g]:(c:=h(g),[*zip(*h(zip(*g)))])[c==g]
