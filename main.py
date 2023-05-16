# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os


def rename(workpath, encode="GBK", decode="Shift_JIS"):  # 输入一个目录，解决该目录下所有文件名的乱码。
    current_path = os.getcwd()
    os.chdir(workpath)
    for path in os.listdir():
        if os.path.isdir(path):
            rename(path, encode, decode)
        os.rename(path, path.encode(encode).decode(encoding=decode, errors="ignore"))
    os.chdir(current_path)


if __name__ == "__main__":
    workpath = "D:\新建文件夹"  # 在这里的引号内输入目录
    rename(workpath)
