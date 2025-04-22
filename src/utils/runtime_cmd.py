import subprocess
import sys

def run_command_realtime(command):
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode !=0:
        print("指令执行错误！")
        print(command)
        exit(-1)
    print(f"指令执行成功：")
    print(*command, sep=' ')
