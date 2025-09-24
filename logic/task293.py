# fill rows or columns from first cell
p=lambda g,f=lambda r:[r[0]or v for v in r]:(c:=[*map(f,g)],[*zip(*map(f,zip(*g)))])[g==c]
