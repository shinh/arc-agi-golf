# rotate the grid and flood fill border-connected zeros with 3, then turn remaining zeros into 2
p=lambda g,n=64:n and p([[(a or(b==3)*3,a or 2)[n<2]for a,b in zip(r,r[1:]+(3,))]for r in zip(*g[::-1])],n-1)or g
