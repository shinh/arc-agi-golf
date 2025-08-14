# rotate the image 90 degrees 4x times with zip(*g[::-1]) instead of applying logic at 4 different directions
p=lambda g,n=63:-n*g or p([[[a or b==1,a^1-(a>1)][n<1]for a,b in zip(r,r[1:]+(1,))]for r in zip(*g[::-1])],n-1)

