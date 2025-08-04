import argparse
import base64
import lzma
import os
import re
import sys
import zlib

import code_golf_utils
import python_minifier


def write_code(code, filename):
    if isinstance(code, bytes):
        with open(filename, "wb") as f:
            f.write(code)
    else:
        with open(filename, "w") as f:
            f.write(code)


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


def inline_create(code):
    return re.sub(r"create\((\w+),(\w+)\)", r"[[0]*\2 for _ in range(int(\1))]", code)


def compress(code, algo="zlib"):
    first_line, *body_orig = code.splitlines()
    if first_line.strip() != "def p(g):":
        return code

    body = []
    has_return = False
    for line in body_orig:
        if "return" in line:
            if has_return:
                return code
            has_return = True
            line, _ = re.subn(r"return\s*","o=",line)
            line += ";1/0"
        body.append(line[1:])

    if algo == "zlib":
        main = "import base64,zlib\n"
        main += "def p(g):\n"
        main += " O={'g':g,'o':None}\n"
        compressed = base64.b85encode(zlib.compress("\n".join(body).encode(),9))
        main += ' try:exec(zlib.decompress(base64.b85decode("' + compressed.decode() + '")),O)\n'
        main += " except:0\n"
        main += " return O['o']\n"
    elif algo == "lzma":
        main = "import base64,lzma\n"
        main += "def p(g):\n"
        main += " O={'g':g,'o':None}\n"
        compressed = base64.b85encode(lzma.compress("\n".join(body).encode()))
        main += ' try:exec(lzma.decompress(base64.b85decode("' + compressed.decode() + '")),O)\n'
        main += " except:0\n"
        main += " return O['o']\n"

    if len(main) < len(code):
        print(f"Use compressed code! {len(code)} => {len(main)}")
        return main

    return code


def check_task(task_id, filename, verbose):
    if verbose:
        print(f"Checking === {filename} ===", flush=True)

    if not os.path.exists(filename):
        return False, "TODO", None

    kind = os.path.basename(os.path.dirname(filename))
    basedir = os.path.join("/tmp", kind)

    os.makedirs(basedir, exist_ok=True)

    result = "N/A"
    ok = False

    logic = open(filename).read()
    code = inline_create(logic)
    code = reindent(code)
    #code = squeeze(code)

    if task_id != 71:
        code = python_minifier.minify(code)
        zlib_code = compress(code,"zlib")
        lzma_code = compress(code,"lzma")
        if len(zlib_code) < len(code):
            if len(lzma_code) < len(zlib_code):
                code = lzma_code
            else:
                code = zlib_code
        elif len(lzma_code) < len(code):
            code = lzma_code

    task_path = f"{basedir}/task{task_id:03d}.py"
    write_code(code, task_path)

    try:
        examples = code_golf_utils.load_examples(int(task_id))
        if code_golf_utils.verify_program(task_id, examples, task_path, quiet=not verbose):
            result = str(2500 - len(code))
            ok = True
        else:
            result = "FAIL"
    except Exception as e:
        if verbose:
            raise
        result = "ERROR"

    return ok, result, code


def submit(task_id, verbose, skip_verify=False):
    if skip_verify:
        return

    # print("Submitting task", task_id)

    ok, result, code = check_task(task_id, f"logic/task{task_id:03d}.py", verbose)

    # dsl_filename = f"dsl/task{task_id:03d}.py"
    # if os.path.exists(dsl_filename) and os.path.getsize(dsl_filename) < 4000:
    #     ok_c, result_c, code_c = check_task(task_id, dsl_filename, verbose)
    #     lc = len(code_c)
    #     if ok_c and (not ok or lc < len(code_c)) and len(code_c) < 2500:
    #         ok = ok_c
    #         result = result_c + " (" + result + ")"
    #         code = code_c

    open(f"reports/task{task_id:03d}.txt", "w").write(result)
    if code:
        write_code(code, f"submissions/task{task_id:03d}.py")

    print(f"Task {task_id:03d}: {result}", flush=True)

    return ok


def report():
    score = 0
    fail_tests = []
    error_tests = []
    todo_tests = []
    negative_tests = []
    for task_id in range(1, 401):
        result = open(f"reports/task{task_id:03d}.txt").read()
        result = result.split()[0]
        if result == "FAIL":
            fail_tests.append(task_id)
        elif result == "ERROR":
            error_tests.append(task_id)
        elif result == "TODO":
            todo_tests.append(task_id)
        else:
            score += int(result)
            if int(result) < 0:
                negative_tests.append(task_id)
    print(f"Failed tests: {len(fail_tests)} {list(sorted(fail_tests))}")
    print(f"Error tests: {error_tests}")
    print(f"TODO tests: {len(todo_tests)} {list(sorted(todo_tests))}")
    if negative_tests:
        print(f"Negative tests: {len(negative_tests)} {list(sorted(negative_tests))}")
    print(f"Total score: {score}")


def main():
    parser = argparse.ArgumentParser(description="Submit code golf.")
    parser.add_argument("task_id")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--skip_verify", action="store_true")
    args = parser.parse_args()

    if args.task_id == "all":
        for task_id in range(1, 401):
            submit(task_id, args.verbose, args.skip_verify)
        report()
    else:
        if not submit(int(args.task_id), True):
            print("FAIL!!")
            sys.exit(1)


if __name__ == "__main__":
    main()
