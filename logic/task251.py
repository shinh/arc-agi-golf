# rotate with zip(*g[::-1]) so 0 only needs to flow right
p=lambda g,n=65:n>64 and p([[c or 1 for c in r]for r in g],64)or n and p([[a*(a>1 or b>0)for a,b in zip(r,r[1:]+(0,))]for r in zip(*g[::-1])],n-1)or g
