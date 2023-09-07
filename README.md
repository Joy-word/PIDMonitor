# PIDMonitor
python 脚本，用于 Linux 上监控进程

## 一些说明
这个项目可用于服务器上监视某个进程，如果进程结束，就主动进行通知。

### 使用说明
一般来说，服务器上挂起进程会使用 `nohup xxxx &` 指令，这个指令会让程序在后台挂起运行，输出会记录在 `nohup.out` 中。

我们使用 `nohup xxxx &` 执行一个进程后，会返回一个进程 id，然后我们执行 `nohup python train_assistant.py [进程id] [进程日志相对位置] > myout.out 2>&1 &` ，即可完成监控工作。监控的日志将输出在 `myout.out`文件中。

机器人我用的是钉钉机器人，如果是其他聊天工具的机器人需要自行查阅相关的文档，然后修改 `print_log` 方法噢。



