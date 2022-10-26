import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

import sqlite3
#_____________third_page___________
#signUp Database
def cont_sign(a,b,nm,em,bu,g):
    #any_var=1
#passorsd=confirm password
    if a.get()==b.get():
        db.execute("CREATE TABLE IF NOT EXISTS user(name CHAR(30) NOT NULL,email CHAR(30) PRIMARY KEY NOT NULL, password CHAR(15) NOT NULL,bloodUnit CHAR(15) NOT NULL,gender CHAR(15) NOT NULL)")
        data = db.execute("SELECT email FROM user").fetchall()
    
        result = [] 
  
        for t in data: 
            result.append(t[0])
        temp_var=em.get()
    
        fal=None
#email already exists
        if temp_var in result:  
            fal=tk.Label(text="The email id matches previous records",fg="gold", 
                         font=("Comic Sans",12),bg="old lace")
            #allow another sign up
            em.delete(0,"end")
            a.delete(0,"end")
            b.delete(0,"end")
            bu.set("choose Blood unit")
            g.set("choose gender")
            fal.place(x=10, y=380)
        else:
            db.execute("INSERT INTO user(name, email, password,bloodUnit,gender) VALUES(?, ?, ?,?,?)", 
                       [ nm.get(), em.get(), a.get(),bu.get(),g.get()])
            db.commit()
            nm.delete(0,"end")
            em.delete(0,"end")
            a.delete(0,"end")
            b.delete(0,"end")
            bu.set("choose Blood unit")
            g.set("choose gender")
            if fal:
                fal.destroy()
            tk.Label(text="Sign Up Successful", font=("Comic Sans",12),fg="gold",
                     bg="old lace").place(x=15, y=380)
#passorsd!=confirm password       
    else:
        lab=tk.Label(text="Please verify the correct password", fg="gold",
                     font=("Comic Sans",12),bg="old lace")
        lab.place(x=15, y=380)

#log in Database
def log_DB(var1,var2):
    data = db.execute("SELECT email FROM user").fetchall()
        
    res=[]

    for t in data: 
        res.append(t[0])
    temp_var1=var1.get()
    
    
#if email is correct
    if temp_var1 in res:
        info = db.execute(f"SELECT password FROM user WHERE email='{temp_var1}'").fetchall()
 #if pass is correct
        if var2.get()==info[0][0]:
            anyo.destroy()
            val=tk.Label(text="You have been successfully logged in", font=("Arial", 12), bg="old lace",
                         fg="gold").pack()
         
            tk.mainloop()
 #if pass is not correct
        else:
            inval=tk.Label(text="Plase enter valid password", bg="old lace", fg="gold").place(x=50,y=180)
          
#if email is  not correct
    else:
        inval1=tk.Label(text="Plase enter valid email", bg="old lace", fg="gold").place(x=50,y=180)
    
def log_in():
    global anyo
    anyo=tk.Tk()
    anyo.geometry("300x500")
    anyo.resizable(False,False)
    anyo.title("Login Page")
    anyo.config(bg="old lace")
    tk.Label(bg="old lace").pack()
    login=tk.Label(anyo, text="Login Page", font=("Comic Sans",24,"bold"), bg="old lace"
                   ,fg="red3")
    login.pack(side="top")

#user name 
    uname=tk.Label(anyo, text="Enter the email id", font=("Comic Sans",16), bg="old lace").place(x=50,y=70)
    utxt=tk.Entry()
    utxt.place(x=50,y=100)
    utxt.bind("<Return>",lambda temp5:passw.focus())

#password
    passw=tk.Label(anyo, text="Enter the password", font=("Comic Sans",16), bg="old lace"
                   ).place(x=50,y=130)
  
    ptxt=tk.Entry(show="*")
    ptxt.place(x=50,y=160)
    ptxt.bind("<Return>",lambda temp6:log_DB(utxt,ptxt))

    logbut=tk.Button(anyo, text="Click here to Login", font=("Comic Sans",12), bg="red3", fg="white"
                     ,command=lambda :log_DB(var1=utxt, var2=ptxt))
    logbut.place(x=50,y=200)
    
    back_but=tk.Button(anyo,text="  back ", fg="white",bg="red3",font=("Comic Sans",12,"bold"),
                       command=lambda:next_back(anyo,Third))
    back_but.place(x=50, y=250)

