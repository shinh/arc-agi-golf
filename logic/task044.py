from collections import Counter

def apply(f,c):
    return type(c)(f(e) for e in c)

def argmax(c,f):
    return max(c,key=f,default=None)

def toindices(p):
    if not p:return frozenset()
    if isinstance(next(iter(p))[1],tuple):
        return frozenset(i for v,i in p)
    return p

def leftmost(p):
    return min(j for i,j in toindices(p))

def lowermost(p):
    return max(i for i,j in toindices(p))

def rightmost(p):
    return max(j for i,j in toindices(p))

def uppermost(p):
    return min(i for i,j in toindices(p))

def bordering(p,g):
    h,w=len(g),len(g[0])
    return uppermost(p)==0 or leftmost(p)==0 or lowermost(p)==h-1 or rightmost(p)==w-1

def chain(h,g,f):
    return lambda x:h(g(f(x)))

def color(o):
    return next(iter(o))[0]

def colorfilter(os,v):
    return frozenset(o for o in os if next(iter(o))[0]==v)

def compose(o,i):
    return lambda x:o(i(x))

def fill(g,v,p):
    h,w=len(g),len(g[0]);r=[list(row)for row in g]
    for i,j in toindices(p):
        if 0<=i<h and 0<=j<w:r[i][j]=v
    return tuple(tuple(row)for row in r)

def mostcolor(e):
    vals=[v for r in e for v in r] if isinstance(e,tuple) else [v for v,_ in e]
    return max(set(vals),key=vals.count)

def cover(g,p):
    return fill(g,mostcolor(g),toindices(p))

def difference(a,b):
    return type(a)(e for e in a if e not in b)

def flip(b):
    return not b

def fork(o,a,b):
    return lambda x:o(a(x),b(x))

def identity(x):
    return x

def lbind(f,fixed):
    n=f.__code__.co_argcount
    if n==2:return lambda y:f(fixed,y)
    if n==3:return lambda y,z:f(fixed,y,z)
    return lambda y,z,a:f(fixed,y,z,a)

def merge(cs):
    return type(cs)(e for c in cs for e in c)

def mapply(f,c):
    return merge(apply(f,c))

def matcher(f,t):
    return lambda x:f(x)==t

def mostcommon(c):
    return max(set(c),key=c.count)

def dneighbors(l):
    i,j=l;return frozenset({(i-1,j),(i+1,j),(i,j-1),(i,j+1)})

def ineighbors(l):
    i,j=l;return frozenset({(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)})

def neighbors(l):
    return dneighbors(l)|ineighbors(l)

def shift(p,d):
    if not p:return p
    di,dj=d
    if isinstance(next(iter(p))[1],tuple):
        return frozenset((v,(i+di,j+dj))for v,(i,j) in p)
    return frozenset((i+di,j+dj)for i,j in p)

def normalize(p):
    if not p:return p
    return shift(p,(-uppermost(p),-leftmost(p)))

def add(a,b):
    if isinstance(a,int) and isinstance(b,int):return a+b
    if isinstance(a,tuple) and isinstance(b,tuple):return (a[0]+b[0],a[1]+b[1])
    if isinstance(a,int) and isinstance(b,tuple):return (a+b[0],a+b[1])
    return (a[0]+b,a[1]+b)

def asindices(g):
    return frozenset((i,j)for i in range(len(g))for j in range(len(g[0])))

def objects(g,univalued,diagonal,without_bg):
    bg=mostcolor(g) if without_bg else None
    obs=set();occ=set();h,w=len(g),len(g[0]);unv=asindices(g);diag=neighbors if diagonal else dneighbors
    for loc in unv:
        if loc in occ:continue
        val=g[loc[0]][loc[1]]
        if val==bg:continue
        obj={(val,loc)};cands={loc}
        while cands:
            nb=set()
            for cand in cands:
                v=g[cand[0]][cand[1]]
                if (val==v) if univalued else (v!=bg):
                    obj.add((v,cand));occ.add(cand)
                    nb|={(i,j)for i,j in diag(cand) if 0<=i<h and 0<=j<w}
            cands=nb-occ
        obs.add(frozenset(obj))
    return frozenset(obs)

def paint(g,o):
    h,w=len(g),len(g[0]);r=[list(row)for row in g]
    for v,(i,j) in o:
        if 0<=i<h and 0<=j<w:r[i][j]=v
    return tuple(tuple(row)for row in r)

def rbind(f,fixed):
    n=f.__code__.co_argcount
    if n==2:return lambda x:f(x,fixed)
    if n==3:return lambda x,y:f(x,y,fixed)
    return lambda x,y,z:f(x,y,z,fixed)

def recolor(v,p):
    return frozenset((v,i) for i in toindices(p))

def sfilter(c,cond):
    return type(c)(e for e in c if cond(e))

def toobject(p,g):
    h,w=len(g),len(g[0])
    return frozenset((g[i][j],(i,j)) for i,j in toindices(p) if 0<=i<h and 0<=j<w)

def totuple(c):
    return tuple(c)

def verify_task044(I):
    x0=mostcolor(I)
    x1=objects(I,True,True,False)
    x2=colorfilter(x1,x0)
    x3=compose(normalize,toindices)
    x4=difference(x1,x2)
    x5=rbind(bordering,I)
    x6=compose(flip,x5)
    x7=sfilter(x2,x6)
    x8=rbind(toobject,I)
    x9=lbind(mapply,neighbors)
    x10=compose(x9,toindices)
    x11=fork(difference,x10,identity)
    x12=chain(mostcolor,x8,x11)
    x13=totuple(x7)
    x14=apply(x12,x13)
    x15=mostcommon(x14)
    x16=matcher(x12,x15)
    x17=sfilter(x7,x16)
    x18=lbind(argmax,x4)
    x19=lbind(matcher,x3)
    x20=chain(x18,x19,x3)
    x21=compose(color,x20)
    x22=fork(recolor,x21,identity)
    x23=mapply(x20,x17)
    x24=cover(I,x23)
    x25=mapply(x22,x17)
    x26=paint(x24,x25)
    return x26

def p(g):
    return [list(r)for r in verify_task044(tuple(tuple(r)for r in g))]
