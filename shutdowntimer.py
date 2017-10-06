#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-04 10:20:43
# @Author  : 酸饺子 (changzheng300@foxmail.com)
# @Link    : http://bbs.fishc.com/space-uid-437297.html
# @Version : $Id$

# 此脚本用于定时开关机

import os
# import sys
import time
import tkinter as tk


class Watch(tk.Frame):
    msec = 1000

    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self._running = False
        self.timestr1 = tk.StringVar()
        self.timestr2 = tk.StringVar()
        self.makeWidgets()
        self.flag = True

    def makeWidgets(self):
        l1 = tk.Label(self, textvariable=self.timestr1)
        l2 = tk.Label(self, textvariable=self.timestr2)
        l1.pack()
        l2.pack()

    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)

    def _settime(self):
        today1 = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.timestr1.set(today1)
        self.timestr2.set(time1)

    def start(self):
        self._update()
        self.pack(side=tk.TOP)


class ShutdownTimer(tk.Frame):

    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        tk.Label(self.master, text='Your computer will shutdown after:').grid(row=0)
        self.hours = tk.Entry(self.master)
        self.minutes = tk.Entry(self.master)
        self.seconds = tk.Entry(self.master)
        self.hours.insert(0, '0')
        self.minutes.insert(0, '0')
        self.seconds.insert(0, '0')
        self.t_sec = -1
        self.hours.grid(row=1, column=0)
        self.minutes.grid(row=2, column=0)
        self.seconds.grid(row=3, column=0)
        tk.Label(self.master, text='hours').grid(row=1, column=1)
        tk.Label(self.master, text='minutes').grid(row=2, column=1)
        tk.Label(self.master, text='seconds').grid(row=3, column=1)
        set_timer_button = tk.Button(
            self.master, text='set shutdown time', command=self._set_timer)
        set_timer_button.grid(row=4)

        self.shutdown_time = tk.StringVar()
        tk.Label(self.master, text='Your computer will shutdown at:').grid(row=5)
        self.shutdown_time_label = tk.Label(
            self.master, textvariable=self.shutdown_time)
        self.shutdown_time_label.grid(row=6)
        self.shutdown_time_input = '--:--:--'
        self.shutdown_time.set(self.shutdown_time_input)

        self.cancel_button = tk.Button(
            self.master, text='cancel', command=self._cancel)
        self.cancel_button.grid(row=7, column=0)

        tk.Button(self.master, text='quit',
                  command=self._quit).grid(row=7, column=1)

    def _set_timer(self):
        self.h = float(self.hours.get())
        self.m = float(self.minutes.get())
        self.s = float(self.seconds.get())
        self.t_sec = self.h * 3600 + self.m * 60 + self.s
        # 关机时刻
        self.shutdown_time_input = time.strftime(
            '%H:%M:%S', time.localtime(time.time() + self.t_sec))
        self.shutdown_time.set(self.shutdown_time_input)
        os.system("shutdown -s -t %d" % self.t_sec)

    def _cancel(self):
        self.shutdown_time_input = '--:--:--'
        self.shutdown_time.set(self.shutdown_time_input)
        self.t_sec = -1
        os.system("shutdown -a")

    def _quit(self):
        os.system("shutdown -a")
        self.quit()


def main():
    master = tk.Tk()
    master.title('shutdowntimer-酸饺子')
    # master.geometry('300x250')

    # 显示当前时间
    now_time_frame = tk.LabelFrame(master, text='now_time')
    now_time = Watch(now_time_frame)
    now_time_frame.pack()
    now_time.start()

    # 设定过多久后关机
    shutdown_timer_frame = tk.LabelFrame(master, text='shutdown_timer')
    shutdown_t = ShutdownTimer(shutdown_timer_frame)
    shutdown_timer_frame.pack()

    master.mainloop()


if __name__ == '__main__':
    main()
