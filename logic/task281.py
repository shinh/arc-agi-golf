def p(g):
        # surround non-unique colors with a frame including the lone cell
        w=len(g[0]);f=sum(g,[])
        i=[i for i,v in enumerate(f)if f.count(v)<2<v+2][0];u=f[i]
        Y,X=zip(*[(i//w,i%w)for i,v in enumerate(f)if 0<v!=u])
        t=min(Y);b=max(Y);l=min(X);r=max(X);B,C=g[t][l],g[t+1][l+1]
        t=min(t,i//w);b=max(b,i//w);l=min(l,i%w);r=max(r,i%w)
        return [[(l<=x<=r)*(t<=y<=b)*(B*(y in(t,b) or x in(l,r)) or C) for x in range(w)]for y in range(len(g))]
