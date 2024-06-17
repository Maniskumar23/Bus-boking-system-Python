from tkinter import*
roo=Tk()
w,h=roo.winfo_screenwidth(),roo.winfo_screenheight()
roo.geometry('%dx%d+0+0'%(w,h))
#root.geometry('600x600')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(roo,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label().grid(row=4,column=0,padx=w//50)
Label(roo,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,columnspan=10,pady=10)
