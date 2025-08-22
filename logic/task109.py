def p(g):
    # mirror TL mask
    h=len(g)//2;return[[v and g[h][0]for v in r[:h]+r[h-1::-1]]for r in g[:h]+g[h-1::-1]]
