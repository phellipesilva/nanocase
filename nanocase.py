#!/usr/bin/env python3
#-*-coding: utf-8-*-
from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.title("NanoCase v1.2 By: Felipe Silva")
tk.geometry("400x100+250+250")
# fun divide
def funD():
  global divd
  global stv
  divd = (float(valt.get()) / int(divc.get()))
  stv = ("%.2f" %divd)
  Label(tk, text=str(divc.get()) + " X de " + str(stv)).place(x=10, y=40)
# fun troco
def tro():
  trc = (float(pg.get()) - float(divd))
  if trc < 0:
    messagebox.showinfo("Troco", "Está faltando!")
  elif trc == 0:
    messagebox.showinfo("Troco", "Está ok!")
  else:
    showv = ("%.2f" %trc)
    messagebox.showinfo("Troco", showv)
# Valor total da compra
Label(tk, text="Valor:").place(x=10, y=10)
valt = Entry(tk, width=5)
valt.place(x=50, y=10)
# Dividir conta
Label(tk, text="Dividir em").place(x=100, y=10)
divc = Entry(tk, width=5)
divc.place(x=170, y=10)
Label(tk, text="vezes").place(x=225, y=10)
# executa a função
Button(tk, text="Calcular", command=funD).place(x=300, y=10)
# calcula troco
Label(tk, text="Valor pago:").place(x=10, y=70)
pg = Entry(tk, width=8)
pg.place(x=100, y=70)
Button(tk, text="Calcular troco", command=tro).place(x=175, y=70)
tk.mainloop()
