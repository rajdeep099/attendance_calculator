from tkinter import *

def abc():
   tl = total_lectures.get()
   ta = total_attended.get()
   tl = int(tl)
   ta = int(ta)
   percent = (ta/tl)*100
      
   Label(root, text='%.2f'%percent).grid(row=2, column=1)
   return percent

def mno():
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
   Label(root, text=i-1).grid(row=5,column=1)

def xyz():
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
         
      Label(root, text = 'Within {} week '.format(week)).grid(row = 8, column = 1)

   elif (pd + ad) == nlw and p2 <= rp and percent < rp:
      Label(root, text='not possible').grid(row=8,column=1)

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
         
      Label(root, text = 'Within {} week '.format(week)).grid(row = 8, column = 1)

   elif percent == rp:
      week = 0
      Label(root, text = 'Within {} week '.format(week)).grid(row = 8, column = 1)

   elif (pd + ad) != nlw:
      Label(root, text = 'check kr bsdk').grid(row = 8, column = 1)

      
root = Tk()
Label(root, text="Total lectures").grid(row=0)
Label(root, text="Total attended").grid(row=1)
Label(root, text='Running Percent').grid(row=2)
Label(root, text='''Percent you
require''').grid(row=3)
Label(root, text='''No. of lectures
per week''').grid(row = 4)
Label(root, text='''No. of lectures
required
(if daily attended)''').grid(row = 5)
Label(root, text='''Present days
per week''').grid(row = 6)
Label(root, text='''Absent days
per week''').grid(row = 7)
Label(root, text='''no of weeks
required''').grid(row = 8)


total_lectures = Entry(root)
total_attended = Entry(root)
req_percent = Entry(root)
NoOfLecturesPerWeek = Entry(root)
PresentDays = Entry(root)
AbsentDays = Entry(root)

t = 0
total_lectures == total_lectures.get()
t = total_lectures

total_lectures.grid(row=0, column=1)
total_attended.grid(row=1, column=1)
req_percent.grid(row=3, column=1)
NoOfLecturesPerWeek.grid(row=4, column=1)
PresentDays.grid(row=6, column=1)
AbsentDays.grid(row=7, column=1)

Button(root, text='Quit', command=quit, activebackground = '#f00000').grid(row=9, column=1, sticky=W, pady=4)

Button(root, text='Show', command=abc).grid(row=2, column=2, sticky=W, pady=4)

Button(root, text='Show', command=mno).grid(row=5, column=2, sticky=W, pady=4)

Button(root, text='Show',command = xyz).grid(row=8, column=2,sticky=W, pady=4)
