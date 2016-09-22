#!/usr/bin/env python
# Name: utils.py
# Time:8/5/16 2:17 PM
# Author:luo1fly

import queue


class Chat(object):

    def __init__(self):
        self.__msg_que = queue.Queue()

    def get_msg(self):
        msg_lst = []
        if self.__msg_que.qsize() > 0:
            for i in range(self.__msg_que.qsize()):
                msg_lst.append(self.__msg_que.get_nowait())
        return msg_lst

    def put_msg(self, *args, **kwargs):
        self.__msg_que.put(*args, **kwargs)