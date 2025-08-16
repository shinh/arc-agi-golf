def p(g):
    # drop empty & duplicate rows/cols
    for _ in"00":g=map(list,zip(*dict.fromkeys(map(tuple,filter(any,g)))))
    return[*g]
