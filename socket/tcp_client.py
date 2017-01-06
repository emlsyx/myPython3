# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2017-01-05 14:55:20
# @Last Modified by:   emlslxl
# @Last Modified time: 2017-01-05 14:55:23

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9008))  # 主动初始化与服务器端的连接
while True:
    send_data = input("输入发送内容:")
    sk.sendall(bytes(send_data, encoding="utf8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("".join(("接收内容：", accept_data)))
sk.close()