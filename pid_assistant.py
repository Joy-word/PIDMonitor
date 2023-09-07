import os
import sys
import time
import requests

# 参数解析
pid = sys.argv[1]
log_path = sys.argv[2]

# 用于跟踪进程的函数
def track_process(pid):
    try:
        # os.kill() 函数用于发送指定的信号到系统，0 信号表示无操作，只进行错误检测。
        os.kill(int(pid), 0)
        return True  # 如果信号发送成功，表示进程存在，返回 True
    except OSError:
        return False  # 如果出现 OSError 错误，表示进程不存在，返回 False


def write_log(text):
    print(text)

def print_log(path):
    with open(path, "r") as log_file:
        log = log_file.read()
    # print(log)
    if len(log) > 500:
        log = log[-500:]

    data = {
        'msgtype': 'text', 
        "text":{
		    "content":f"滴滴:{pid}进程已结束 \n {log}"
	    },
    }

    print(data)
    # 给机器人发消息
    response = requests.post('[你的机器人通知地址]', json = data)
    print(response.text)


# 主函数
def main():
    if not track_process(pid):  # 如果进程不存在
        write_log(f"{pid} 进程不存在.")
        return  # 退出程序

    while True:  # 否则执行无限循环
        if not track_process(pid):  # 如果进程不存在
            write_log(f"{pid} 进程已结束")
            print_log(log_path)
            break  # 退出循环

        time.sleep(600)

# 运行主函数
if __name__ == "__main__":
    main()