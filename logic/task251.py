# rotate the image 90 degrees 4x times with zip(*g[::-1]) instead of applying logic at 4 different directions
# p=lambda g,n=64:n and p([[[a or b==1,a^1-(a>1)][n<2]for a,b in zip(r,r[1:]+(1,))]for r in zip(*g[::-1])],n-1)or g

import re
#p=lambda g:eval(re.subn(r"2, (0, )+2",lambda m:"2, "+"1, "*((m.endpos-m.pos-4)//3)+"2",str(g))[0])
def p(g):
    print(g)
    g=eval(re.subn(r"2, (0, )+(?=2)",lambda m:("2, "+"1, "*((m.endpos-m.pos-3)//60)),str(g))[0])
    show(g, "hoge")
    return g

