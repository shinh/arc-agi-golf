def p(a):
 # densest block
 return max((sum(sum(r)-w for r in b),w*len(b),b)for y in range(20)for c in range(20)for w in[(a[y][c:]+[0]).index(0)]for b in[[r[c:c+w]for r in a[y:y+([r[c]for r in a[y:]]+[0]).index(0)]]])[2]

