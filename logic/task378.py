from re import sub;p=lambda g,k=3:k<0 and g or p(eval(sub(r'(0)(?=.{%d}(?:.{%d}){0,9}([1-9]).{2}\2.{%d}\2.{2}0.{%d}([1-9]))'%((n:=len(g)*3+4),n+1,n-6,n),r'\3',str([*zip(*g[::-1])]))),k-1)
