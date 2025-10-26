def p(a):
 r,c,h,w=max((sum(sum(x[c:][:w])for x in a[r:][:h])-h*w,h*w,r,c,h,w)for r in range(20)for c in range(20)for w,h in[((a[r][c:]+[0]).index(0),([x[c]for x in a[r:]]+[0]).index(0))])[2:]
 return[x[c:][:w]for x in a[r:][:h]]