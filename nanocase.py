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
  divd = (float(valt.get()) / int(divc.get())) 
  Label(tk, text=str(divc.get()) + " parcelas de " + str(divd)).place(x=10, y=40)
# fun troco
def tro():
  trc = (float(pg.get()) - float(divd))
  if trc < 0:
    messagebox.showinfo("Troco", "Está faltando!")
  elif trc == 0:
    messagebox.showinfo("Troco", "Está ok!")
  else:
    messagebox.showinfo("Troco", trc)
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
