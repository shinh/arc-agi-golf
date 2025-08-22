# 118
# boundary via neighbor set
p=lambda g,h=[[0]*30]:[[a*({b,c,d,e}!={a})for a,b,c,d,e in zip(r,r[1:]+[0],[0]+r,u,d)]for r,u,d in zip(g,g[1:]+h,h+g)]
