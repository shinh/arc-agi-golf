def show(g,msg=None,yx=None):
    if msg:
        print(msg)
    if yx is not None:
        print(yx)
    for y,r in enumerate(g):
        a=[]
        for x,c in enumerate(r):
            s=str(c)
            if yx is not None:
                if yx[0]==y and yx[1]==x:
                    s="\033[42m"+s+"\033[0m"
            a.append(s)
        print("".join(a))