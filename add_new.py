import os
import pathlib

def main():
    project_path = pathlib.Path(__file__).parent.resolve()
    name = input("请输入题号: ").strip()
    dir_path = os.path.join(project_path, name)
    os.makedirs(dir_path, exist_ok=True)
    cases = [
        "solution.go",
        "solution.py",
        "Solution.java"
    ]
    for case in cases:
        f = open(os.path.join(dir_path, case), "w")
        f.close()


if __name__ == "__main__":
    main()
