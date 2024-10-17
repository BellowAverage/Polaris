import os
import re

def rename_md_files(base_dir):
    # 遍历base_dir下的所有文件和文件夹
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                new_name = extract_title(file_path)
                if new_name:
                    new_file_path = os.path.join(root, f"{sanitize_filename(new_name)}.md")
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file}' to '{new_name}.md'")

def extract_title(file_path):
    # 从文件中提取title
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("title:"):
                # 假设title后面直接跟着标题内容
                return line.strip().replace("title:", "").strip()

def sanitize_filename(filename):
    # 清理文件名中的非法字符
    return re.sub(r'[\\/*?:"<>|]', "", filename)

if __name__ == "__main__":
    base_dir = "data"  # 假设该脚本位于与data文件夹同级的目录中
    rename_md_files(base_dir)
