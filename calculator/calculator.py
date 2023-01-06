#!/usr/bin/python3
#-*- coding:utf-8 -*-

import tkinter
from tkinter import font

class Calculator:
  def __init__(self, tk):
    self.__tk = tk
    self.__operator = ''
    self.__operahend = ''
    self.__screen = tkinter.StringVar()

    frame = tkinter.Frame(self.__tk, borderwidth=5)
    self.__calculator_screen(frame).grid(row=0, columnspan=5)
  
    self.__button(frame, 7, self.__handle_number(7)).grid(row=1, column=0)
    self.__button(frame, 8, self.__handle_number(8)).grid(row=1, column=1)
    self.__button(frame, 9, self.__handle_number(9)).grid(row=1, column=2)
    self.__button(frame, '÷', self.__handle_operator('÷')).grid(row=1, column=3)
    self.__button(frame, 'AC', self.__handle_clear).grid(row=1, column=4)
    
    self.__button(frame, 4, self.__handle_number(4)).grid(row=2, column=0)
    self.__button(frame, 5, self.__handle_number(5)).grid(row=2, column=1)
    self.__button(frame, 6, self.__handle_number(6)).grid(row=2, column=2)
    self.__button(frame, '⨉ ', self.__handle_operator('⨉')).grid(row=2, column=3)
    self.__button(frame, 'BS', self.__handle_backspace).grid(row=2, column=4)

    self.__button(frame, 1, self.__handle_number(1)).grid(row=3, column=0)
    self.__button(frame, 2, self.__handle_number(2)).grid(row=3, column=1)
    self.__button(frame, 3, self.__handle_number(3)).grid(row=3, column=2)
    self.__button(frame, '−', self.__handle_operator('−')).grid(row=3, column=3)
    self.__button(frame, '% ', self.__handle_operator('%')).grid(row=3, column=4)

    self.__button(frame, 0, self.__handle_number(0)).grid(row=4, column=0)
    self.__button(frame, '᛫', self.__handle_point).grid(row=4, column=1)
    self.__button(frame, '±', self.__handle_plus_minus).grid(row=4, column=2)
    self.__button(frame, '+', self.__handle_operator('+')).grid(row=4, column=3)
    self.__button(frame, '= ', self.__handle_equal).grid(row=4, column=4)

    frame.grid()

  def __calculator_screen(self, tk_obj):
    calc_inp = tkinter.Frame(tk_obj, borderwidth=5)
    tkinter.Label(
      calc_inp, textvariable=self.__screen,
      background='white', width=18, anchor='e',
      font=font.Font(weight='bold')
    ).pack()
    return calc_inp
  
  def __button(self, tk_obj, num, cmd):
    calc_btn = tkinter.Frame(tk_obj)
    tkinter.Button(
      calc_btn, text=num, command=cmd,
      font=font.Font(weight='bold')
    ).pack()
    return calc_btn
  
  def __handle_number(self, num):
    return lambda: self.__do_handle_number(num)
  
  def __do_handle_number(self, num):
    txt = self.__screen.get()
    if len(txt) < 12:
      self.__screen.set(txt+str(num))
  
  def __handle_operator(self, opr):
    return lambda: self.__do_handle_operator(opr)
  
  def __do_handle_operator(self, opr):
    if not self.__operahend:
      self.__operahend = float(self.__screen.get())
      self.__operator = opr
      self.__screen.set('')
    else:
      self.__handle_equal()

  def __handle_point(self):
    txt = str(self.__screen.get())
    if txt.find('.') == -1:
      self.__screen.set(txt + '.')

  def __handle_plus_minus(self):
    txt = self.__screen.get()
    if txt:
      self.__screen.set(['-'+txt, txt[1:]][txt[0] == '-'])

  def __handle_clear(self, screen = True):
    if screen: self.__screen.set('')
    self.__operahend = None
    self.__operator = None
  
  def __handle_equal(self):
    opr = self.__operator
    frst = float(self.__operahend)
    scnd = float(self.__screen.get())
    if opr == '+':
      res = round(frst + scnd, 12)
      self.__screen.set(res)
      self.__handle_clear(False)
    elif opr == '−':
      res = round(frst - scnd, 12)
      self.__screen.set(res)
      self.__handle_clear(False)
    elif opr == '⨉':
      res = round(frst * scnd, 12)
      self.__screen.set(res)
      self.__handle_clear(False)
    elif opr == '÷':
      res = round(frst / scnd, 12)
      self.__screen.set(res)
      self.__handle_clear(False)
    elif opr == '%':
      pass
  
  def __handle_backspace(self):
    txt = self.__screen.get()
    if txt: self.__screen.set(txt[0:-1])

  def mainloop(self):
    self.__tk.mainloop()