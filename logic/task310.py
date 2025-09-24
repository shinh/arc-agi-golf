# box rare color
def p(m):
 b=sum(m,[])
 return(s:={*b}-{0})and(w:=len(m[0]),i:=b.index(l:=min(s,key=b.count)),q:=b[::-1].index(l))and[r[i%w:w-q%w]for r in m[i//w:len(m)-q//w]]or[]