def sign_up():
    sign=tk.Tk()
    sign.geometry("300x500")
    sign.resizable(False, False)
    sign.config(bg="old lace")

    tk.Label(sign,text="Create a free Account",fg="red3", font=("Comic Sans",20,
             "bold"),bg="old lace").place(x=10, y=20)
#name
    tk.Label(sign,text="Please enter your name", font=("Comic Sans",16),
             bg="old lace").place(x=15, y=70)

    name=tk.Entry(sign,width=20)
    name.place(x=15,y=100)

    name.bind("<Return>",lambda temp1:email.focus())
    
#email
    tk.Label(sign,text="Please enter your email id", font=("Comic Sans",16),
             bg="old lace").place(x=15, y=130)
    email=tk.Entry(sign,width=20)
    email.place(x=15,y=160)
    email.bind("<Return>",lambda temp2:password.focus())
    
#password
    tk.Label(sign,text="Please enter the password", font=("Comic Sans",16),
             bg="old lace").place(x=15, y=190)
    password=tk.Entry(sign,show="*",width=20)
    password.place(x=15,y=220)
    password.bind("<Return>",lambda temp3:re_password.focus())

#re_password
    tk.Label(sign,text="Please re-enter the password", font=("Comic Sans",16)
             ,bg="old lace").place(x=15, y=250)

    re_password=tk.Entry(sign,show="*",width=20)
    re_password.place(x=15,y=280)
    re_password.bind("<Return>",lambda temp4:optionmenu_widget.focus())

#Blood_unit
    tk.Label(sign,text="Blood unit :",font=("Comic Sans",20,"bold"),
              bg="old lace").place(x=10, y=300)
    control_variable = tk.StringVar(sign)
    control_variable.set("choose Blood unit")
    OPTION_TUPLE = ("AB+", "AB-", "O+","O-","A+","A-","B+","B-") 
    optionmenu_widget = tk.OptionMenu(sign,control_variable, *OPTION_TUPLE)
    optionmenu_widget.place(x=170,y=305)
    optionmenu_widget.bind("<Return>",lambda temp5:gender.focus())

#Gender
    tk.Label(sign,text="Gender :",font=("Comic Sans",20,"bold"),
             bg="old lace").place(x=10, y=330)
    gene_variable = tk.StringVar(sign)
    gene_variable.set("choose gender")
    OPTIONTUPLE = ("male", "female") 
    gender = tk.OptionMenu(sign,
                  gene_variable, *OPTIONTUPLE)
    gender.place(x=130,y=335)
    
    
    gender.bind("<Return>",lambda temp6:gender.cont_sign
     (a=password,b=re_password,nm=name,em=email,g=gene_variable,bu=control_variable))


    sign_cont=tk.Button(sign,text="Sign Up",fg="white", bg="red3",font=("Comic Sans",
     12,"bold"),command=lambda :cont_sign(a=password,b=re_password,nm=name,
       em=email,g=gene_variable,bu=control_variable))
    sign_cont.place(x=200, y=380)
    
    back_but=tk.Button(sign,text="  back ", fg="white",bg="red3",font=("Comic Sans",12,"bold"),
                       command=lambda:next_back(sign,Third))
    back_but.place(x=200, y=430)
    
