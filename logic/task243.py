# spread 1s by rotating
p=lambda g,n=80:n and p([[a or(b==1)|0 for a,b in zip(r,r[1:]+(0,))]for r in zip(*g[::-1])],n-1)or g
