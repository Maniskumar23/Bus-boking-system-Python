from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
#root.geometry('600x600')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label().grid(row=4,column=0,padx=w//50)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,columnspan=10,pady=10)
def fun(e=0):
    root.destroy()
    import page3_seat_booking
Button(root,text='Seat Booking',bg='violet red',font='Arial 12',command=fun).grid(row=4,column=3,columnspan=1,padx=w//100)
def fun2(i=0):
    root.destroy()
    import page4_check_your_booking
Button(root,text='Check Booking Seat',bg='violet red',font='Arial 12',command=fun2).grid(row=4,column=4,padx=w//100)
def fun3(o=0):
    root.destroy()
    import page5_add_bus_details
Button(root,text='Add Bus Details',bg='violet red',font='Arial 12',command=fun3).grid(row=4,column=5,padx=w//100)