def Third():
        global root
        root=tk.Tk()
        root.geometry("300x500")
        root.resizable(False, False)
        root.title("Login Page")
        root.config(bg="old lace")
        tk.Label(root,text="Sign Up / Login", font=("Comic Sans",20,"bold"), fg="red3",
                 bg="old lace").place(x=40, y=20)

        tk.Label(root,text="To create an account: ", font=("Comic Sans",16),
                 bg="old lace").place(x=15, y=80)

        sign_but=tk.Button(root,text="Sign Up",fg="white", bg="red3",font=("Comic Sans",12,"bold"), command=lambda:next_back(root,sign_up))
        sign_but.place(x=130, y=130)


        tk.Label(root,text="For an existing account:", font=("Comic Sans",16),bg="old lace").place(x=15, y=170)

        log_but=tk.Button(root,text="  Login  ", fg="white",bg="red3",font=("Comic Sans",12,"bold"),command=lambda:next_back(root,log_in))
        log_but.place(x=130, y=220)
        back_but=tk.Button(root,text="  back ", fg="white",bg="red3",font=("Comic Sans",12,"bold"),
                           command=lambda:next_back(root,second))
        back_but.place(x=130, y=260)
        
    


#_____________second_page__________
def second():
    global _top
    _top = Tk()
    _top.title("requirements for blood Donation")
    _top.minsize(300,400)
    title_name=Label(text="Requirements of blood donor",font=("arial",16),fg="red3")
    title_name.grid(column=1,row=0)

    star1=Label(text="*",font=("comic Sans",22),fg="red3")
    star1.grid(column=0,row=12)

    req1=Label(text="The donor must be in good health and not suffer from any contagious diseases.",font=("comic Sans",12))
    req1.grid(column=1,row=12)
    star2=Label(text="*",font=("comic Sans",22),fg="red3")
    star2.grid(column=0,row=13)
    req2=Label(text=" The age of the donor should be between 18-65 years.",font=("comic Sans",12))
    req2.grid(column=1,row=13)
    star3=Label(text="*",font=("comic Sans",22),fg="red3")
    star3.grid(column=0,row=14)
    req3=Label(text="The blood pressure is less than 120/80 mm Hg ",font=("comic Sans",12))
    req3.grid(column=1,row=14)
    star2=Label(text="*",font=("comic Sans",22),fg="red3")
    star2.grid(column=0,row=15)
    req4=Label(text="The pulse should be between 50-100 per minute.",font=("comic Sans",12))
    req4.grid(column=1,row=15)
    star2=Label(text="*",font=("comic Sans",22),fg="red3")
    star2.grid(column=0,row=16)
    req5=Label(text="The hemoglobin level for men should be 14-17 g, and for women it should be 12-14 g. ",font=("comic Sans",12))
    req5.grid(column=1,row=16)
    star2=Label(text="*",font=("comic Sans",22),fg="red3")
    star2.grid(column=0,row=17)
    req6=Label(text=" the temperature does not exceed 37 degrees Celsius. ",font=("comic Sans",12))
    req6.grid(column=1,row=17)

    b_=Button(text="Accept",font=("Comic Sans",10),bg="sky blue",command=lambda:next_back(_top,Third),
          
          fg="dark blue",height=2,width=10,anchor='center').place(relx=0.35,rely=0.70)
    
    Button(text="Back",font=("Comic Sans",10),bg="sky blue",command=lambda:next_back(_top,first),
          
          fg="dark blue",height=2,width=10,anchor='center').place(relx=0.35,rely=0.85)
        
