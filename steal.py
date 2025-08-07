import glob
import os
import shutil
import subprocess
import sys

from concurrent.futures import ProcessPoolExecutor


def check_score(task_id, code_dir):
    result = subprocess.run(
        [sys.executable, "submit.py", str(task_id), "--code_dir", code_dir],
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return int(result.stdout.split()[-1])


def steal(py, new_dir):
    task_id = int(os.path.basename(py)[4:7])
    new_score = check_score(task_id, new_dir)
    if new_score is None:
        print(f"Task {task_id:03d}: {py} is broken", flush=True)
        return

    base_score = check_score(task_id, "logic")
    if base_score is None:
        raise RuntimeError(f"Baseline is broken for task {task_id}")

    print(f"Task {task_id:03d}: {base_score} => {new_score}", flush=True)

    if new_score > base_score:
        shutil.copy(py, os.path.join("logic", os.path.basename(py)))


def main():
    executor = ProcessPoolExecutor()
    futures = []

    new_dir = sys.argv[1]
    for py in sorted(glob.glob(os.path.join(new_dir, "task*.py"))):
        executor.submit(steal, py, new_dir)

    for future in futures:
        future.result()


if __name__ == "__main__":
    main()
