from tkinter import *
from tkinter import messagebox
import mysql.connector as my

db=my.connect(host='localhost',user='root',password='',database='gui')
cur=db.cursor()

def handle():

    global a1,a2,a3
    a1=en1.get()
    a2=int(en2.get())
    a3=int(ty.get())

    print("Member Name:",a1)
    print("Age:",a2)
    print("Membership type:",a3)
    en3.delete(0,END)
    en3.insert(0,a3)

    messagebox.showinfo("Success","Hello"+a1+"\nFee Checked!")


def handle2():
    global a4
    a4=int(d.get())
    print("Discount eligibility:",a4)
    en4.delete(0,END)
    en4.insert(0,a4)

    messagebox.showinfo("Success","\nDiscount Checked!")


def handle3():

    global a5
    a5=a3-a4
    print('Discount:',a5)
    en5.delete(0,END)
    en5.insert(0,a5)

    messagebox.showinfo("success!","\nCalculation Successful!")


def handle4():

    db=my.connect(host='localhost',user='root',password='',database='gui')
    cur=db.cursor()

    insert="insert into data2 (name, age, fee, discount, netfee) values ('%s','%d','%d','%d','%d')"%(a1,a2,a3,a4,a5)
    cur.execute(insert)
    db.commit()
    print("data saved in databases......")

    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en4.delete(0,END)
    en5.delete(0,END)
    ty.set(None)
    d.set(None)

    messagebox.showinfo("success!","Data Cleared!")


win =Tk()

win.title('Read more, Learn more.........')

win.geometry('1000x1000')



win.configure(background='black')

fr=Frame(height=650,width=850,background='white')
fr.place(x=70,y=70)

head=Label(fr,text='Readers Paradise Library',font=('Times New Roman',28),fg='black',bg='white')
head.place(x=20,y=30)

name=Label(fr,text='Member Name:',font=('elephant',20),fg='white')
name.place(x=50,y=100)

en1=Entry(fr,font=('ariel',20),bg='#CFD8DC',fg='black')
en1.place(x=350,y=100)

Age=Label(fr,text='Age:',font=('elephant',20),fg='white')
Age.place(x=50,y=150)

en2=Spinbox(fr,font=('ariel',20),bg='#CFD8DC',from_=10,to_=70,width=7,fg='black')
en2.place(x=350,y=150)

type=Label(fr,text='Membership Type:',font=('elephant',20),fg='white')
type.place(x=50,y=200)

ty=IntVar()

r1=Radiobutton(fr,text='Monthly',font=('elephant',20),fg='black',value=500,var=ty,bg='white')
r1.place(x=350,y=200)

r2=Radiobutton(fr,text='Quaterly',font=('elephant',20),fg='black',value=1000,var=ty,bg='white')
r2.place(x=500,y=200)

r3=Radiobutton(fr,text='Yearly',font=('elephant',20),fg='black',value=1500,var=ty,bg='white')
r3.place(x=650,y=200)

btn1=Button(fr,text='Check Fee',font=('ariel',20),bg='#BBDEFB',fg='black',width=10,command=handle)
btn1.place(x=300,y=250)

fee=Label(fr,text='Fee:',font=('elephant',20),fg='white')
fee.place(x=50,y=300)

en3=Entry(fr,font=('ariel',20),bg='#CFD8DC',fg='black')
en3.place(x=350,y=300)

d=IntVar()

dis=Label(fr,text='Discount Eligibility:',font=('elephant',20),fg='white')
dis.place(x=50,y=350)

r4=Radiobutton(fr,text='Students',font=('elephant',20),fg='black',value=100,var=d,bg='white')
r4.place(x=350,y=350)

r5=Radiobutton(fr,text='Others',font=('elephant',20),fg='black',value=50,var=d,bg='white')
r5.place(x=500,y=350)

btn2=Button(fr,text='Check Discount',font=('ariel',20),bg='#BBDEFB',fg='black',width=10,command=handle2)
btn2.place(x=300,y=400)

disc=Label(fr,text='Discount:',font=('elephant',20),fg='white')
disc.place(x=50,y=450)

en4=Entry(fr,font=('ariel',20),bg='#CFD8DC',fg='black')
en4.place(x=350,y=450)

btn3=Button(fr,text='Calculate',font=('ariel',20),bg='#BBDEFB',fg='black',width=10,command=handle3)
btn3.place(x=300,y=500)

net=Label(fr,text='Net Fee:',font=('elephant',20),fg='white')
net.place(x=50,y=550)

en5=Entry(fr,font=('ariel',20),bg='#CFD8DC',fg='black')
en5.place(x=350,y=550)

btn4=Button(fr,text='Clear all',font=('ariel',20),bg='#BBDEFB',fg='black',width=10,command=handle4)
btn4.place(x=300,y=600)

win.mainloop()