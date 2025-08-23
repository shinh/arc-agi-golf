def p(g):
    # drop empty & duplicate rows/cols
    for _ in"00":g=zip(*dict.fromkeys(map(tuple,filter(any,g))))
    return*g,
