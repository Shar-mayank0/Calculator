from tkinter import *
import unicodedata

root = Tk()
root.title("Calculator")

infld = Entry(root, width=35 , borderwidth=5)
infld.grid(row=0, column=0, columnspan=5, rowspan=2)

num1 = Button(root, text="1", padx=30, pady=20)
num2 = Button(root, text="2", padx=30, pady=20)
num3 = Button(root, text="3", padx=30, pady=20)

num4 = Button(root, text="4", padx=30, pady=20)
num5 = Button(root, text="5", padx=30, pady=20)
num6 = Button(root, text="6", padx=30, pady=20)

num7 = Button(root, text="7", padx=30, pady=20)
num8 = Button(root, text="8", padx=30, pady=20)
num9 = Button(root, text="9", padx=30, pady=20)

num0 = Button(root, text="0", padx=30, pady=20)

butt_add = Button(root, text="+", padx=28, pady=20)

butt_sub = Button(root, text="-", padx=29, pady=20)

butt_mlt = Button(root, text= ("x"), padx=29, pady=20)

butt_dvd = Button(root, text= chr(247), padx=28, pady=20)

butt_equal = Button(root, text= "=",padx=66, pady=20)

butt_dot = Button(root, text=".", padx=31, pady=20)

butt_sqrt = Button(root, text= "√x", padx=27, pady=20)
butt_sqr = Button(root, text="x²", padx=27, pady=20)

butt_clear = Button(root, text="C", padx=29, pady=20)
butt_bksps = Button(root, text="⌫", padx=27, pady=20)

num1.grid(row=6 , column=0 )
num2.grid(row=6 , column=1 )
num3.grid(row=6 , column=2 )

num4.grid(row=5 , column=0 )
num5.grid(row=5 , column=1 )
num6.grid(row=5 , column=2 )

num7.grid(row=4 , column=0 )
num8.grid(row=4 , column=1 )
num9.grid(row=4 , column=2 )

num0.grid(row=7, column=0 )

butt_add.grid(row=6, column=3)
butt_sub.grid(row=5, column=3)
butt_mlt.grid(row=4, column=3)
butt_dvd.grid(row=3, column=3)
butt_equal.grid(row=7, column=2, columnspan=3)
butt_dot.grid(row=7,column=1)

butt_sqrt.grid(row=2,column=0)
butt_sqr.grid(row=2, column=1)
butt_clear.grid(row=2, column=2)
butt_bksps.grid(row=2, column=3)
root.mainloop()