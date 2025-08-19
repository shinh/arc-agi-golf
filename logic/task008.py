import re
def p(g):
    for o in range(40):
        #print(g,"2, 8"not in str(g),re.(r"2, 0[,0 ]+8",str(g)))
        if re.search(r"2, 0[,0 ]+8",str(g))and"2, 8"not in str(g):
            g=[[[0,8,2,8][(c>7)+(p==2)*2]for c,p in zip(r,[0]+r)]for r in g]

        g=[*map(list,zip(*g[::-1]))]
    return g
