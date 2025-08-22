def p(g):# border
    h,w=len(g),len(g[0])
    return[[8]*w,*[[8,*[0]*(w-2),8]]*(h-2),[8]*w]
