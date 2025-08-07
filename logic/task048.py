def f(x,y,g):
  global a;v.append((x,y))
  for k in R(x-1,x+2):
    for l in R(y-1,y+2):
      if (k,l) in v:continue
      v.append((k,l))
      if k<0 or k>=h or l<0 or l>=w or (k,l) in [(r,c),(r+1,c),(r,c+1),(r+1,c+1)]:continue
      if g[k][l]==2:a=8
      if g[k][l]==8:f(k,l,g)
def p(g):
  global a,v,r,c,h,w,R
  a,v,h,w,R,E=0,[],len(g),len(g[0]),range,enumerate
  for r,s in E(g):
    for c,d in E(s):
      if d==2:
        for x in R(r-1,r+3):
          for y in R(c-1,c+3):
            if x>=0 and x<h and y>=0 and y<w and g[x][y]==8:f(x,y,g)
        return [[a]]