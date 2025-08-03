def p(g):
    a=sorted((x,c)for r in g for x,c in enumerate(r)if c)
    b=[]
    for i in range(0,len(a),3):
        c=[v for _,v in a[i:i+3]]
        if i//3%2:b+=c[::-1]
        else:b+=c
    b+=[0]*9
    return [b[i:i+3]for i in range(0,9,3)]
