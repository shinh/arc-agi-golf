def p(g):
    a=g[0][0];o=create(3,3)
    if a==2:
        for i in range(3):o[i][i]=5
    elif a==3:
        for i in range(3):o[i][2-i]=5
    else:o[0]=[5]*3
    return o
