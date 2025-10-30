# densest block
R=range(20)
p=lambda a:max((sum(sum((b:=[r[c:c+w]for r in a[y:y+h]]),[]))-w*h,w*h,b)for y in R for c in R for w,h in[((a[y][c:]+[0]).index(0),([*zip(*a)][c][y:]+(0,)).index(0))])[2]
