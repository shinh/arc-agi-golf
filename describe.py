import argparse
import gzip
import json
import os

import matplotlib.pyplot as plt
import numpy as np

import code_golf_utils


def collect_info(task_id):
    task_id = "%03d" % int(task_id)
    js = json.load(gzip.open(os.path.join("tasks", "task" + task_id + ".json.gz")))
    data = []
    for kind in ["train", "test", "arc-gen"]:
        data.extend(js[kind])

    input_hs = []
    input_ws = []
    output_hs = []
    output_ws = []
    io_ratio_hs = []
    io_ratio_ws = []
    input_cols = []
    output_cols = []
    for d in data:
        ib = d["input"]
        ob = d["output"]
        input_hs.append(len(ib))
        input_ws.append(len(ib[0]))
        output_hs.append(len(ob))
        output_ws.append(len(ob[0]))
        io_ratio_hs.append(len(ob) / len(ib))
        io_ratio_ws.append(len(ob[0]) / len(ib[0]))

        for r in ib:
            for c in r:
                input_cols.append(c)
        for r in ob:
            for c in r:
                output_cols.append(c)

    info = []
    if len(set(input_hs)) == 1 and len(set(input_ws)) == 1:
        info.append(f"static input size {input_ws[0]}x{input_hs[0]}")
    if len(set(output_hs)) == 1 and len(set(output_ws)) == 1:
        info.append(f"static output size {output_ws[0]}x{output_hs[0]}")

    if not info:
        if len(set(io_ratio_hs)) == 1 and len(set(io_ratio_ws)) == 1:
            info.append(f"static output/input ratio {io_ratio_ws[0]}x{io_ratio_hs[0]}")

    info.append("colors: " + str(list(set(input_cols))) + " => " + str(list(set(output_cols))))

    return info, data


def save(task_id, out_dir, skip_savefig):
    comment = ""
    if os.path.exists(os.path.join(out_dir, f"{task_id}.txt")):
        with open(os.path.join(out_dir, f"{task_id}.txt")) as f:
            comment = f.read().strip()

    info, data = collect_info(task_id)

    print(f"Task {task_id}: {', '.join(info)} {comment}")

    html = "<h3>Task %s</h3>" % task_id
    html += "<div>" + ", ".join(info) + "</div>"
    html += "<div>" + comment + "</div>"
    html += f"<div><img src='{task_id}-train.png'></div>"
    html += f"<div><img src='{task_id}-arc-gen.png'></div>"
    open(os.path.join(out_dir, f"{task_id}.html"), "w").write(html)

    if not skip_savefig:
        examples = code_golf_utils.load_examples(int(task_id))
        code_golf_utils.show_examples(examples['train'][0:5])
        plt.savefig(os.path.join(out_dir, f"{task_id}-train.png"))
        code_golf_utils.show_examples(examples['arc-gen'][0:5])
        plt.savefig(os.path.join(out_dir, f"{task_id}-arc-gen.png"))


def show(task_id):
    info, data = collect_info(task_id)
    print(f"Task {task_id}: {', '.join(info)}")

    for d in data[0:3]:
        ib = d["input"]
        ob = d["output"]
        print("Input:")
        for r in ib:
            a = ""
            for c in r:
                a += str(c)
            print(a)
        print("Output:")
        for r in ob:
            a = ""
            for c in r:
                a += str(c)
            print(a)


def main():
    parser = argparse.ArgumentParser(description="Show code golf examples.")
    parser.add_argument("task_id")
    parser.add_argument("out", nargs="?")
    parser.add_argument("--skip_savefig", action="store_true")
    args = parser.parse_args()

    if args.out is None:
        show(args.task_id)
    elif args.task_id == "all":
        for task_id in range(1, 401):
            save(task_id, f"{args.out}", args.skip_savefig)
    else:
        save(int(args.task_id), args.out, args.skip_savefig)


if __name__ == "__main__":
    main()
