# tile w rotations
p=lambda g:(g:=[a+[*b]for a,b in zip(g,zip(*g[::-1]))])+[y[::-1]for y in g[::-1]]
