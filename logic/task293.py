# fill rows or columns from first cell
p=lambda g,h=lambda g:[[r[0]or v for v in r]for r in g],z=zip:(c:=h(g),[*map(list,z(*h(z(*g))))])[c==g]
