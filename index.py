from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
root = Tk()
root.title("سیستم بارگزاری و کار با اطلاعات پارس آرین")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")

#============================VARIABLES===================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
email = StringVar()
CONTACT = StringVar()
passportnum = StringVar()
birth = StringVar()
passportcode = StringVar()
passportexp = StringVar()
melicode = StringVar()


#============================METHODS=====================================

def Database():
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Mosaferha` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, email TEXT, contact TEXT, passportnum TEXT, birth TEXT, passportcode TEXT, passportexp TEXT, melicode TEXT)")
    cursor.execute("SELECT * FROM `Mosaferha` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or CONTACT.get() == "" or passportnum.get() == "" or birth.get() == "" or passportexp.get() == "" or melicode.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Mosaferha` (firstname, lastname, gender, age, email, contact, passportnum, birth, passportcode, passportexp, melicode) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(email.get()), str(CONTACT.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `Mosaferha` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        email.set("")
        CONTACT.set("")
        passportnum.set("")
        birth.set("")
        passportcode.set("")
        passportexp.set("")
        melicode.set("")

def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `Mosaferha` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `email` = ?, `contact` = ?, `passportnum` = ?, `birth` = ?, `passportcode` = ?, `passportexp` = ?, `melicode` = ? WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(email.get()), str(CONTACT.get()), str(passportnum.get()), str(birth), str(passportcode.get()), str(passportexp.get()), str(melicode.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `Mosaferha` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        email.set("")
        CONTACT.set("")
        passportnum.set("")
        birth.set("")
        passportcode.set("")
        passportexp.set("")
        melicode.set("")
        
    
def OnSelected(event, email=email, passportnum=email, birth=birth, passportcode=birth, passportexp=passportexp,
               melicode=melicode):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    email.set("")
    CONTACT.set("")
    passportnum.set("")
    birth.set("")
    passportcode.set("")
    passportexp.set("")
    melicode.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[3])
    email.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    passportnum.set(selecteditem[7])
    birth.set(selecteditem[8])
    passportcode.set(selecteditem[9])
    passportexp.set(selecteditem[10])
    melicode.set(selecteditem[11])
    UpdateWindow = Toplevel()
    UpdateWindow.title("لیست مسافران")
    width = 750
    height = 750
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 750) - (width/2)
    y = ((screen_height/2) + 750) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    #===================LABELS==============================

    lbl_title = Label(FormTitle, text= "New", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="نام", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="نام خانوادگی", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="جنسیت", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="سن", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="ایمیل(اگر وجود دارد)", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="شماره موبایل", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)
    lbl_passportnum = Label(ContactForm, text="شماره پاسپورت", font=('arial', 14), bd=5)
    lbl_passportnum.grid(row=6, sticky=W)
    lbl_birth = Label(ContactForm, text="تاریخ تولد", font=('arial', 14), bd=5)
    lbl_birth.grid(row=7, sticky=W)
    lbl_passportcode = Label(ContactForm, text="کد پاسپورت", font=('arial', 14), bd=5)
    lbl_passportcode.grid(row=8, sticky=W)
    lbl_passportexp = Label(ContactForm, text="تاریخ انقضای پاسپورت", font=('arial', 14), bd=5)
    lbl_passportexp.grid(row=9, sticky=W)
    lbl_melicode = Label(ContactForm, text="کد ملی", font=('arial', 14), bd=5)
    lbl_melicode.grid(row=10, sticky=W)
    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    email = Entry(ContactForm, textvariable=email,  font=('arial', 14))
    email.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=5, column=1)
    passportnum = Entry(ContactForm, textvariable=passportnum, font=('arial', 14))
    passportnum.grid(row=6, column=1)
    birth = Entry(ContactForm, textvariable=birth, font=('arial', 14))
    birth.grid(row=7, column=1)
    passportcode = Entry(ContactForm, textvariable=passportcode, font=('arial', 14))
    passportcode.grid(row=8, column=1)
    passportexp = Entry(ContactForm, textvariable=passportexp, font=('arial', 14))
    passportexp.grid(row=9, column=1)
    melicode = Entry(ContactForm, textvariable=melicode, font=('arial', 14))
    melicode.grid(row=10, column=1)

    #==================BUTTONS==============================
    btn_updatecon = Button(ContactForm, text="به روز رسانی", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


#fn1353p    
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'لطفا ابتدا حداقل یکی را انتخاب کنید', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'واقعا میخوای اینی که انتخاب کردی رو پاکنی؟', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `Mosaferha` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    
def AddNewWindow(email=email, passportnum=passportnum, birth=birth, passportcode=passportcode, passportexp=passportexp,
                 melicode=melicode):
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    email.set("")
    CONTACT.set("")
    passportnum.set("")
    birth.set("")
    passportcode.set("")
    passportexp.set("")
    melicode.set("")
    NewWindow = Toplevel()
    NewWindow.title("لیست مسافران")
    width = 810
    height = 640
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="آقا", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="خانم", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)

    # ===================LABELS==============================

    lbl_title = Label(FormTitle, text="New", font=('arial', 16), bg="orange", width=300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="نام", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="نام خانوادگی", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="جنسیت", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="سن", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="ایمیل(اگر وجود دارد)", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="شماره موبایل", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)
    lbl_passportnum = Label(ContactForm, text="شماره پاسپورت", font=('arial', 14), bd=5)
    lbl_passportnum.grid(row=6, sticky=W)
    lbl_birth = Label(ContactForm, text="تاریخ تولد", font=('arial', 14), bd=5)
    lbl_birth.grid(row=7, sticky=W)
    lbl_passportcode = Label(ContactForm, text="کد پاسپورت", font=('arial', 14), bd=5)
    lbl_passportcode.grid(row=8, sticky=W)
    lbl_passportexp = Label(ContactForm, text="تاریخ انقضای پاسپورت", font=('arial', 14), bd=5)
    lbl_passportexp.grid(row=9, sticky=W)
    lbl_melicode = Label(ContactForm, text="کد ملی", font=('arial', 14), bd=5)
    lbl_melicode.grid(row=10, sticky=W)
    # ===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE, font=('arial', 14))
    age.grid(row=3, column=1)
    email = Entry(ContactForm, textvariable=email, font=('arial', 14))
    email.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT, font=('arial', 14))
    contact.grid(row=5, column=1)
    passportnum = Entry(ContactForm, textvariable=passportnum, font=('arial', 14))
    passportnum.grid(row=6, column=1)
    birth = Entry(ContactForm, textvariable=birth, font=('arial', 14))
    birth.grid(row=7, column=1)
    passportcode = Entry(ContactForm, textvariable=passportcode, font=('arial', 14))
    passportcode.grid(row=8, column=1)
    passportexp = Entry(ContactForm, textvariable=passportexp, font=('arial', 14))
    passportexp.grid(row=9, column=1)
    melicode = Entry(ContactForm, textvariable=melicode, font=('arial', 14))
    melicode.grid(row=10, column=1)

    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Save", width=70, command=SubmitData)
    btn_addcon.grid(row=15, columnspan=2, pady=10)




    
#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="#6666ff")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#6666ff")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(Top, text="سیستم مدیریت مسافران پارس آرین", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+جدید", bg="#66ff66", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="حذف", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "Firstname", "Lastname", "Gender", "Age", "email", "Contact", "passportnum", "birth", "passportcode", "passportexp", "melicode"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="آی دی", anchor=W)
tree.heading('Firstname', text="نام", anchor=W)
tree.heading('Lastname', text="نام خانوادگی", anchor=W)
tree.heading('Gender', text="جنسیت", anchor=W)
tree.heading('Age', text="سن", anchor=W)
tree.heading('email', text="ایمیل", anchor=W)
tree.heading('Contact', text="تلفن", anchor=W)
tree.heading('passportnum', text='شماره پاسپورت', anchor=W)
tree.heading('birth', text="تاریخ تولد", anchor=W)
tree.heading('passportcode', text='کد پاسپورت')
tree.heading('passportexp', text='تاریخ انقضای پاسپورت')
tree.heading('melicode', text="کدملی")
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()
    
