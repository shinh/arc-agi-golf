# draw bar in first row and center if count is four
p=lambda g,b=[0]*3:(n:=sum(sum(g,[])))and[([2]*n+b)[:3],(n>3)*[0,2,0]or b,b]
