def p(g):
    h=len(g);w=len(g[0])
    return [r[:w//2]for r in g] if w>h else g[:h//2]
