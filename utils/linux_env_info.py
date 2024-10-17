import platform
import sys
import subprocess
import pkg_resources

def print_python_env_info():
    # 打印Python版本
    print(f"Python Version: {platform.python_version()}")
    print(f"Version tuple: {sys.version_info}")
    print(f"Compiler: {platform.python_compiler()}")
    print(f"Build: {platform.python_build()}\n")
    
    # 打印操作系统信息
    print(f"System: {platform.system()}")
    print(f"Node: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}\n")
    
    # 打印已安装的第三方包和版本
    print("Installed packages and versions:")
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    for m in installed_packages_list:
        print(m)

# 这个函数尝试使用pip命令列出所有已安装的包，作为另一种方式获取包信息
def print_installed_packages_via_pip():
    try:
        pip_output = subprocess.run(['pip', 'list'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        print("\nPip list output:")
        print(pip_output.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running pip list", e)

if __name__ == "__main__":
    print_python_env_info()
    print_installed_packages_via_pip()
