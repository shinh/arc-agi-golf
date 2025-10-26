def p(a):
 r=next(filter(any,a));b=a.index(r);c=9-a[::-1].index(r)
 d=r.index(max(r));e=9-r[::-1].index(max(r))
 a[c+1][e+1],a[c+1][d-1],a[b-1][e+1],a[b-1][d-1]=a[b+1][d+1],a[b+1][e-1],a[c-1][d+1],a[c-1][e-1]
 a[b+1][d+1]=a[b+1][e-1]=a[c-1][d+1]=a[c-1][e-1]=0
 return a