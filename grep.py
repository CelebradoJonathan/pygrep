import re
import os
import argparse


def read(some_file):
    with open(some_file, "r") as f:
        f_contents = f.read()
        return f_contents.splitlines()


def split_lines(reg_exp, filepath):
    lines = read(filepath)
    for num, line in enumerate(lines, 1):
        if re.search(reg_exp, line):
            print(str(num)+" "+line)
        else:
            pass


def count_lines(reg_exp, filepath):
    lines = read(filepath)
    for num, line in enumerate(lines, 1):
        if re.search(reg_exp, line):
            num += num
            print("Count: "+ str(num + 1))
        else:
            pass


def grep(reg_exp, file_pattern, path, recursive):

    if os.path.exists(path):
        for root, directories, files in os.walk(path):
            for file in files:
                if re.search(file_pattern, file):
                    filepath = "{}\{}".format(root, file)
                    if split_lines(reg_exp, filepath) is not None:
                        split_lines(reg_exp, filepath)
            if not recursive:
                break
            else:
                pass
    else:
        print("path not found")

    if args.count:
        count_lines(reg_exp, filepath)
    else:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("regex", nargs='?')
    parser.add_argument("file", nargs='?')
    parser.add_argument("directory", nargs='?')
    parser.add_argument("-r", '--recursive', action="store_true")
    parser.add_argument("-c", '--count', action="store_true")
    args = parser.parse_args()

    regex_pattern = re.compile(args.regex)
    file_pattern = re.compile(args.file)

    if args.recursive:
        grep(regex_pattern, file_pattern, args.directory, True)
    else:
        grep(regex_pattern, file_pattern, args.directory, False)