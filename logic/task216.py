# densest block
p=lambda a:max((sum(sum(b,[]))-w*h,w*h,b)for y in range(20)for c in range(20)for w,h in[((a[y][c:]+[0]).index(0),([r[c]for r in a[y:]]+[0]).index(0))]for b in[[r[c:c+w]for r in a[y:y+h]]])[2]