#_____________last_page__________
def last():
    
    global top
    global listbox
    top=tk.Tk()
    top.minsize(800,800)
    top.title('Blood Units')
    listbox=Listbox(top,font=("Bold",12))
    
    #Title
    l=Label(text="Blood Units",font=("Bold",22),fg="dark blue")
    l.grid(row=0,column=4)
    bs=Button(text="Search",font=("comic sans",8),bg="dark red",command=lambda:DisplayForm(),
             
             fg="#fff",height=2,width=8)
    bs.grid(row=2,column=2)
    #_____A+___
    
    b=Button(text="A+",font=("Bold",15),bg="#fff",command=lambda:Buttons("A+"),
             
             fg="dark red",height=10,width=20)
    b.grid(row=6,column=0) 
    #_____B+___
    b2=Button(text="B+",font=("Bold",15),bg="#fff",command=lambda:Buttons("B+"),
             
             fg="dark red",height=10,width=20)
    b2.grid(row=6,column=2) 
    #_____O+___
    b4=Button(text="O+",font=("Bold",15),bg="#fff",command=lambda:Buttons("O+"),
             
             fg="dark red",height=10,width=20)
    b4.grid(row=6,column=4)
    #____AB+___
    b5=Button(text="AB+",font=("Bold",15),bg="#fff",command=lambda:Buttons("AB+"),
             
             fg="dark red",height=10,width=20)
    b5.grid(row=6,column=8)
    #____A-___
    b6=Button(text="A-",font=("Bold",15),bg="#fff",command=lambda:Buttons("A-"),
             
             fg="dark red",height=10,width=20)
    b6.grid(row=8,column=0) 
    #____B-____  
    b7=Button(text="B-",font=("Bold",15),bg="#fff",command=lambda:Buttons("B-"),
             
             fg="dark red",height=10,width=20)
    b7.grid(row=8,column=2) 
    #____O-____
    b9=Button(text="O-",font=("Bold",15),bg="#fff",command=lambda:Buttons("O-"),
             
             fg="dark red",height=10,width=20)
    b9.grid(row=8,column=4)
    #____AB-____
    b10=Button(text="AB-",font=("Bold",15),bg="#fff",command=lambda:Buttons("AB-"),
             
             fg="dark red",height=10,width=20)
    b10.grid(row=8,column=8)
    Label(text="Emails of donors of selected blood unit",fg="dark blue").grid(row=10,column=2)
 
    Button(text="Back",font=("Comic Sans",10),bg="dark red",command=lambda:next_back(top,first),
          
          fg="white",height=2,width=10,anchor='center').place(relx=0.60,rely=0.80)
    
def Buttons(t_bu):
  listbox.delete(0,"end")  
  ho= db.execute(f"SELECT email FROM user WHERE bloodUnit='{t_bu}'").fetchall() 
  for i in range(len(ho)):
       listbox.insert(i, ho[i])
       listbox.grid(row=12,column=2)     
 

#_____________next/back__________
def next_back(recent,fun):
    recent.destroy()
    fun()

#_____________first_page___________
def first():
 global win
 win=Tk()
 win.title("Blood donation")
 win.geometry("300x500")

 Label(text="Welcome To ",font=("bold",16),
            
                fg="black").place(relx=0.30,rely=0.2)
 Label(text="Blood donation app ",font=("Comic Sans",20),                
                fg="red3").place(relx=0.5,rely=0.4,anchor='center')
 Button(text="Donor",font=("Comic Sans",10),bg="sky blue",command=lambda:next_back(win,second),
              
              fg="dark blue",height=2,width=10).place(relx=0.35,rely=0.6)
 Button(text="Reciver",font=("Comic Sans",10),bg="sky blue",command=lambda:next_back(win,last), 
           
               fg="dark blue",height=2,width=10).place(relx=0.35,rely=0.75)
 
 
def DisplayForm():
    
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("800x200")
    #setting title for window
    display_screen.title("Search Page")
    global tree
    global SEARCH
    SEARCH = StringVar()
    #creating frame
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(display_screen, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Blood Unit Records", font=('verdana', 18), width=600,bg="dark red",fg="white")
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('verdana', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    SEARCH = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    SEARCH.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Name", "Email", "Blood Unit","Gender"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
   # tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Blood Unit', text="Blood Unit", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
   # tree.heading('Branch', text="Branch", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
   # tree.column('#3', stretch=NO, minwidth=0, width=80)
   # tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
#function to search data
def SearchRecord():
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        #conn = sqlite3.connect('user.db')
        #select query with where clause
        cursor=db.execute("SELECT name, email, bloodunit, gender FROM user WHERE name LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
       # conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    #conn = sqlite3.connect('user.db')
    #select query
    cursor=db.execute("SELECT name, email, bloodunit, gender FROM user")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
   # conn.close()
 

db=sqlite3.connect("data.db") 
first()
tk.mainloop()