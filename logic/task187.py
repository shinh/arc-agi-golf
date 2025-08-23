# rotate grid flood edge0s to3 then0->2
p=lambda g,n=63:-n*g or p([[b or(2,(a==3)*3)[n>0]for a,b in zip((3,)+r,r)]for r in zip(*g[::-1])],n-1)
