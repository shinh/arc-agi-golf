def show(g,msg=None):
    if msg:
        print(msg)
    for r in g:
        a=[]
        for c in r:
            a.append(str(c))
        print("".join(a))