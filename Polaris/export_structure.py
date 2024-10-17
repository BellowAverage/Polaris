import os

def list_files(startpath, depth=-1):
    """
    遍历指定目录，打印目录结构
    :param startpath: 要遍历的目录路径
    :param depth: 遍历的深度，-1表示无限深
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if depth >= 0 and level > depth:
            continue
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def export_project_directory(startpath, output_file, depth=-1):
    """
    导出项目目录到文本文件
    :param startpath: 要遍历的目录路径
    :param output_file: 输出文件路径
    :param depth: 遍历的深度，-1表示无限深
    """
    original_stdout = sys.stdout
    with open(output_file, 'w') as f:
        sys.stdout = f
        list_files(startpath, depth)
    sys.stdout = original_stdout

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        project_path = sys.argv[1]
        output_path = sys.argv[2]
        export_project_directory(project_path, output_path)
    else:
        print("Usage: python export_project_dir.py [PROJECT_PATH] [OUTPUT_FILE]")
