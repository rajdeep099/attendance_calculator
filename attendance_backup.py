from tkinter import *

def show1():
   tl = total_lectures.get()
   ta = total_attended.get()
   tl = int(tl)
   ta = int(ta)
   percent = (ta/tl)*100
      
   la = Label(f, text='%.2f'%percent)
   la.grid(row=2, column=1)
   return percent

def show2():
   percent = 0
   tl = total_lectures.get()
   ta = total_attended.get()
   tl = int(tl)
   ta = int(ta)
   percent =(ta/tl)*100
   rp = req_percent.get()
   rp = int(rp)
   nlw = NoOfLecturesPerWeek.get()
   nlw = int(nlw)
   
   i = 1
   for i in range (i,100):
      if percent < rp:
         percent = ((ta + i)/(tl + i))*100
         
      elif percent >= rp:
         break
   lb = Label(f, text=i-1)
   lb.grid(row=5,column=1)

def show3():
   percent = 0
   tl = total_lectures.get()
   ta = total_attended.get()
   tl = int(tl)
   ta = int(ta)
   percent =(ta/tl)*100
   percent = ('%.2f'%percent)
   percent = float(percent)
   
   rp = req_percent.get()
   rp = int(rp)
   nlw = NoOfLecturesPerWeek.get()
   nlw = int(nlw)
   pd = PresentDays.get()
   pd = int(pd)
   ad = AbsentDays.get()
   ad = int(ad)
   p2 = (pd/nlw)*100
   
   while True:
       lc = Label(f, text="")
       lc.grid(row=8, column=1)
       if (pd + ad) == nlw and p2 > rp and percent < rp:
          
          week = 0
          if percent < rp :
             
             for week in range (1,100):
                ta = ta + pd
                tl = tl + nlw
                percent =(ta/tl)*100
                percent = ('%.2f'%percent)
                percent = float(percent)
                
                if percent < rp:
                   pass
                else:
                   break            
             
          ld = Label(f, text = 'Within {} week '.format(week))
          ld.grid(row = 8, column = 1)
          break
         
       elif (pd + ad) == nlw and p2 <= rp and percent < rp:
          le = Label(f, text="can't be done")
          le.grid(row=8,column=1)
          break
    
       elif (pd + ad) == nlw and percent > rp:
    
          week = 0
          if percent > rp :
             
             for week in range (1,100):
                ta = ta + pd
                tl = tl + nlw
                percent =(ta/tl)*100
                percent = ('%.2f'%percent)
                percent = float(percent)
                
                if percent > rp:
                   pass
                else:
                   break            
             
          lf = Label(f, text = 'Within {} week '.format(week))
          lf.grid(row = 8, column = 1)
          break
         
       elif percent == rp:
          week = 0
          lg = Label(f, text = 'Within {} week '.format(week))
          lg.grid(row = 8, column = 1)
          break
         
       elif (pd + ad) != nlw:
          lh = Label(f, text = 'wrong input given')
          lh.grid(row = 8, column = 1)
          break

# changing of colors
def on_enterB1(e) :
   b1['background'] = 'red'
def on_enterB2(e) :
   b2['background'] = 'green'
def on_enterB3(e) :
   b3['background'] = 'green'
def on_enterB4(e) :
   b4['background'] = 'green'
def on_leave(e):
    b1['background'] = 'SystemButtonFace'
    b2['background'] = 'SystemButtonFace'
    b3['background'] = 'SystemButtonFace'
    b4['background'] = 'SystemButtonFace'

# main
if __name__ == "__main__" :  
    root = Tk()
    
    root.title("Attendance Calculator")
    
    # opening in Command Line Interface
    root.minsize(height = 250, width = 280)

    # declare Frame as f
    f = Frame(root, height = 290, width = 350)
    f.propagate(0)
    f.pack()
    
    # declaring Labels
    l1 = Label(f, text="Total lectures")
    l1.grid(row=0)
    l2 = Label(f, text="Total attended")
    l2.grid(row=1)
    l3 = Label(f, text='Running Percent')
    l3.grid(row=2)
    l4 = Label(f, text='''Percent you
    require''').grid(row=3)
    l5 = Label(f, text='''No. of lectures
    per week''').grid(row = 4) 
    l6 = Label(f, text='''No. of lectures
    required
    (if daily attended)''').grid(row = 5)
    l7 = Label(f, text='''Present days
    per week''').grid(row = 6)
    l8 = Label(f, text='''Absent days
    per week''').grid(row = 7)
    l9 = Label(f, text='''no of weeks
    required''').grid(row = 8)
    
    # taking entries
    total_lectures = Entry(f)
    total_attended = Entry(f)
    req_percent = Entry(f)
    NoOfLecturesPerWeek = Entry(f)
    PresentDays = Entry(f)
    AbsentDays = Entry(f)
    
    t = 0
    total_lectures == total_lectures.get()
    t = total_lectures
    
    total_lectures.grid(row=0, column=1)
    total_attended.grid(row=1, column=1)
    req_percent.grid(row=3, column=1)
    NoOfLecturesPerWeek.grid(row=4, column=1)
    PresentDays.grid(row=6, column=1)
    AbsentDays.grid(row=7, column=1)

    # Buttons
    b1 = Button(f, text='Quit', command=quit, activebackground = '#f00000')
    b1.grid(row=9, column=1)
    b1.bind("<Enter>", on_enterB1)
    b1.bind("<Leave>", on_leave)

    b2 = Button(f, text='Show', command=show1)
    b2.grid(row=2, column=2)
    b2.bind("<Enter>", on_enterB2)
    b2.bind("<Leave>", on_leave)
   
    b3 = Button(f, text='Show', command=show2)
    b3.grid(row=5, column=2)
    b3.bind("<Enter>", on_enterB3)
    b3.bind("<Leave>", on_leave)
    
    b4 = Button(f, text='Show',command = show3)
    b4.grid(row=8, column=2)
    b4.bind("<Enter>", on_enterB4)
    b4.bind("<Leave>", on_leave)
    
    root.mainloop()
