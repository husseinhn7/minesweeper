from random import randrange
from time import time
from tkinter import *
import datetime
from tkinter import messagebox
w=Tk()

w.config(bg="black")
w.title("MineSweeper")
w.geometry("680x800")
#t=PhotoImage(file=r"C:\Users\Dell\Desktop\tkinter chess\MineSweeper\pngwing.com.png")
w.resizable(0, 0)
#w.iconphoto(False,t)
H=[]
tr=[]
tim=[]
a3=0
F=Frame(w,bg="black",width=700,height=900,borderwidth=20)
F.grid(row=0,column=0)
#2c3e50   border 
a2=0
coordsx=[]
coordsy=[]
def fu():
    global a2
    if a2==0:
        a=0
        while a<=15:
            Q=randrange(0,10)
            W=randrange(0,10)
            if [W,Q] not in H:
                coordsx.append(Q)
                coordsy.append(W)
                H.append([W,Q])
                a+=1
        a2 +=1

    


#004e92



for i in range(0,10):
    for u in range(0,10):
        exec(f'b{i}{u}=Button(F,width=6,height=3,command=fu,font=("arial",10),borderwidth=5)')
        exec(f'b{i}{u}.grid(row=i,column=u)')
        exec(f'b{i}{u}["bg"]="#004e92"')








f=Frame(w)
s=0
m=0
rc=15
count=0
jh=[]
lk=[]
def number(n1,n2):
    lo2=[]
    z=[[n1-1,n2-1],[n1,n2-1],[n1+1,n2-1],[n1-1,n2],[n1+1,n2],[n1-1,n2+1],[n1+1,n2+1],[n1,n2+1]]
    for q in range(0,8):
        if z[q] in H:
            lo2.append(0)
    if len(lo2)==0:
        return   str(" ")
    else:
        return str(len(lo2))
ih=[]


def he(m):
    global a ,a2 ,count,H,rc,lk   , ih
    x1=m.x_root-F.winfo_rootx()
    y1=m.y_root-F.winfo_rooty()
    x=(F.grid_location(x1,y1))[0]
    y=(F.grid_location(x1,y1))[1]
    
    if ([x,y] not in lk) and ([x,y] not in tr) :
        exec(f'b{y}{x}["text"]=str("!")')
        exec(f'b{y}{x}["bg"]="gray"')
        lk.append([x,y])
    elif ([x,y] in lk) and ([x,y] not in tr) :
        exec(f'b{y}{x}["text"]= " "')
        exec(f'b{y}{x}["bg"]="#004e92"')
        #lk=[j for j in lk if j!=[x,y]]
        lk.remove([x,y])
    rc-=1
    ca2["text"]=f"{rc}"
    if [x,y] not in ih :
        ih.append([x,y])
        print(sorted(ih))
        print(sorted(H))
        hg=[xc for xc in H if xc in ih ]
        if  len(hg)-len(H)==0:
            g=messagebox.askquestion(title="congrats",message=f"you have won\n your time is {tim[0]}min\n do you want to play again? ")
            if g=="yes":
                H.clear()
                ih.clear()
                hg.clear()
                coordsx.clear()
                coordsy.clear()
                a=0;a2=0;count=0
                for i in range(0,10):
                    for u in range(0,10):
                        exec(f'b{i}{u}["state"]=ACTIVE')
                        exec(f'b{i}{u}["bg"]="#004e92"')
                        exec(f'b{i}{u}["text"]="  "')

        

     
def h(m):
    global count , tr
    global a ,a2 ,count,H,rc,jh
    lo=[]
    a3==1
    count+=1
    x1=m.x_root-F.winfo_rootx()
    y1=m.y_root-F.winfo_rooty()
    x=(F.grid_location(x1,y1))[0]
    y=(F.grid_location(x1,y1))[1]
    z=[[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x+1,y+1],[x,y+1]]
    #le1["text"]=f"{count}"

    if [x,y] in H:
        for i in range(len(coordsx)):
            exec(f'b{coordsx[i]}{coordsy[i]}["text"]=str("💣")')
            exec(f'b{coordsx[i]}{coordsy[i]}["state"]=DISABLED')
            exec(f'b{coordsx[i]}{coordsy[i]}["bg"]="#8a0721"')
        g=messagebox.askquestion(title="game over",message=f"you have lost\n do you want to play again? ")
        if g=="yes":
            for i in range(0,10):
                for u in range(0,10):
                    exec(f'b{i}{u}["state"]=ACTIVE')
                    exec(f'b{i}{u}.config(background="#004e92")')
                    exec(f'b{i}{u}["text"]="     "')
            H.clear()
            coordsx.clear()
            coordsy.clear()
            a=0;a2=0;count=0
           
        elif g=="no":
            w.destroy()
    else:
        tr.append([x,y])
        for i in range(0,8):
            if z[i] in H:
                lo.append(0)
            k=str(len(lo))
        if a2==0:
            k==" "
            exec(f'b{y}{x}["text"]=" "')
        elif k=="0":
            
            for i in range(-1,2):
                for u in range(-1,2):
                    if 10>(x+u) >=0 and 10>(y+i) >=0 :
                        exec(f'b{y+i}{x+u}["text"]="{number(x+u,y+i)}"')
                        exec(f'b{y+i}{x+u}["bg"]="white"')
                        if number(x+u,y+i)==" ":
                            exec(f'b{y+i}{x+u}["fg"]="white"')
                        elif number(x+u,y+i)=="1":
                            exec(f'b{y+i}{x+u}["fg"]="blue"')
                        elif number(x+u,y+i)=="2":
                            exec(f'b{y+i}{x+u}["fg"]="green"')
                        else :
                            exec(f'b{y+i}{x+u}["fg"]="red"')
                        tr.append([x+u,y+i])
                    
        else:
            print(number(x,y))
            if k=="1":
                exec(f'b{y}{x}["fg"]="blue"')
            elif k=="2":
                exec(f'b{y}{x}["fg"]="green"')
            else:
                exec(f'b{y}{x}["fg"]="red"')
            exec(f'b{y}{x}["text"]={k}')
            exec(f'b{y}{x}["bg"]="white"')
    if count==1:
        def update():
            """ update the label every 1 second """
            global s, m
            s+=1
            if s==60:
                s=0
                m+=1
            f.after(1000, update)
            tim.clear()
            tim.append(f"{m}:{s}")
            ca["text"]=f"{m}:{s}"
        f.after(1000, update)







ca=Label(F,width=21,height=4,font=10,fg="blue",bg="black")
Canvas(ca,width=7,height=6,bg="black")
ca.grid(row=11,column=0,columnspan=4)


ca2=Label(F,width=21,height=4,font=10,fg="blue",bg="black")
ca2.grid(row=11,column=6,columnspan=4)




w.bind("<Button-1>",h)
w.bind("<Button-3>",he)
w.mainloop()