import argparse
import os
import re
import sys

import code_golf_utils


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


def submit(task_id, skip_verify=False):
    if skip_verify:
        return

    print("Submitting task", task_id)

    core = open("logic/core.py").read()

    if not os.path.exists(f"logic/task{task_id:03d}.py"):
        open(f"reports/task{task_id:03d}.txt", "w").write("TODO")
        return

    try:
        logic = open(f"logic/task{task_id:03d}.py").read()

        code = inline_create(logic)
        code = reindent(code)
        code = squeeze(code)
        # code = core + "\n" + logic

        task_path = f"submissions/task{task_id:03d}.py"
        open(task_path, "w").write(code)

        examples = code_golf_utils.load_examples(int(task_id))
        if code_golf_utils.verify_program(task_id, examples, task_path):
            open(f"reports/task{task_id:03d}.txt", "w").write(str(2500 - len(code)))
            return True
        else:
            open(f"reports/task{task_id:03d}.txt", "w").write("FAIL")
    except:
        open(f"reports/task{task_id:03d}.txt", "w").write("ERROR")


def report():
    score = 0
    fail_tests = []
    error_tests = []
    todo_tests = []
    negative_tests = []
    for task_id in range(1, 401):
        result = open(f"reports/task{task_id:03d}.txt").read()
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
    parser.add_argument("--skip_verify", action="store_true")
    args = parser.parse_args()

    if args.task_id == "all":
        for task_id in range(1, 401):
            submit(task_id, args.skip_verify)
        report()
    else:
        if not submit(int(args.task_id)):
            print("FAIL!!")
            sys.exit(1)


if __name__ == "__main__":
    main()
