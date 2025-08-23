def p(g):
 # copy quads
 s=sum(g,[]);f=s.index;r,c=divmod(f(8),10);o=create(10,10)
 for v in {*s}-{0,8}:o[r+((i:=f(v))//10>r)][c+(i%10>c)]=v
 return o
