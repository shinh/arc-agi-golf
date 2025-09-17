p=lambda g,e=enumerate:[[v or g[i%6][j%6]and g[5][0]for j,v in e(r)]for i,r in e(g)]#copypatternblocks
