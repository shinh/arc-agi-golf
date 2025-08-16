t=lambda g:list(map(list,zip(*g)))
def p(g):
 #drop3sunder2add8
 h,w=len(g),len(g[0])
 if w>h:return t(p(t(g)))
 s=sum(g,[]);a=s.index(2)//w;b=s.index(3)//w;c=h-1-s[::-1].index(3)//w
 if b<a:return p(g[::-1])[::-1]
 return g[:a+1]+g[b:c+1]+[[8]*w]+[[0]*w]*(h-a+b-c-3)

