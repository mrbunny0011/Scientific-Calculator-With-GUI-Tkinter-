from tkinter import *

import math


first_num=second_num=operater=None

#   Function of Digit
def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

#  Funtion of Clear Screen
def clear():
    result_label.config(text="")

#  Function of operaters
def get_operater(op):
    global first_num,operater
    first_num=int(result_label['text'])
    operater=op
    result_label.config(text="")

    
#   Function of Trignomatry
def get_func(trig):
    global operater,first_num
    first_num=result_label.config(text=trig)
    operater=trig
    result_label.config(text="")



#  Function of Result
def result():
    global first_num,operater,second_num
    second_num=int(result_label['text'])
    if operater=='+':
        result_label.config(text=(str(first_num+second_num)))
    elif operater=='-':
        result_label.config(text=(str(first_num-second_num)))
    elif operater=='*':
        result_label.config(text=(str(first_num*second_num)))
    elif operater=='/':
        if second_num==0:
            result_label.config(text="Error")
        else:
            result_label.config(text=(str(round(first_num/second_num,2))))
    elif operater=='tan':
        result_label.config(text=(str(round (math.tan(second_num),5))))
    elif operater=='atan':
        result_label.config(text=(str(round (math.atan(second_num),5))))
    elif operater=='sin':
        result_label.config(text=(str(round (math.sin(second_num),5))))
    elif operater=='asin':
        result_label.config(text=(str(round (math.asin(second_num),5))))
    elif operater=='cos':
        result_label.config(text=(str(round (math.cos(second_num),5))))
    elif operater=='acos':
        result_label.config(text=(str(round (math.acos(second_num),5))))
    elif operater=='log':
        result_label.config(text=(str(round (math.log(second_num),5))))
    elif operater=="Square":
        result_label.config(text=(str(second_num*second_num)))
        

    

root = Tk()
root.title("Calculater")
root.geometry("391x360")
root.resizable(0,0)
root.configure(bg="#0C090A")

result_label=Label(root,text="",bg="#0C090A",fg="white")
result_label.grid(row=0,column=0,columnspan=9,pady=(50,15),sticky="w")
result_label.config(font=("verdana",26,'bold'))

# Button of first row
btn7=Button(root,text="7",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("vardana",14))

btn8=Button(root,text="8",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("vardana",14))

btn9=Button(root,text="9",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("vardana",14))

btn_sum=Button(root,text="+",bg="#3B3131",fg="white",width=5,height=2,command=lambda:get_operater('+'))
btn_sum.grid(row=1,column=3)
btn_sum.config(font=("vardana",14))

btn_tan=Button(root,text="Tan",bg="#622F22",fg="white",width=5,height=2,command=lambda:get_func("tan"))
btn_tan.grid(row=1,column=4)
btn_tan.config(font=("vardana",14))

btn_atan=Button(root,text="ArcTan",bg="#622F22",fg="white",width=5,height=2,command=lambda:get_func("atan"))
btn_atan.grid(row=1,column=5)
btn_atan.config(font=("vardana",14))


# Button of Second row
btn4=Button(root,text="4",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("vardana",14))

btn5=Button(root,text="5",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("vardana",14))

btn6=Button(root,text="6",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("vardana",14))

btn_sub=Button(root,text="-",bg="#3B3131",fg="white",width=5,height=2,command=lambda:get_operater('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=("vardana",14))

btn_sin=Button(root,text="Sin",bg="#622F22",fg="white",width=5,height=2,command=lambda:get_func("sin"))
btn_sin.grid(row=2,column=4)
btn_sin.config(font=("vardana",14))

btn_asin=Button(root,text="ArcSin",bg="#622F22",fg="white",width=5,height=2,command=lambda:get_func("asin"))
btn_asin.grid(row=2,column=5)
btn_asin.config(font=("vardana",14))


# Button of Third row
btn1=Button(root,text="1",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("vardana",14))

btn2=Button(root,text="2",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("vardana",14))

btn3=Button(root,text="3",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("vardana",14))

btn_mul=Button(root,text="*",bg="#3B3131",fg="white",width=5,height=2,command=lambda:get_operater('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=("vardana",14))

btn_cos=Button(root,text="Cos",bg="#622F22",fg="white",width=5,height=2,command=lambda:get_func("cos"))
btn_cos.grid(row=3,column=4)
btn_cos.config(font=("vardana",14))

btn_acos=Button(root,text="ArcCos",bg="#622F22",fg="white",width=5,height=2,command=lambda:get_func("acos"))
btn_acos.grid(row=3,column=5)
btn_acos.config(font=("vardana",14))


# Button of Forth row
btn_clr=Button(root,text="C",bg="#C04000",fg="white",width=5,height=2,command=lambda :clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("vardana",14))

btn0=Button(root,text="0",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("vardana",14))

btn_res=Button(root,text="=",bg="#C04000",fg="white",width=5,height=2,command=lambda :result())
btn_res.grid(row=4,column=2)
btn_res.config(font=("vardana",14))

btn_dvi=Button(root,text="/",bg="#3B3131",fg="white",width=5,height=2,command=lambda:get_operater('/'))
btn_dvi.grid(row=4,column=3)
btn_dvi.config(font=("vardana",14))

btn_log=Button(root,text="Log",bg="#5C3317",fg="white",width=5,height=2,command=lambda:get_func("log"))
btn_log.grid(row=4,column=4)
btn_log.config(font=("vardana",14))

btn_Squ=Button(root,text="Square",bg="#5C3317",fg="white",width=5,height=2,command=lambda:get_func("Square"))
btn_Squ.grid(row=4,column=5)
btn_Squ.config(font=("vardana",14))


root.mainloop()