import re


def reindent(code):
    lines = []
    cur_indent = 0
    prev_indent = 0
    indents = {}
    for line in code.splitlines():
        line = re.sub(r"#.*", "", line)
        line = line.rstrip()
        if not line:
            continue

        n = len(line) - len(line.lstrip())
        if n > prev_indent:
            cur_indent += 1
        elif n < prev_indent:
            cur_indent = indents[n]
        prev_indent = n
        indents[n] = cur_indent

        lines.append(" " * cur_indent + line.lstrip())
    return "\n".join(lines)


def squeeze(s):
    W='if for while try with class def else elif except finally'.split()
    L=s.split('\n');R=[];i=0
    while i<len(L):
        a=L[i];n=len(a)-len(a.lstrip());j=i+1;B=[];ok=1
        while j<len(L):
            c=L[j];m=len(c)-len(c.lstrip())
            if m<=n:break
            d=c.lstrip();w=d.split()
            if m>n+1 or ':'in d or w[:1]and w[0]in W:ok=0;break
            B+=[d];j+=1
        if ok and B and m<=n:R+=[a+B[0]+''.join(';'+x for x in B[1:])];i=j
        else:R+=[a];i+=1
    return'\n'.join(R)


def remove_spaces(code):
    # TODO: Consider not replacing code in string literals.
    code, _ = re.subn(r"(\S) +([\[({,:+\-*/%\]})])", r"\1\2", code)
    code, _ = re.subn(r"([\[({,:+\-*/%\]})]) +(\w)", r"\1\2", code)
    # o and x will be confused as octal/hex numbers.
    code, _ = re.subn(r"(\b[0-9]+) +([a-np-wyz])", r"\1\2", code)
    return code


def jam(s):
    W='if for while try with class def else elif except finally'.split()
    L=s.split('\n');bal=lambda t:sum((c in'([{')-(c in')]}')for c in t)
    h=lambda x:(m:=re.match('[a-z]+',x))and m.group()
    R=[L[0]];d=bal(L[0])
    for b in L[1:]:
        a=R[-1];n=len(a)-len(a.lstrip())
        if d==0 and n==len(b)-len(b.lstrip())and not a.rstrip().endswith(':'):
            if(h(a.lstrip())not in W and h(b.lstrip())not in W):
                R[-1]+=';'+b.lstrip();d+=bal(b);continue
        R+=[b];d+=bal(b)
    return'\n'.join(R)


def replce_fixed_range(code):
    code = code.replace("in range(2):", "in 0,1:")
    code = code.replace("in range(3):", "in 0,1,2:")
    code = code.replace("in range(4):", "in 0,1,2,3:")
    return code


def minify(code):
    code = reindent(code)
    code = squeeze(code)
    code = remove_spaces(code)
    code = jam(code)

    if len(code) < 150:
        # Bad with LZ.
        code = replce_fixed_range(code)

    return code
