import base64
import re
import zlib


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


def add_indent(code):
    result = ""
    for line in code.splitlines():
        result += " " + line + "\n"
    return result


def concat(name, defs, reqs_map, seen):
    code = ""
    for r in reqs_map[name]:
        if r not in defs:
            continue
        if r in seen:
            continue
        seen.add(r)
        code += concat(r, defs, reqs_map, seen)
    code += defs[name]
    return code


def main():
    defs = {}
    cur_func = None
    for line in open("dsl.py").readlines():
        if m := re.match(r"^([A-Z_]+) = (.*)", line):
            defs[m.group(1)] = m.group(0)
        elif m := re.match(r"^def (\w+)\(", line):
            cur_func = m.group(1)
            defs[cur_func] = line
        elif re.match(r'^\s*""".*"""$', line):
            continue
        elif line.strip() == "":
            cur_func = None
        elif cur_func:
            defs[cur_func] += line

    for name, func in defs.items():
        func, _ = re.subn(r": [A-Z]\w+", "", func)
        func, _  = re.subn(r"\) -> [A-Z]\w+", ")", func)
        func = reindent(func) + "\n"
        # func, _ = re.subn(r"tuple", "list", func)
        defs[name] = func

    reqs_map = {}
    for name, func in defs.items():
        reqs = []
        for m in re.findall(r"([A-Z_]+|[a-z]+)", func):
            if m != name:
                reqs.append(m)
        reqs_map[name] = set(reqs)

    for task_id in range(1, 401):
        task_id_str = f"{task_id:03d}"
        name = "verify_task" + task_id_str

        func = concat(name, defs, reqs_map, set())

        dsl = func
        dsl += "def p(g):\n"
        dsl += f" return [list(r)for r in verify_task001(tuple(tuple(r) for r in g))]"
        open(f"dsl/task{task_id_str}.py", "w").write(dsl)

        body = add_indent(func)
        body += f" o=[list(r)for r in verify_task001(tuple(tuple(r) for r in g))]"

        # main = b"# -*- coding: latin-1 -*-\n"
        # main += b"import zlib\n"
        # main += b"def p(g):\n"
        # compressed = zlib.compress(body.encode())
        # chunks = []
        # for tok in compressed.split(b"\0"):
        #     chunks.append(b"r'''" + tok + b"'''")
        # compressed = b"+'\\0'+".join(chunks)
        # main += b" exec(" + compressed + b")\n"
        # main += b" return o\n"
        # open(f"cdsl/task{task_id_str}.py", "wb").write(main)

        main = "import base64,zlib\n"
        main += "def p(g):\n"
        compressed = base64.b85encode(zlib.compress(body.encode()))
        main += ' exec(base64.b85decode("' + compressed.decode() + '"))\n'
        main += " return o"
        open(f"cdsl/task{task_id_str}.py", "w").write(main)


if __name__ == "__main__":
    main()
