# draw bar in first row and center if count is four
p=lambda g,b=[0]*3:(n:=sum(sum(g,[])))and(([2]*n+b)[:3],(0,n//4*2,0),b)
