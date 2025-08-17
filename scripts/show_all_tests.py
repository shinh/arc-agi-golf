#!/usr/bin/env python3

import argparse
import gzip
import json

import numpy as np

from PIL import Image


colors = [
    (0, 0, 0),
    (30, 147, 255),
    (250, 61, 49),
    (78, 204, 48),
    (255, 221, 0),
    (153, 153, 153),
    (229, 59, 163),
    (255, 133, 28),
    (136, 216, 241),
    (147, 17, 49),
    (255, 255, 255),
]


def main():
    parser = argparse.ArgumentParser(description="Make an instruction for AI.")
    parser.add_argument("task_id")
    args = parser.parse_args()

    js = json.load(gzip.open("tasks/task%03d.json.gz" % int(args.task_id)))
    data = []
    for kind in ["train", "test", "arc-gen"]:
        data.extend(js[kind])

    lines = []
    for tc in data:
        input = tc["input"]
        output = tc["output"]

        line = []
        for y in range(max(len(input), len(output))):
            cols = []
            if y < len(input):
                cols += input[y]
            else:
                cols += [10] * len(input[0])

            cols += [10]
            if y < len(output):
                cols += output[y]
            else:
                cols += [10] * len(output[0])

            lines.append(cols)

        lines.append([])

    W = max(len(line) for line in lines)
    lines = [cols + [10] * (W - len(cols)) for cols in lines]

    lines = np.array(lines)
    print(lines.shape)

    lines = np.repeat(lines, 10, axis=0)
    lines = np.repeat(lines, 10, axis=1)
    print(lines.shape)

    out = np.array(colors)[lines]

    Image.fromarray(out.astype(np.uint8)).save("task%03d.png" % int(args.task_id))


if __name__ == "__main__":
    main()
