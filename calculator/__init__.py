#!/usr/bin/python3
#-*- coding:utf-8 -*-

import tkinter
from os import path
from calculator import Calculator

fp = path.abspath(path.dirname(__file__)+'/../asset/calculator.png')
tk = tkinter.Tk(className='Calculator')
tk.resizable(False, False)
tk.title('Calculator')
tk.iconname('Calculator')
tk.iconphoto(True, tkinter.PhotoImage(file=fp))
Calculator(tk).mainloop()