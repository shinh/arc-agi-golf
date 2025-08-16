def p(g):
    # mirror TL mask
    h=len(g)//2;g=[[v and g[h][0]for v in r[:h]]for r in g[:h]]
    return[r+r[::-1]for r in g+g[::-1]]
