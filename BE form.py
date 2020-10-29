from tkinter import *
from tkinter import messagebox
import sqlite3
import pandas as pd

#creating object for tkinter
root=Tk()
root.title('BE ADMISSION FORM')
root.geometry('1350x650+0+20')

head=Label(root,text='BE ADMISSION 2019-20',fg='black',bg='white',font=('arial',16,'bold underline'))
head.pack()

name=StringVar()
father=StringVar()
mother=StringVar()
dob=StringVar()
gender=IntVar()
mobile=StringVar()
email=StringVar()
address=StringVar()
country=StringVar()
nationality=StringVar()
religion=StringVar()
cat=StringVar()
cetrank=IntVar()
branch=IntVar()


def database():
        if var.get()==1:
                fullname=name.get()
                father_=father.get()
                mother_=mother.get()
                dob_=dob.get()
                gender_=gender.get()
                mobile_=mobile.get()
                email_=email.get()
                address_=address.get()
                country_=country.get()
                nationality_=nationality.get()
                religion_=religion.get()
                cat_=cat.get()
                cetrank_=cetrank.get()
                branch_=branch.get()
                       
                conn=sqlite3.connect('BE_form.db')

                with conn:
                    cursor=conn.cursor()
                cursor.execute(
                    'create table if not exists student_info(name text,father text,mother text,dob int,gender text,mobile text,email text,address text,country text,nationality text,religion text,cat text,cetrank int,branch text)') 
                cursor.execute(
                    'insert into student_info(name,father,mother,dob,gender,mobile,email,address,country,nationality,religion,cat,cetrank,branch) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (fullname,father_,mother_,dob_,gender_,mobile_,email_,address_,country_,nationality_,religion_,cat_,cetrank_,branch_))

                df = pd.read_sql_query("SELECT * from student_info", conn)
                conn.commit()
                print(df)
                from pandas import ExcelWriter
                writer=ExcelWriter("test.xlsx")
                df.to_excel(writer,"sheet1")
                writer.save()
        else:
                messagebox.showinfo(title='Error',message='please click on checkbox before submitting')



c=Canvas(root,height=590,width=1250,bg='SteelBlue')
rect=c.create_rectangle(10,10,1240,580,fill='LightSkyBlue3',outline='black')
c.pack()

label1=Label(root,text='1. Full Name (Block Letters) :',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label1.place(x=80,y=50)
entry1=Entry(root,textvar=name)
entry1.place(x=370,y=55,width=620,height=25)

label2=Label(root,text='2. Father Name:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label2.place(x=80,y=100)
entry2=Entry(root,textvar=father)
entry2.place(x=240,y=105,width=380,height=25)

label3=Label(root,text='3. Mother Name:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label3.place(x=650,y=100)
entry3=Entry(root,textvar=mother)
entry3.place(x=820,y=105,width=380,height=25)

label4=Label(root,text='4. Date of Birth (DD/MM/YYYY):',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label4.place(x=80,y=150)
entry4=Entry(root,textvar=dob)
entry4.place(x=390,y=155,width=220,height=25)

label5=Label(root,text='5. Gender:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label5.place(x=650,y=150)
rad1=Radiobutton(root,text='Male',variable=gender,value=1,font=('arial',14,'bold italic'),bg='SteelBlue2')
rad1.place(x=770,y=148)
rad2=Radiobutton(root,text='Female',variable=gender,value=2,font=('arial',14,'bold italic'),bg='SteelBlue2')
rad2.place(x=865,y=148)

label6=Label(root,text='6. Mobile N0. :',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label6.place(x=80,y=200)
entry6=Entry(root,textvar=mobile)
entry6.place(x=230,y=205,width=390,height=25)

label7=Label(root,text='7. Email Id:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label7.place(x=650,y=200)
entry7=Entry(root,textvar=email)
entry7.place(x=770,y=205,width=430,height=25)

label8=Label(root,text='8. Address:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label8.place(x=80,y=250)
entry8=Entry(root,textvar=address)
entry8.place(x=210,y=250,width=990,height=25)

label9 = Label(root, text='9. Country:', font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label9.place(x=80, y=300)
list1 = ['Australia','Bhutan','Canada','India','Iceland','Nepal','South Africa','West Indies'];
droplist = OptionMenu(root, country, *list1)
droplist.config(width=35,font=('arial',12,'bold italic'))
country.set('select your country')
droplist.place(x=200, y=300)

label10=Label(root,text='10. Nationality:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label10.place(x=650,y=300)
entry10=Entry(root,textvar=nationality)
entry10.place(x=800,y=300,width=400,height=25)

label11=Label(root,text='11. Religion:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label11.place(x=80,y=350)
entry11=Entry(root,textvar=religion)
entry11.place(x=220,y=350,width=400,height=25)

label12= Label(root, text='12. Category:', font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label12.place(x=650, y=350)
list2 = ['SC','ST','2A','2B','3A','3B','GM'];
droplist = OptionMenu(root, cat, *list2)
droplist.config(width=35,font=('arial',12,'bold italic'))
cat.set('select your category')
droplist.place(x=790, y=350)

label13=Label(root,text='13. Cet Rank No.:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label13.place(x=80,y=400)
entry13=Entry(root,textvar=cetrank)
entry13.place(x=260,y=400,width=360,height=25)

label14=Label(root,text='14. Branch:',font=('arial',14,'bold italic'),fg='black',bg='SteelBlue2')
label14.place(x=650,y=400)
rada=Radiobutton(root,text='EEE',variable=branch,value=1,font=('arial',14,'bold italic'),bg='SteelBlue2')
rada.place(x=780,y=398)
radc=Radiobutton(root,text='ECE',variable=branch,value=2,font=('arial',14,'bold italic'),bg='SteelBlue2')
radc.place(x=860,y=398)
radd=Radiobutton(root,text='CSE',variable=branch,value=3,font=('arial',14,'bold italic'),bg='SteelBlue2')
radd.place(x=940,y=398)
rade=Radiobutton(root,text='ISE',variable=branch,value=4,font=('arial',14,'bold italic'),bg='SteelBlue2')
rade.place(x=1030,y=398)
radf=Radiobutton(root,text='MECH',variable=branch,value=5,font=('arial',14,'bold italic'),bg='SteelBlue2')
radf.place(x=1110,y=398)

var=IntVar()
check=Checkbutton(root,text='''I declare that the information given above is true to the best of my knowledge:''',variable=var,font=('arial',12,'italic'),fg='black',bg='SteelBlue2')
check.place(x=390,y=470)

butt=Button(root,text='Submit',fg='black',font=('arial',18,'bold'),command=database)
butt.place(x=600,y=520)
                                                                                     
label15=Label(root,text='Please click on the checkbox before submitting to avoid error message.')
label15.place(x=460,y=580)


root.mainloop()
            






                   
                

