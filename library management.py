from tkinter import *
from tkinter import ttk
import mysql.connector as db
import datetime as heusc

def exitm(w):
    w.destroy()

def reset_password_lib():
    win1=Tk()
    win1.configure(bg="black")
    win1.title("Reset Password")
    
    s1=Label(win1,text="Enter your recent password - ",font=("monotype corsiva",22),bg="black",fg="white")
    s1.grid(padx=20,pady=10,row=0,column=0)
    
    ebox1=Entry(win1,width=20,bg="white",fg="black",show="*")
    ebox1.grid(padx=20,pady=10,row=0,column=1)
    def b1_command():
            win2=Tk()
            win2.configure(bg="black")
            win2.title("Reset Password")
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
            mycursor=mydb.cursor()
            mycursor.execute("select * from authorised_librarians ;")
            user_details=mycursor.fetchall()
            recent_p=ebox1.get()

            user_p=""
            def b2_command():
                win3=Tk()
                win3.title("Reset Password")
                win3.configure(bg="black")
                new_p=ebox2.get()
                confirm_p=ebox3.get()
                
                if len(new_p)==0 or len(confirm_p)==0:
                    no_new=Label(win3,text="Please enter all the details in the previous window!!",font=("Times New Roman",22),bg="black",fg="red")
                    no_new.grid(padx=20,pady=10,row=0,column=0)
                    
                elif new_p!=confirm_p:
                    d_m=Label(win3,text="Error occured!! Please check whether the info. entered are correct..",font=("Times New Roman",22),bg="black",fg="red")
                    d_m.grid(padx=20,pady=10,row=0,column=0)
                    
                elif new_p==confirm_p:
                    mycursor.execute("update authorised_librarians set password='%s' where emp_id='%s'"%(new_p,emp_id,))
                    
                    pc=Label(win3,text="Your password has been successfully changed.",font=("Times New Roman",22),bg="black",fg="green")
                    pc.grid(padx=20,pady=10,row=0,column=0)
                    
                def b3_command():
                    win3.destroy()
                    win2.destroy()
                    win1.destroy()
                    mm_lib.destroy()

                    win100=Tk()
                    win100.configure(bg="black")
                    win100.title("Info")

                    s1=Label(win100,text="You need to login again to use the services... ",font=("monotype corsiva",22),bg="black",fg="white")
                    s1.grid(row=0, column=0, padx=20)

                    n1=Button(win100, text="Login Now !!", font=("Times New Roman",20), anchor="center", command=lambda:[log_lib(),exitm(win100)] , padx=20,pady=10)
                    n1.grid(row=1, column=0,pady=20)
                    win100.mainloop()
                    
                b3=Button(win3,text="Close",command=b3_command)
                b3.grid(padx=20,pady=5,row=1,column=1)
                win3.mainloop()

                
            for i in user_details:
                if i[3]==emp_id:
                    user_p=i[2]
                    
                else :
                    pass
                
            if len(recent_p)==0:
                ad=Label(win2,text="Please enter all the details in the previous window!!",font=("Times New Roman",22),bg="black",fg="red")
                ad.grid(padx=20,pady=10,row=0,column=0)
                
            elif recent_p!=user_p:
                ad=Label(win2,text="Access denied!!! Password didn't match...",font=("Times New Roman",22),bg="black",fg="red")
                ad.grid(padx=20,pady=10,row=0,column=0)
                
            elif recent_p==user_p:
                s2=Label(win2,text="Enter your new password - ",font=("monotype corsiva",22),bg="black",fg="white")
                s2.grid(padx=20,pady=10,row=0,column=0)
                
                ebox2=Entry(win2,width=20,bg="white",fg="black",show="*")
                ebox2.grid(padx=20,pady=10,row=0,column=1)
                
                s3=Label(win2,text="Confirm your password - ",font=("monotype corsiva",22),bg="black",fg="white")
                s3.grid(padx=20,pady=5,row=1,column=0)
                
                ebox3=Entry(win2,width=20,bg="white",fg="black",show="*")
                ebox3.grid(padx=20,pady=5,row=1,column=1)
                
                b2=Button(win2,text="Submit",font=("Times New Roman",20),command=b2_command)
                b2.grid(padx=20,pady=10,row=2,column=1)
                
            elif len(recent_p)==0:
                no_p=Label(win2,text="Please go back and enter your recent password...",font=("Times New Roman",22),bg="black",fg="red")
                no_p.grid(padx=20,pady=10,row=0,column=0)
            win2.mainloop()
    b1=Button(win1,text="Submit",font=("Times New Roman",16) ,command=b1_command, padx=10, pady=5)
    b1.grid(padx=20,pady=10,row=1,column=1)
    win1.mainloop()

def edit_libr():
    win90=Tk()
    win90.title("Library Details")
    win90.configure(bg="black")

    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
    mycursor=mydb.cursor()

    mycursor.execute("select * from lib_details")
    det1=mycursor.fetchall()

    det=[]
    
    for i in det1:
        for ii in range(0,2):
            det.append(i[ii])

    s1=Label(win90,text="Rate of late fee (Rs./day late) - ",font=("monotype corsiva",22),bg="black",fg="blue")
    s1.grid(padx=20,pady=10,row=0,column=0)

    s2=Label(win90,text=det[0],font=("monotype corsiva",22),bg="black",fg="white")
    s2.grid(padx=20,pady=10,row=0,column=1)

    s3=Label(win90,text="Max days of borrowing the book - ",font=("monotype corsiva",22),bg="black",fg="blue")
    s3.grid(padx=20,pady=10,row=1,column=0)

    s4=Label(win90,text=det[1],font=("monotype corsiva",22),bg="black",fg="white")
    s4.grid(padx=20,pady=10,row=1,column=1)

    def ed_libr():
        win91=Tk()
        win91.title("Edit Library Details")
        win91.configure(bg="black")

        s101=Label(win91,text="Enter the new rate (Rs./Day late) : ",font=("monotype corsiva",22),bg="black",fg="white")
        s101.grid(padx=20,pady=10,row=0,column=0)

        ebox2=Entry(win91,width=20,bg="white",fg="black")
        ebox2.grid(padx=20,pady=10,row=0,column=1)

        s102=Label(win91,text="Enter the new max days of borrwing the book : ",font=("monotype corsiva",22),bg="black",fg="white")
        s102.grid(padx=20,pady=10,row=1,column=0)

        ebox3=Entry(win91,width=20,bg="white",fg="black")
        ebox3.grid(padx=20,pady=10,row=1,column=1)

        def b2_command():
            new_rate=ebox2.get()
            new_date=ebox3.get()

            if new_rate=="" or new_date=="":
                err=Tk()
                err.title("ERROR !!")
                err.configure(bg="black")
                errs=Frame(err)
                errs.pack()
                
                ad=Message(errs,text="Please enter all the details in the previous window!!",font=("Times New Roman",22),bg="black",fg="red")
                ad.pack()

                err.mainloop()

            elif new_rate.isdigit()==False:
                errs=Tk()
                errs.config(bg="black")
                errs.title("ERROR !!!")
                err=Frame(errs)
                err.pack()

                err1=Message(err, text="Please enter an integer as new rate...", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err1.pack()

                err.mainloop()

            elif new_date.isdigit()==False:
                errs=Tk()
                errs.config(bg="black")
                errs.title("ERROR !!!")
                err=Frame(errs)
                err.pack()

                err1=Message(err, text="Please enter an integer as new max days of borrowing a book...", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err1.pack()

                err.mainloop()

            else :
                mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
                mycursor=mydb.cursor()

                mycursor.execute("update lib_details set rate=%s"%(new_rate,))

                mycursor.execute("update lib_details set max_days=%s"%(new_date,))

                success=Tk()
                success.title("Success")
                success.configure(bg="black")

                err1=Label(success, text="Details updates successfully !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err1.grid(row=0,column=0, padx=10, pady=10)

                suby=Button(success,text="Close",font=("Times New Roman",14) ,command=lambda:[exitm(success),exitm(win91),exitm(win90)], padx=7, pady=5)
                suby.grid(padx=20,pady=10,row=1, column=0, sticky=E)

                success.mainloop()

        b2=Button(win91,text="Submit",font=("Times New Roman",16) ,command=b2_command, padx=10, pady=5)
        b2.grid(padx=20,pady=10,row=2,column=1)
        win91.mainloop()

    b1=Button(win90,text="Edit",font=("Times New Roman",20) ,command=ed_libr, padx=10, pady=5)
    b1.grid(padx=20,pady=10,row=2,column=0)
    win90.mainloop()

def new_arr_lib():
    w=Tk()
    w.configure(bg="black")
    w.title("New arrivals")
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
    mycursor=mydb.cursor()
    mycursor.execute("select * from new_arrivals")
    rec=mycursor.fetchall()
    if len(rec)==0:
        not_ar=Label(w, text="Sorry, but there are no new arrivals", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        not_ar.pack()
    else :
        nam=Label(w,text="New arrivals...",font=("monotype corsiva",16),bg="black",fg="red")
        nam.grid(row=0, column=0,padx=10, pady=10)

        def del_n_arr():
            win2=Tk()
            win2.config(bg="black")
            win2.title("Books")

            ask=Label(win2,text="Are you sure you want to delete all the details from the issued table ??" ,font=("Monotype corsiva",24),bg="black",fg="red")
            ask.grid(row=0, column=0, padx=10, pady=10)

            def del_n_arr2():
                mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
                mycursor=mydb.cursor()

                mycursor.execute("delete from new_arrivals;")

                success=Tk()
                success.config(bg="black")
                success.title("Info")

                err1=Label(success, text="New Arrivals have been successfully deleted from the database !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err1.grid(row=0, column=0, padx=10, pady=10)

                success.mainloop()

            suby=Button(win2,text="Yes",font=("Times New Roman",14) ,command=lambda:[del_n_arr2(),exitm(win2),exitm(w)], padx=7, pady=5)
            suby.grid(padx=20,pady=10,row=1, column=0, sticky=E)

            subn=Button(win2,text="No",font=("Times New Roman",14) ,command=lambda:[exitm(win2)], padx=7, pady=5)
            subn.grid(padx=20,pady=10,row=1, column=1)

            win2.mainloop()

        b1=Button(w,text="Delete books",font=("Times New Roman",12) ,command=del_n_arr, padx=10, pady=5)
        b1.grid(row=0,column=7)
        
        headings=("Book Name", "Publisher Name", "Year of Publish", "Edition", "Author", "Status", "Book ID", "Book MRP")
        x=0
        for l in headings:
            h=Entry(w,width=22,bg="white",fg="blue")
            h.grid(row=1,column=x)
            h.insert(END,l)
            x+=1
        
        i=2
        for j in rec:
            for k in range(len(j)):
                e=Entry(w,width=22,bg="white",fg="black")
                e.grid(row=i,column=k)
                e.insert(END,j[k])
            i+=1
    w.mainloop()

def add_bk():
    win77=Tk()
    win77.config(bg="black")
    win77.title("Add New Books")

    nam=Label(win77,text="Enter the name of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    nam.grid(row=0, column=0,padx=10, pady=10)

    nam_ent=Entry(win77, width=46)
    nam_ent.grid(row=0, column=1,padx=10, pady=10)

    publ=Label(win77,text="Enter the publisher of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    publ.grid(row=1, column=0,padx=10, pady=10)

    publ_ent=Entry(win77, width=46)
    publ_ent.grid(row=1, column=1,padx=10, pady=10)

    year_publ=Label(win77,text="Enter the year of publish of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    year_publ.grid(row=2, column=0,padx=10, pady=10)

    year_publ_ent=Entry(win77, width=46)
    year_publ_ent.grid(row=2, column=1,padx=10, pady=10)

    ed_num=Label(win77,text="Enter the edition of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    ed_num.grid(row=3, column=0,padx=10, pady=10)

    ed_num_ent=Entry(win77, width=46)
    ed_num_ent.grid(row=3, column=1,padx=10, pady=10)
    
    auth=Label(win77,text="Enter the author of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    auth.grid(row=4, column=0,padx=10, pady=10)

    auth_ent=Entry(win77, width=46)
    auth_ent.grid(row=4, column=1,padx=10, pady=10)

    book_id=Label(win77,text="Enter the ID of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    book_id.grid(row=5, column=0,padx=10, pady=10)

    book_id_ent=Entry(win77, width=46)
    book_id_ent.grid(row=5, column=1,padx=10, pady=10)

    book_mrp=Label(win77,text="Enter the MRP of the book :",font=("monotype corsiva",22),bg="black",fg="white")
    book_mrp.grid(row=6, column=0,padx=10, pady=10)

    book_mrp_ent=Entry(win77, width=46)
    book_mrp_ent.grid(row=6, column=1,padx=10, pady=10)

    def sub_but1_comm():
        nam_b=nam_ent.get()
        publ_b=publ_ent.get()
        year_publ_b=year_publ_ent.get()
        ed_num_b=ed_num_ent.get()
        auth_b=auth_ent.get()
        book_id_b=book_id_ent.get()
        book_mrp_b=book_mrp_ent.get()

        mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
        mycursor=mydb.cursor()

        mycursor.execute("select * from books;")
        books_det=mycursor.fetchall()

        l=[]

        for i in books_det:
            l.append(i[6])

        if nam_b=="" or publ_b=="" or year_publ_b=="" or ed_num_b=="" or auth_b=="" or book_id_b=="" or book_mrp_b=="" :
            errs=Tk()
            errs.config(bg="black")
            errs.title("ERROR !!!")
            err=Frame(errs)
            err.pack()

            err1=Message(err, text="Please fill all the details in the previous window...", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
            err1.pack()

            errs.mainloop()

        elif ed_num_b.isdigit()==False:
            errs=Tk()
            errs.config(bg="black")
            errs.title("ERROR !!!")
            err=Frame(errs)
            err.pack()

            err1=Message(err, text="Please enter an integer in edition number...", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
            err1.pack()

            errs.mainloop()

        elif book_mrp_b.isdigit()==False:
            errs=Tk()
            errs.config(bg="black")
            errs.title("ERROR !!!")
            err=Frame(errs)
            err.pack()

            err1=Message(err, text="Please enter an integer in book MRP...", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
            err1.pack()

            errs.mainloop()

        elif str(book_id_b) in l:
            errs=Tk()
            errs.config(bg="black")
            errs.title("ERROR !!!")
            err=Frame(errs)
            err.pack()

            err1=Message(err, text="Book ID already in the database. Please enter a distinct book ID", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
            err1.pack()

            errs.mainloop()

        else :
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
            mycursor=mydb.cursor()

            mycursor.execute("insert into books values(%s,%s,%s,%s,%s,'Not Issued',%s,%s);", (nam_b, publ_b, year_publ_b,ed_num_b,auth_b,book_id_b, book_mrp_b))

            mycursor.execute("insert into new_arrivals values(%s,%s,%s,%s,%s,'Not Issued',%s,%s);", (nam_b, publ_b, year_publ_b,ed_num_b,auth_b,book_id_b, book_mrp_b))

            success=Tk()
            success.config(bg="black")
            success.title("ERROR !!!")

            err1=Label(success, text="The book has been successfully added in the database !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
            err1.grid(row=0, column=0, padx=10, pady=10)

            success.mainloop()

    sub_but1=Button(win77,text="Submit",font=("Times New Roman",20) ,command=sub_but1_comm, padx=10, pady=5)
    sub_but1.grid(row=7,column=0,padx=10, pady=10)

    win77.mainloop()

def del_books2(s):
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
    mycursor=mydb.cursor()

    mycursor.execute("delete from books where book_id='%s';"%(s,))

    success=Tk()
    success.config(bg="black")
    success.title("Info")

    err1=Label(success, text="The book has been successfully deleted from the database !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
    err1.grid(row=0, column=0, padx=10, pady=10)

    success.mainloop()
    
def del_bk():
    win99=Tk()
    win99.title("Delete Books...")
    win99.configure(bg="black")

    l1=Label(win99,text="Enter the ID of the book :",font=("times new roman",16),bg="black",fg="white")
    l1.grid(padx=10,pady=5,row=0, column=0)

    eb1=Entry(win99, width=40)
    eb1.grid(padx=10,pady=5, row=0, column=1)

    def del_bks():
        book_id_e=eb1.get()

        if book_id_e=="" :
            win3i=Tk()
            win3i.config(bg="black")
            win3i.title("Error")
            win3=Frame(win3i)
            win3.pack()

            err=Message(win3,text="Please fill all the details in the previous window..",font=("Monotype corsiva",20),bg="black",fg="red")
            err.pack()

            win3i.mainloop()

        else :
            win2=Tk()
            win2.config(bg="black")
            win2.title("Books")
        
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
            mycursor=mydb.cursor()
            mycursor.execute("select * from books;")
            all_books=mycursor.fetchall()
            flag=0
        
            for i in all_books:
                if ( str(book_id_e)==i[6]):
                    flag=1
                    mes=Label(win2,text="Book found !!",font=("Monotype corsiva",26),bg="black",fg="green")
                    mes.grid(row=0, column=0,padx=10,pady=20)

                    mes1=Label(win2,text="Book Name :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes1.grid(row=1, column=0, padx=10, pady=10)

                    mes2=Label(win2,text=i[0],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes2.grid(row=2, column=0, padx=10, pady=10)

                    mes3=Label(win2,text="Edition Number :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes3.grid(row=3, column=0, padx=10, pady=10)

                    mes4=Label(win2,text=i[3],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes4.grid(row=4, column=0, padx=10, pady=10)

                    mes5=Label(win2,text="Publisher :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes5.grid(row=5, column=0, padx=10, pady=10)

                    mes6=Label(win2,text=i[1],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes6.grid(row=6, column=0, padx=10, pady=10)

                    mes7=Label(win2,text="Author :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes7.grid(row=7, column=0, padx=10, pady=10)

                    mes8=Label(win2,text=i[4],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes8.grid(row=8, column=0, padx=10, pady=10)

                    ask=Label(win2,text="Are you sure you want to delete this ??" ,font=("Monotype corsiva",24),bg="black",fg="blue")
                    ask.grid(row=9, column=0, padx=10, pady=10)

                    suby=Button(win2,text="Yes",font=("Times New Roman",14) ,command=lambda:[del_books2(book_id_e),exitm(win2),exitm(win99)], padx=7, pady=5)
                    suby.grid(padx=20,pady=10,row=10, column=0, sticky=E)

                    subn=Button(win2,text="No",font=("Times New Roman",14) ,command=lambda:[exitm(win2)], padx=7, pady=5)
                    subn.grid(padx=20,pady=10,row=10, column=1)

                    win2.mainloop()
                
            else:
                if flag==0:
                    n=Label(win2,text="There is no such book in the Library Database.Please search for a valid book.",font=("Monotype corsiva",22),bg="black",fg="red")
                    n.grid(row=0, column=0, padx=10, pady=10)

                    win2.mainloop()
                    
                else :
                    pass

    sub=Button(win99,text="Submit",font=("Times New Roman",14) ,command=del_bks, padx=10, pady=5)
    sub.grid(padx=20,pady=10,row=1, column=0)

    win99.mainloop()

def ret_bk():
    win110=Tk()
    win110.config(bg="black")
    win110.title("Return Books")

    l1=Label(win110,text="Enter the ID of the book :",font=("times new roman",16),bg="black",fg="white")
    l1.grid(padx=10,pady=5, row=0, column=0)

    eb1=Entry(win110, width=40)
    eb1.grid(padx=10,pady=5, row=0, column=1)

    l2=Label(win110,text="Enter the ID of the patron :",font=("times new roman",16),bg="black",fg="white")
    l2.grid(padx=10,pady=5,row=1, column=0)

    eb2=Entry(win110, width=40)
    eb2.grid(padx=10,pady=5, row=1, column=1)

    def ret_bks():
        global id_pat1
        global id_bk1
        
        id_bk1=eb1.get()
        id_pat1=eb2.get()

        if id_bk1=="" or id_pat1=="":
            errs=Tk()
            errs.config(bg="black")
            errs.title("Error")
            err=Frame(errs)
            err.pack()

            err1=Message(err,text="Please fill all the details in the previous window..",font=("Monotype corsiva",20),bg="black",fg="red")
            err1.pack()

            errs.mainloop()

        else :
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management",autocommit=True)
            mycursor=mydb.cursor()

            mycursor.execute("select * from patrons;")
            pat_det=mycursor.fetchall()

            patr_det=[]

            for ii in pat_det:
                patr_det.append(ii[5])

            mycursor.execute("select * from issued_books;")
            iss_book=mycursor.fetchall()

            iss_books=[]

            for jj in iss_book:
                iss_books.append(jj[1])

            if (str(id_bk1) in iss_books) and (str(id_pat1) in patr_det) :
                mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management",autocommit=True)
                mycursor=mydb.cursor()

                mycursor.execute("select * from issued_books;")
                iss_book1=mycursor.fetchall()

                for k in iss_book1:
                    if k[1]==str(id_bk1):
                        ret_dat=k[3]

                    else :
                        pass

                td=heusc.date.today()

                ret_day=td-ret_dat
                ret_days=ret_day.days

                fine1=0

                for kk in range(0,1):
                    if ret_days>0:
                        fine1=ret_days

                    else :
                        pass

                mycursor.execute("update books set state='Not Issued' where book_id='%s';"%(str(id_bk1),))

                mycursor.execute("delete from issued_books where book_id='%s';"%(str(id_bk1),))

                mycursor.execute("select * from lib_details;")
                det=mycursor.fetchall()

                for ll in det:
                    rate1=ll[0]

                success=Tk()
                success.config(bg="black")
                success.title("Info")

                err1=Label(success, text="The book has been successfully returned !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err1.grid(row=0, column=0, padx=10, pady=10)

                err2=Label(success, text="The fine would be -", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err2.grid(row=1, column=0, padx=10, pady=5)

                err3=Label(success, text="Rs."+str(fine1*float(rate1)), font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                err3.grid(row=2, column=0, padx=10, pady=5)

                success.mainloop()

                mycursor.execute("select * from new_arrivals")
                new_a=mycursor.fetchall()

                l313=[]

                for i in new_a:
                    l313.append(i[6])

                if str(id_bk1) in l313:
                    mycursor.execute("update new_arrivals set state='Not Issued' where book_id='%s';"%(str(id_bk1),))

                else :
                    pass

            else :
                errs=Tk()
                errs.config(bg="black")
                errs.title("Error")
                err=Frame(errs)
                err.pack()

                err1=Message(err,text="Error occurred!! Please check if the details entered are correct or not..",font=("Monotype corsiva",20),bg="black",fg="red")
                err1.pack()

                errs.mainloop()

    sub=Button(win110,text="Submit",font=("Times New Roman",14) ,command=ret_bks, padx=10, pady=5)
    sub.grid(padx=20,pady=10,row=2, column=1)

    win110.mainloop()

def issue_new_bk():
    win110=Tk()
    win110.config(bg="black")
    win110.title("Issue New Books")

    l1=Label(win110,text="Enter the ID of the book :",font=("times new roman",16),bg="black",fg="white")
    l1.grid(padx=10,pady=5, row=0, column=0)

    eb1=Entry(win110, width=40)
    eb1.grid(padx=10,pady=5, row=0, column=1)

    l2=Label(win110,text="Enter the ID of the patron :",font=("times new roman",16),bg="black",fg="white")
    l2.grid(padx=10,pady=5,row=1, column=0)

    eb2=Entry(win110, width=40)
    eb2.grid(padx=10,pady=5, row=1, column=1)

    def issue_new_bks():
        global book_nam1
        global id_pat1
        global id_bk1
        
        id_bk1=eb1.get()
        id_pat1=eb2.get()

        if id_bk1=="" or id_pat1=="":
            errs=Tk()
            errs.config(bg="black")
            errs.title("Error")
            err=Frame(errs)
            err.pack()

            err1=Message(err,text="Please fill all the details in the previous window..",font=("Monotype corsiva",20),bg="black",fg="red")
            err1.pack()

            errs.mainloop()

        else :
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management",autocommit=True)
            mycursor=mydb.cursor()

            mycursor.execute("select * from books;")
            book_det=mycursor.fetchall()

            books_det=[]

            for i in book_det:
                books_det.append(i[6])

            mycursor.execute("select * from patrons;")
            pat_det=mycursor.fetchall()

            patr_det=[]

            for ii in pat_det:
                patr_det.append(ii[5])

            mycursor.execute("select * from issued_books;")
            iss_book=mycursor.fetchall()

            iss_books=[]

            for jj in iss_book:
                iss_books.append(jj[1])

            if (str(id_bk1) in books_det) and (str(id_pat1) in patr_det) :

                if (str(id_bk1) not in iss_books) :
                    
                    for ii in book_det :
                        if str(id_bk1)==ii[6]:
                            book_nam1=ii[0]

                        else :
                            pass

                    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management",autocommit=True)
                    mycursor=mydb.cursor()

                    mycursor.execute("select * from lib_details;")

                    lib_det=mycursor.fetchall()

                    for i in lib_det:
                        ret_day=i[1]

                    td=heusc.date.today()

                    ret_dat=td+heusc.timedelta(ret_day)

                    mycursor.execute("insert into issued_books values ('{0}','{1}','{2}','{3}','{4}');".format(book_nam1,str(id_bk1),td,ret_dat,str(id_pat1),))

                    mycursor.execute("update books set state='Issued' where book_id='%s';"%(str(id_bk1),))

                    success=Tk()
                    success.config(bg="black")
                    success.title("Info")

                    err1=Label(success, text="The book has been successfully issued !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                    err1.grid(row=0, column=0, padx=10, pady=10)

                    success.mainloop()

                    mycursor.execute("select * from new_arrivals")
                    new_a=mycursor.fetchall()

                    l313=[]

                    for i in new_a:
                        l313.append(i[6])

                    if str(id_bk1) in l313:
                        mycursor.execute("update new_arrivals set state='Issued' where book_id='%s';"%(str(id_bk1),))

                    else :
                        pass

                else :
                    errs=Tk()
                    errs.config(bg="black")
                    errs.title("Error")
                    err=Frame(errs)
                    err.pack()

                    err1=Message(err,text="The book has been already issued....",font=("Monotype corsiva",20),bg="black",fg="red")
                    err1.pack()

                    errs.mainloop()

            else :
                errs=Tk()
                errs.config(bg="black")
                errs.title("Error")
                err=Frame(errs)
                err.pack()

                err1=Message(err,text="Error occurred!! Please check if the details entered are correct or not..",font=("Monotype corsiva",20),bg="black",fg="red")
                err1.pack()

                errs.mainloop()

    sub=Button(win110,text="Submit",font=("Times New Roman",14) ,command=issue_new_bks, padx=10, pady=5)
    sub.grid(padx=20,pady=10,row=2, column=1)

    win110.mainloop()
    
def issued_bk_list():
    win101=Tk()
    win101.config(bg="black")
    win101.title("Issued Books")
    
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
    mycursor=mydb.cursor()
    
    mycursor.execute("select * from issued_books;")
    rec=mycursor.fetchall()

    r=1
    if len(rec)==0:
        no_issue=Label(win101,text="No books have been issued yet.....",font=("Times New Roman",22),bg="black",fg="red")
        no_issue.grid(row=0, column=0)
        win101.mainloop()

    else :
        headings=("Book Name","Book ID","Issued Date","Return Date","Issued to (ID number)")
        x=0

        for head in headings:
            e1=Entry(win101,width=22,fg="blue")
            e1.grid(row=0,column=x)
            e1.insert(END,head)
            x+=1

        a=0
        for i in rec:
            for val in range(5):
                e2=Entry(win101,width=22)
                e2.grid(row=r,column=a)
                e2.insert(END,i[val])
                a+=1

        win101.mainloop()

def change_subs_tot():
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
    mycursor=mydb.cursor()
    mycursor.execute("update patrons set subscriptions='%s' where id='%s'"%(book_name,id_num,))
    mycursor.execute("update patrons set edition_num='%s' where id='%s'"%(edition_num,id_num,))
    
def change_subs() :
    win99=Tk()
    win99.title("Change your subscriptions...")
    win99.configure(bg="black")

    l2=Label(win99,text="Enter the name of the book :",font=("times new roman",16),bg="black",fg="white")
    l2.grid(padx=10,pady=5, row=0, column=0)

    eb1=Entry(win99, width=40)
    eb1.grid(padx=10,pady=5, row=0, column=1)

    l3=Label(win99,text="Enter the edition of the book :",font=("times new roman",16),bg="black",fg="white")
    l3.grid(padx=10,pady=5,row=1, column=0)

    eb2=Entry(win99, width=40)
    eb2.grid(padx=10,pady=5, row=1, column=1)

    def change_subs_but():
        global book_name
        global edition_num
        
        book_name=eb1.get()
        edition_num=eb2.get()

        if book_name=="" or edition_num=="" :
            win3i=Tk()
            win3i.config(bg="black")
            win3i.title("Error")
            win3=Frame(win3i)
            win3.pack()

            err=Message(win3,text="Please fill all the details in the previous window..",font=("Monotype corsiva",20),bg="black",fg="red")
            err.pack()

            win3i.mainloop()

        else :

            win2=Tk()
            win2.config(bg="black")
            win2.title("Books")
        
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
            mycursor=mydb.cursor()
            mycursor.execute("select * from books;")
            all_books=mycursor.fetchall()
            flag=0
        
            for i in all_books:
                if ( (book_name.lower() in i[0].lower()) and (int(edition_num)==int(i[3])) ):
                    flag=1
                    mes=Label(win2,text="Book found !!",font=("Monotype corsiva",26),bg="black",fg="green")
                    mes.grid(row=0, column=0,padx=10,pady=20)

                    mes1=Label(win2,text="Book Name :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes1.grid(row=1, column=0, padx=10, pady=10)

                    mes2=Label(win2,text=i[0],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes2.grid(row=2, column=0, padx=10, pady=10)

                    mes3=Label(win2,text="Edition Number :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes3.grid(row=3, column=0, padx=10, pady=10)

                    mes4=Label(win2,text=i[3],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes4.grid(row=4, column=0, padx=10, pady=10)

                    mes5=Label(win2,text="Publisher :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes5.grid(row=5, column=0, padx=10, pady=10)

                    mes6=Label(win2,text=i[1],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes6.grid(row=6, column=0, padx=10, pady=10)

                    mes7=Label(win2,text="Author :",font=("Monotype corsiva",20),bg="black",fg="blue")
                    mes7.grid(row=7, column=0, padx=10, pady=10)

                    mes8=Label(win2,text=i[4],font=("Monotype corsiva",20),bg="black",fg="white")
                    mes8.grid(row=8, column=0, padx=10, pady=10)

                    ask=Label(win2,text="Are you sure you want to subscibe this ??" ,font=("Monotype corsiva",24),bg="black",fg="blue")
                    ask.grid(row=9, column=0, padx=10, pady=10)

                    suby=Button(win2,text="Yes",font=("Times New Roman",14) ,command=lambda:[change_subs_tot(),exitm(win2),exitm(win99)], padx=7, pady=5)
                    suby.grid(padx=20,pady=10,row=10, column=0, sticky=E)

                    subn=Button(win2,text="No",font=("Times New Roman",14) ,command=lambda:[exitm(win2)], padx=7, pady=5)
                    subn.grid(padx=20,pady=10,row=10, column=1)

                    win2.mainloop()
                
            else:
                if flag==0:
                    n=Label(win2,text="There is no such book in the Library Database.Please search for a valid book.",font=("Monotype corsiva",22),bg="black",fg="red")
                    n.grid(row=0, column=0, padx=10, pady=10)

                    win2.mainloop()
                    
                else :
                    pass

    sub=Button(win99,text="Submit",font=("Times New Roman",20) ,command=change_subs_but, padx=10, pady=5)
    sub.grid(padx=20,pady=10,row=2, column=0)

    win99.mainloop()
    
def reset_password():
    win1=Tk()
    win1.configure(bg="black")
    win1.title("Reset Password")
    s1=Label(win1,text="Enter your recent password - ",font=("monotype corsiva",22),bg="black",fg="white")
    s1.grid(padx=20,pady=10,row=0,column=0)
    ebox1=Entry(win1,width=20,bg="white",fg="black",show="*")
    ebox1.grid(padx=20,pady=10,row=0,column=1)
    def b1_command():
            win2=Tk()
            win2.configure(bg="black")
            win2.title("Reset Password")
            mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management", autocommit=True)
            mycursor=mydb.cursor()
            mycursor.execute("select * from patrons ;")
            user_details=mycursor.fetchall()
            recent_p=ebox1.get()

            user_p=""
            def b2_command():
                win3=Tk()
                win3.title("Reset Password")
                win3.configure(bg="black")
                new_p=ebox2.get()
                confirm_p=ebox3.get()
                if len(new_p)==0 or len(confirm_p)==0:
                    no_new=Label(win3,text="Please enter all the details in the previous window!!",font=("Times New Roman",22),bg="black",fg="red")
                    no_new.grid(padx=20,pady=10,row=0,column=0)
                elif new_p!=confirm_p:
                    d_m=Label(win3,text="Error occured!! Please check whether the info. entered are correct..",font=("Times New Roman",22),bg="black",fg="red")
                    d_m.grid(padx=20,pady=10,row=0,column=0)
                elif new_p==confirm_p:
                    mycursor.execute("update patrons set password='%s' where id='%s'"%(new_p,id_num,))
                    
                    pc=Label(win3,text="Your password has been successfully changed.",font=("Times New Roman",22),bg="black",fg="green")
                    pc.grid(padx=20,pady=10,row=0,column=0)
                def b3_command():
                    win3.destroy()
                    win2.destroy()
                    win1.destroy()

                    mm_pat.destroy()

                    win100=Tk()
                    win100.configure(bg="black")
                    win100.title("Info")

                    s1=Label(win100,text="You need to login again to use the services... ",font=("monotype corsiva",22),bg="black",fg="white")
                    s1.grid(row=0, column=0, padx=20)

                    n1=Button(win100, text="Login Now !!", font=("Times New Roman",20), anchor="center", command=lambda:[log_pat(),exitm(win100)] , padx=20,pady=10)
                    n1.grid(row=1, column=0,pady=20)

                    win100.mainloop()
                    
                b3=Button(win3,text="Close",command=b3_command)
                b3.grid(padx=20,pady=5,row=1,column=1)
                win3.mainloop()
            for i in user_details:
                if i[5]==id_num:
                    username=i[0]
                    designation=i[1]
                    subs=i[2]
                    gender=i[3]
                    user_p=i[4]
                else :
                    pass
            if len(recent_p)==0:
                ad=Label(win2,text="Please enter all the details in the previous window!!",font=("Times New Roman",22),bg="black",fg="red")
                ad.grid(padx=20,pady=10,row=0,column=0)
            elif recent_p!=user_p:
                ad=Label(win2,text="Access denied!!! Password didn't match...",font=("Times New Roman",22),bg="black",fg="red")
                ad.grid(padx=20,pady=10,row=0,column=0)
            elif recent_p==user_p:
                s2=Label(win2,text="Enter your new Password - ",font=("monotype corsiva",22),bg="black",fg="white")
                s2.grid(padx=20,pady=10,row=0,column=0)
                
                ebox2=Entry(win2,width=20,bg="white",fg="black",show="*")
                ebox2.grid(padx=20,pady=10,row=0,column=1)
                
                s3=Label(win2,text="Confirm your Password - ",font=("monotype corsiva",22),bg="black",fg="white")
                s3.grid(padx=20,pady=5,row=1,column=0)
                
                ebox3=Entry(win2,width=20,bg="white",fg="black",show="*")
                ebox3.grid(padx=20,pady=5,row=1,column=1)
                
                b2=Button(win2,text="Submit",font=("Times New Roman",20),command=b2_command)
                b2.grid(padx=20,pady=10,row=2,column=1)
            elif len(recent_p)==0:
                no_p=Label(win2,text="Please go back and enter your recent password...",font=("Times New Roman",22),bg="black",fg="red")
                no_p.grid(padx=20,pady=10,row=0,column=0)
            win2.mainloop()
    b1=Button(win1,text="Submit",font=("Times New Roman",20) ,command=b1_command, padx=10, pady=5)
    b1.grid(padx=20,pady=10,row=2,column=0)
    win1.mainloop()

def issued_bk():
    win1=Tk()
    win1.config(bg="black")
    win1.title("Issued Books")
    
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
    mycursor=mydb.cursor()
    
    mycursor.execute("select * from issued_books;")
    rec=mycursor.fetchall()
    flag=0
    r=1
    for i in rec:
        if i[4]==id_num:
            flag=1
            headings=("Book Name","Book ID","Issued Date","Return Date")
            x=0
            
            for head in headings:
                e1=Entry(win1,width=22,fg="blue")
                e1.grid(row=0,column=x)
                e1.insert(END,head)
                x+=1

            a=0

            for val in range(4):
                e2=Entry(win1,width=22)
                e2.grid(row=r,column=a)
                e2.insert(END,i[val])
                
                a+=1
            r+=1
    
    if flag==0:
        no_issue=Message(win1,text="You haven't issued any book this week. Please ask your librarian if you want to issue one.",font=("Times New Roman",22),bg="black",fg="red")
        no_issue.grid(row=0, column=0)
        win1.mainloop()
                
    else:
        win1.mainloop()
        pass

def search_bk():
    win1=Tk()
    win1.config(bg="black")
    win1.title("Search")
    es=Label(win1,text="Search your book...", font=("Times New Roman",20),bg="black",fg="yellow")
    es.grid(row=0, column=0)
    
    e=Entry(win1,width=52)
    e.grid(padx=10,pady=10,row=1,column=0)

    def ain():
        win2=Tk()
        win2.config(bg="black")
        win2.title("Books")
        us_book=e.get()
        mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
        mycursor=mydb.cursor()
        mycursor.execute("select * from books;")
        all_books=mycursor.fetchall()
        flag=0
        a=2 

        for i in all_books:
            if (us_book.lower() in i[0].lower()):
                flag=1
                mes=Label(win2,text="Search",font=("Monotype corsiva",26),bg="black",fg="red")
                mes.grid(row=0, column=0)

                mes1=Label(win2,text="Results...",font=("Monotype corsiva",26),bg="black",fg="red")
                mes1.grid(row=0, column=1)
                
                headings=("Book Name","Publisher Name","Year Of Publish","Edition Number","Author","Status","Book ID","Book MRP")
                x=0
                for j in headings:
                    c=Entry(win2,width=22,bg="white",fg="blue")
                    c.grid(row=1,column=x)
                    c.insert(END,j)
                    x+=1
    
                for b in range(len(i)):
                    eb=Entry(win2,width=22,bg="white",fg="black")
                    eb.grid(row=a,column=b)
                    eb.insert(END,i[b])

                a+=1
                ro=0
                col=8
            else :
                pass
                    
        else:
            if flag==0:
                n=Label(win2,text="There is no such in the Library Database.Please search for a valid book.",font=("Monotype corsiva",22),bg="black",fg="red")
                n.grid(row=0, column=0)
                ro=1
                col=1
            else :
                pass
        
        close_but=Button(win2,text ="Done", command=win2.destroy,padx=10, pady=5)
        close_but.grid(row=ro, column=col)
        win2.mainloop()
    s_b=Button(win1,text="Search",command=ain)
    s_b.grid(padx=10,pady=10,row=1,column=1)
    gs=Label(win1,text="""**This is not a Google search.It won't be able to display "You mean this:...."**""", font=("Times New Roman",10),bg="black",fg="green")

    gs1=Label(win1,text="""**Please enter the exact name of the book you want to search**""", font=("Times New Roman",10),bg="black",fg="green")
    gs.grid(row=3, column=0)
    gs1.grid(row=4, column=0)
    win1.mainloop()

def book_l():
    w2=Tk()
    w2.configure(bg="black")
    w2.title("Book List")
    mydb=db.connect(host="localhost",user="root",password="12589",database="lib_management")
    mycursor=mydb.cursor()
    mycursor.execute("select * from books")
    r=mycursor.fetchall()
    if len(r)==0:
        n=Label(w2,text="Sorry,but there is no book in the library at the moment...",font=("Monotype corsiva",22),bg="black",fg="white",padx=20,pady=10)
        n.pack()
    else:
        headings=("Book Name","Publisher Name","Year of Publish","Edition","Author","Status","Book ID","Book MRP")
        x=0
        for t in headings:
            l=Entry(w2,width=22,bg="white",fg="blue")
            l.grid(row=0,column=x)
            l.insert(END,t)
            x+=1
        i=1
        for j in r:
            for k in range(len(j)):
                    e=Entry(w2,width=22,bg="white",fg="black")
                    e.grid(row=i,column=k)
                    e.insert(END,j[k])
            i+=1
    w2.mainloop()

def subscr():
    win1=Tk()
    win1.title("Subscriptions")
    win1.config(bg="black")
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
    mycursor=mydb.cursor()
    mycursor.execute("select * from patrons ;")
    subs=mycursor.fetchall()

    for i in subs:
        if i[5]==id_num:
            book_name=i[2]
            edition_num=i[6]
            break
        else :
            pass
    
    if len(book_name)==0:
        no_sub=Label(win1,text="Nothing subscribed yet.",font=("Monotype Corsiva",22),bg="black",fg="white")
        no_sub.pack()

        s=Button(win1,text="Search",bg="white",command=search_bk)
        s.pack()
    else :
        
        mycursor.execute("select * from books ;")
        book_det=mycursor.fetchall()


        for i in book_det:
            if ((book_name.lower() in i[0].lower()) and (int(edition_num)==int(i[3]))):
                book_n=i[0]
                book_author=i[4]
                edition_n=i[3]
                book_id_s=i[6]
            else :
                pass
        
        l1=Label(win1,text="Book Name -",font=("Times New Roman",22),bg="black",fg="white")
        l1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        l1_v=Label(win1,text=book_n,font=("Monotype Corsiva",22),bg="black",fg="green",padx=10)
        l1_v.grid(row=0,column=1,padx=10,pady=10)
        
        l2=Label(win1,text="Author -",font=("Times New Roman",22),bg="black",fg="white")
        l2.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        l2_v=Label(win1,text=book_author,font=("Monotype Corsiva",22),bg="black",fg="green",padx=10)
        l2_v.grid(row=1,column=1,padx=10,pady=10)
        
        l3=Label(win1,text="Edition Number -",font=("Times New Roman",22),bg="black",fg="white")
        l3.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        l3_v=Label(win1,text=edition_n,font=("Monotype Corsiva",22),bg="black",fg="green",padx=10)
        l3_v.grid(row=2,column=1,padx=10,pady=10)
        
        mycursor.execute("select * from new_arrivals;")
        n_ed=mycursor.fetchall()

        l=[]
        
        for ii in n_ed:
            l.append(ii[6])
            
        for j in l:
            if j==book_id_s:
                ed_a=Label(win1,text="New edition has arrived.",bg="black",fg="white",font=("Monotype corsiva",22))
                ed_a.grid(row=4,column=0,padx=10, pady=10)
                break
            else:
                pass
        
        s=Button(win1,text="Search",bg="white",font=("Times New Roman",18),command=search_bk,padx=10)
        s.grid(row=3,column=0,padx=20, pady=10)

        s1=Button(win1,text="Change Subsciptions",bg="white",font=("Times New Roman",18),command=change_subs,padx=10)
        s1.grid(row=3,column=1,padx=20, pady=10)
        
    win1.mainloop()

def new_arr():
    w=Tk()
    w.configure(bg="black")
    w.title("New arrivals")
    mydb=db.connect(host="localhost",user="root",passwd="12589",database="lib_management")
    mycursor=mydb.cursor()
    mycursor.execute("select * from new_arrivals")
    rec=mycursor.fetchall()
    if len(rec)==0:
        not_ar=Label(w, text="Sorry, but there are no new arrivals", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        not_ar.pack()
    else :
        headings=("Book Name", "Publisher Name", "Year of Publish", "Edition", "Author", "Status", "Book ID", "Book MRP")
        x=0
        for l in headings:
            h=Entry(w,width=22,bg="white",fg="blue")
            h.grid(row=0,column=x)
            h.insert(END,l)
            x+=1
        
        i=1
        for j in rec:
            for k in range(len(j)):
                e=Entry(w,width=22,bg="white",fg="black")
                e.grid(row=i,column=k)
                e.insert(END,j[k])
            i+=1
    w.mainloop()
	 
def main_menu_pat():
    global mm_pat
    
    mm_pat=Tk()
    mm_pat.geometry("350x500")
    mm_pat.configure(background="black")
    mm_pat.title("Library Management System - Patrons' Menu")
    
    head=Label(mm_pat, text="Main Menu...", font=("monotype corsiva", "25","underline"),bg="black" ,fg="red" , anchor="center", padx=100)
    head.grid(row=0,column=0,pady=20)

    new = Button(mm_pat, text="New Arrivals", padx=15, pady=5,command=new_arr)
    new.grid(row=1,column=0,pady=10)
    
    subs = Button(mm_pat, text="Subscriptions", padx=13, pady=5,command=subscr)
    subs.grid(row=2,column=0, pady=10)
    
    bookl = Button(mm_pat, text="Book list", padx=26, pady=5,command=book_l)
    bookl.grid(row=3, column=0, pady=10)
    
    search_b= Button(mm_pat, text="Search Books", padx=14, pady=5,command=search_bk)
    search_b.grid(row=4, column=0, pady=10)
    
    issued_b = Button(mm_pat, text="Issued Books", padx=15, pady=5,command=issued_bk)
    issued_b.grid(row=5, column=0, pady=10)
    
    reset_pass = Button(mm_pat, text="Reset Password", padx=9, pady=5,command=reset_password)
    reset_pass.grid(row=6, column=0, pady=10)

    ex = Button(mm_pat, text="Exit", padx=35, pady=5,command=mm_pat.destroy)
    ex.grid(row=7, column=0, pady=10)

    mm_pat.mainloop()

def main_menu_lib():
    global mm_lib
    
    mm_lib=Tk()
    mm_lib.geometry("570x450")
    mm_lib.configure(background="black")
    mm_lib.title("Library Management System - Librarians' Menu")
    
    head1=Label(mm_lib, text="Main Menu...", font=("monotype corsiva", "25","underline"),bg="black" ,fg="red" , anchor="center", padx=70)
    head1.grid(row=0,column=0,pady=10)

    bookl1 = Button(mm_lib, text="Book list", padx=36, pady=5,command=book_l)
    bookl1.grid(row=1, column=0, pady=10)

    new1= Button(mm_lib, text="New Arrivals", padx=25, pady=5,command=new_arr_lib)
    new1.grid(row=2,column=0,pady=10)

    search_b1= Button(mm_lib, text="Search Books", padx=24, pady=5,command=search_bk)
    search_b1.grid(row=3, column=0, pady=10)

    add_b= Button(mm_lib, text="Add New Books", padx=15, pady=5,command=add_bk)
    add_b.grid(row=4, column=0, pady=10)

    del_b= Button(mm_lib, text="Delete Books Details", padx=5, pady=5,command=del_bk)
    del_b.grid(row=5, column=0, pady=10)

    ed_b= Button(mm_lib, text="Return Books", padx=20, pady=5,command=ret_bk)
    ed_b.grid(row=6, column=0, pady=10)

    iss_b= Button(mm_lib, text="Issue New Books", padx=21, pady=5,command=issue_new_bk)
    iss_b.grid(row=1, column=1, pady=10)
    
    issued_b1= Button(mm_lib, text="Issued Books", padx=35, pady=5,command=issued_bk_list)
    issued_b1.grid(row=2, column=1, pady=10)
    
    edit_lib= Button(mm_lib, text="Edit Library Details/Rules", padx=3, pady=5,command=edit_libr)
    edit_lib.grid(row=3, column=1, pady=10)

    reset_pass_lib= Button(mm_lib, text="Reset Password", padx=27, pady=5,command=reset_password_lib)
    reset_pass_lib.grid(row=4, column=1, pady=10)

    ex1 = Button(mm_lib, text="Exit", padx=57, pady=5,command=mm_lib.destroy)
    ex1.grid(row=5, column=1, pady=10)

    mm.lib.mainloop()


def reg_lib() :
    reg_libs=Tk()
    reg_libs.geometry("800x400")
    reg_libs.title("Librarian Registration")
    reg_libs.configure(background="black")

    name_lab=Label(reg_libs, text="Enter your name - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    name_lab.grid(row=0, column=0, sticky=W)

    name_ent=ttk.Entry(reg_libs, width=46)
    name_ent.grid(row=0,column=1)
    name_ent.focus()
    
    gen_lab=Label(reg_libs, text="Enter your gender - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    gen_lab.grid(row=1, column=0, sticky=W)

    gen_ent=ttk.Combobox(reg_libs, width=42, state="readonly")
    gen_ent["values"]=["Male","Female","Other"]
    gen_ent.grid(row=1, column=1)

    pass_lab=Label(reg_libs, text="Enter a strong password - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    pass_lab.grid(row=2, column=0, sticky=W)

    pass_ent=ttk.Entry(reg_libs, width=46, show="*")
    pass_ent.grid(row=2,column=1)

    ver_code_lab=pass_lab=Label(reg_libs, text="Enter the verification code - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    ver_code_lab.grid(row=3, column=0, sticky=W)

    ver_code_ent=ttk.Entry(reg_libs, width=46, show="*")
    ver_code_ent.grid(row=3,column=1)

    emp_lab=pass_lab=Label(reg_libs, text="Enter your Employee Number - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    emp_lab.grid(row=4, column=0, sticky=W)

    emp_ent=ttk.Entry(reg_libs, width=46)
    emp_ent.grid(row=4,column=1)

    def actionrl():
        username=name_ent.get()
        gender=gen_ent.get()
        password=pass_ent.get()
        verif=ver_code_ent.get()
        emp=emp_ent.get()

        if verif !="148970" or username=="" or gender=="" or password=="" or verif=="" or emp=="":
            verif_err=Tk()
            verif_err.title("ERROR !!")
            ver_err=Frame(verif_err)
            ver_err.configure(background="black")
            ver_err.pack()

            if username=="" or gender=="" or password=="" or verif=="" or emp=="":
                 not_reg=Message(ver_err, text="Please fill all the details in the previous window !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                 not_reg.pack()

            elif verif!="148970":
                not_reg=Message(ver_err, text="You have entered an INCORRECT verification code", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                not_reg.pack()

                not_reg2=Message(ver_err, text="Please enter the correct code again", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                not_reg2.pack()
            else :
                 not_reg=Label(ver_err, text="Please fill all the details in the previous window !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                 not_reg.pack()
            ver_err.mainloop()
        else :
            datab=db.connect(host="localhost", user="root", password="12589")
            data_cur=datab.cursor()
            data_cur.execute("use lib_management;")
            data_cur.execute("select * from authorised_librarians;")
            data_tot=data_cur.fetchall()

            flag=1
            
            for i in data_tot:
                if i[3]==emp:
                    flag=0
                    break
                else :
                    flag=1
                    
            if flag==1:
                data_cur.execute("insert into authorised_librarians values(%s,%s,%s,%s);", (username, gender, password,emp))
                datab.commit()

                suc=Tk()
                suc.title("Information")
                success=Frame(suc)
                success.configure(background="black")
                success.pack()
                n=Label(success, text="You have successfully registered !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                n.pack(pady=10)
                n1=Button(success, text="Login Now !!", font=("Times New Roman",20), anchor="center", command=lambda:[log_lib(),exitm(success)], padx=20,pady=10)
                n1.pack(pady=20)

                suc.mainloop()

            else :
                err=Tk()
                err.title("ERROR !!")
                errs=Frame(err)
                errs.configure(background="black")
                errs.pack()
                not_reg=Label(errs, text="The user is already registered !!!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                not_reg.pack()

                not_reg_but=Button(errs, text="Close",font=("Times New Roman", 20),command=lambda:[exitm(errs)] ,padx=10)
                not_reg_but.pack(padx=20, pady=10)

                err.mainloop()
            

    submit_but=Button(reg_libs, text="SUBMIT", font=("Times New Roman",18), command=actionrl, padx=30, pady=10)
    submit_but.grid(row=5, column=0, padx= 100, pady=30)
    
    reg_libs.mainloop()

def reg_pat():
    reg_pat=Tk()
    reg_pat.geometry("800x400")
    reg_pat.title("Patron Registration")
    reg_pat.configure(background="black")

    name_lab=Label(reg_pat, text="Enter your name - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    name_lab.grid(row=0, column=0, sticky=W)

    name_ent=ttk.Entry(reg_pat, width=46)
    name_ent.grid(row=0,column=1)
    name_ent.focus()
    
    gen_lab=Label(reg_pat, text="Enter your gender - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    gen_lab.grid(row=1, column=0, sticky=W)

    gen_ent=ttk.Combobox(reg_pat, width=42, state="readonly")
    gen_ent["values"]=["Male","Female","Other"]
    gen_ent.grid(row=1, column=1)

    pass_lab=Label(reg_pat, text="Enter a strong password - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    pass_lab.grid(row=2, column=0, sticky=W)

    pass_ent=ttk.Entry(reg_pat, width=46, show="*")
    pass_ent.grid(row=2,column=1)

    des_lab=Label(reg_pat, text="You are a ? ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=70,pady=10)
    des_lab.grid(row=3, column=0)
    
    usertype=StringVar(reg_pat)
    des_rad_but=ttk.Radiobutton(reg_pat, text="Student", value="Student", variable=usertype)
    des_rad_but.grid(row=4, column=0)
    des_rad_but2=ttk.Radiobutton(reg_pat, text="Teacher", value="Teacher", variable=usertype)
    des_rad_but2.grid(row=4, column=1, sticky=W)

    id_lab=Label(reg_pat, text="Enter your ID number - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
    id_lab.grid(row=5, column=0, sticky=W)

    id_ent=ttk.Entry(reg_pat, width=16)
    id_ent.grid(row=5, column=1, padx=20)

    def actionrps():
        username=name_ent.get()
        gender=gen_ent.get()
        password=pass_ent.get()
        designation=usertype.get()
        id1=id_ent.get()
        
        if username=="" or gender=="" or password=="" or designation=="" or id1=="":
            err=Tk()
            err.title("ERROR !!")
            errs=Frame(err)
            errs.configure(background="black")
            errs.pack()
            not_reg=Message(errs, text="Please fill all the details in the previous window !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
            not_reg.pack()

            err.mainloop()

        else :
            datab=db.connect(host="localhost", user="root", password="12589")
            data_cur=datab.cursor()
            data_cur.execute("use lib_management;")

            data_cur.execute("select * from patrons;")
            data_tot=data_cur.fetchall()

            flag=1

            for i in data_tot:
                if i[3]==id1:
                    flag=0
                    break

                else :
                    flag=1

            if flag==1 :
                data_cur.execute("insert into patrons(name, designation, gender, password,id) values(%s, %s,%s,%s,%s);", (username, designation, gender, password,id1))
                datab.commit()
            
                suc=Tk()
                suc.title("Information")
                success=Frame(suc)
                success.configure(background="black")
                success.pack()
                n=Label(success, text="You have successfully registered !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                n.pack(pady=10)
                n1=Button(success, text="Login Now !!", font=("Times New Roman",20), anchor="center", command=lambda:[log_pat(),exitm(success)] , padx=20,pady=10)
                n1.pack(pady=20)

                suc.mainloop()

            else :
                err=Tk()
                err.title("ERROR !!")
                errs=Frame(err)
                errs.configure(background="black")
                errs.pack()
                not_reg=Message(errs, text="The user is already registered !!!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                not_reg.pack()

                not_reg_but=Button(errs, text="Close",font=("Times New Roman", 12),command=lambda:[exitm(errs)] ,padx=10)
                not_reg_but.pack(padx=20, pady=10)

                err.mainloop()
            
    submit_but=Button(reg_pat, text="SUBMIT", font=("Times New Roman",18), command=actionrps, padx=10)
    submit_but.grid(row=6, column=0, padx= 100, pady=10)

    reg_pat.mainloop()

def log_pat():
    
    datab=db.connect(host="localhost", user="root", password="12589")
    data_cur=datab.cursor()
    data_cur.execute("use lib_management;")
    data_cur.execute("select * from patrons;")
    datapr=data_cur.fetchall()
    if len(datapr)==0:
        log_pat_sc=Tk()
        log_pat_sc.title("ERROR !!")
        log_pat_scr=Frame(log_pat_sc)
        log_pat_scr.configure(background="black")
        log_pat_scr.pack()
        
        not_log=Message(log_pat_scr, text="There are no patrons registered !", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
        not_log.pack()

        not_log2=Message(log_pat_scr, text=" Please register a librarian first !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20, pady=10)
        not_log2.pack()

        log_pat_sc.mainloop()
    else :
        log_pats=Tk()
        log_pats.geometry("700x380")
        log_pats.title("Login")
        log_pats.configure(background="black")
        
        name_lab=Label(log_pats, text="Enter your name  - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        name_lab.grid(row=0, column=0, sticky=W)

        name_ent=ttk.Entry(log_pats, width=46)
        name_ent.grid(row=0,column=1)
        name_ent.focus()
    
        pass_lab=Label(log_pats, text="Enter your password - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        pass_lab.grid(row=1, column=0, sticky=W)

        pass_ent=ttk.Entry(log_pats, width=46, show="*")
        pass_ent.grid(row=1,column=1)

        des_lab=Label(log_pats, text="You are a ? ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        des_lab.grid(row=2, column=0, sticky=W)
        
        usertype=StringVar(log_pats)
        des_rad_but=ttk.Radiobutton(log_pats, text="Student", value="Student", variable=usertype)
        des_rad_but.grid(row=3, column=0)
        des_rad_but2=ttk.Radiobutton(log_pats, text="Teacher", value="Teacher", variable=usertype)
        des_rad_but2.grid(row=3, column=1, sticky=W)

        id_lab=Label(log_pats, text="Enter your ID number -", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        id_lab.grid(row=4, column=0, sticky=W)

        id_ent=ttk.Entry(log_pats, show="*" ,width=46)
        id_ent.grid(row=4,column=1)

        def actionll():
            global id_num
            
            username=name_ent.get()
            password=pass_ent.get()
            designation=usertype.get()
            id_num=id_ent.get()

            if username=="" or password=="" or designation=="" or id_num=="":
                err=Tk()
                err.title("ERROR !!")
                errs=Frame(err)
                errs.configure(background="black")
                errs.pack()
                not_log=Message(errs, text="Please fill all the details in the previous window !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                not_log.pack()

                err.mainloop()
            else :
                for i in datapr:
                    if i[0]==username :
                        if i[1]==designation:
                            if i[5]==id_num:
                                if i[4]==password:
                                    exitm(log_pats)
                                    main_menu_pat()
                                    break
                                
                                else :
                                    pass
                                
                            else :
                                err=Tk()
                                err.title("ERROR !!")
                                errs=Frame(err)
                                errs.configure(background="black")
                                errs.pack()

                                not_log=Message(errs, text="An error occurred while logging in, please see if you have entered the correct details", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                                not_log.pack()

                                err.mainloop()
                                break
                            
                        else :
                            err=Tk()
                            err.title("ERROR !!")
                            errs=Frame(err)
                            errs.configure(background="black")
                            errs.pack()

                            not_log=Message(errs, text="An error occurred while logging in, please see if you have entered the correct details", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                            not_log.pack()

                            err.mainloop()
                            break
                        
                    else :
                        err=Tk()
                        err.title("ERROR !!")
                        errs=Frame(err)
                        errs.configure(background="black")
                        errs.pack()

                        not_log=Message(errs, text="An error occurred while logging in, please see if you have entered the correct details", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                        not_log.pack()

                        err.mainloop()
                        break
                else :
                        err=Tk()
                        err.title("ERROR !!")
                        errs=Frame(err)
                        errs.configure(background="black")
                        errs.pack()
                            
                        not_log=Message(errs, text="An error occurred while logging in, please see if you have entered the correct details", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                        not_log.pack()
                        err.mainloop()
                            
        submit_but=Button(log_pats, text="SUBMIT", font=("Times New Roman",18), command=actionll, padx=30, pady=10)
        submit_but.grid(row=5, column=0, padx= 100, pady=30)

        log_pats.mainloop()


def log_lib():
    datab=db.connect(host="localhost", user="root", password="12589")
    data_cur=datab.cursor()
    data_cur.execute("use lib_management;")
    data_cur.execute("select * from authorised_librarians;")
    datapr=data_cur.fetchall()
    if len(datapr)==0:
        log_lib_sc=Tk()
        log_lib_sc.title("ERROR !!")
        log_lib_scr=Frame(log_lib_sc)
        log_lib_scr.configure(background="black")
        log_lib_scr.pack()
        
        not_log=Message(log_lib_scr, text="There are no librarians registered !", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
        not_log.pack()

        not_log2=Message(log_lib_scr, text=" Please register a librarian first !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20, pady=10)
        not_log2.pack()

        log_lib_sc.mainloop()
    else :
        log_libs=Tk()
        log_libs.geometry("700x300")
        log_libs.title("Login")
        log_libs.configure(background="black")
        
        name_lab=Label(log_libs, text="Enter your name  - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        name_lab.grid(row=0, column=0, sticky=W)

        name_ent=ttk.Entry(log_libs, width=46)
        name_ent.grid(row=0,column=1)
        name_ent.focus()
    
        pass_lab=Label(log_libs, text="Enter your password - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        pass_lab.grid(row=1, column=0, sticky=W)

        pass_ent=ttk.Entry(log_libs, width=46, show="*")
        pass_ent.grid(row=1,column=1)

        emp_id_lab=Label(log_libs, text="Enter your Employee Number - ", font=("Monotype Corsiva",22), bg="black", fg="white",  padx=20,pady=10)
        emp_id_lab.grid(row=2, column=0, sticky=W)

        emp_id_ent=ttk.Entry(log_libs, show="*", width=46)
        emp_id_ent.grid(row=2,column=1)

        def actionll():
            global emp_id
            
            username=name_ent.get()
            password=pass_ent.get()
            emp_id=emp_id_ent.get()

            if username=="" or password=="" or emp_id=="" :
                err=Tk()
                err.title("ERROR !!")
                errs=Frame(err)
                errs.configure(background="black")
                errs.pack()
                not_log=Message(errs, text="Please fill all the details in the previous window !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                not_log.pack()

                err.mainloop()
            else :
                for i in datapr:
                    if i[0]==username :
                        if i[3]==emp_id :
                            if i[2]==password:
                                main_menu_lib()
                                exitm(log_libs)
                                break
                            else :
                                pass
                        else :
                            err=Tk()
                            err.title("ERROR !!")
                            errs=Frame(err)
                            errs.configure(background="black")
                            errs.pack()

                            not_log=Message(errs, text="You have entered an incorrect employee number !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                            not_log.pack()

                            err.mainloop()
                            break

                    else :
                        err=Tk()
                        err.title("ERROR !!")
                        errs=Frame(err)
                        errs.configure(background="black")
                        errs.pack()

                        not_log=Message(errs, text="You have entered an incorrect username !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                        not_log.pack()

                        err.mainloop()
                        break
                else :
                    err=Tk()
                    err.title("ERROR !!")
                    errs=Frame(err)
                    errs.configure(background="black")
                    errs.pack()
                            
                    not_log=Message(errs, text="You have entered an incorrect password !!", font=("Times New Roman",28,"bold"), anchor="center", bg="black", fg="white",  padx=20,pady=20)
                    not_log.pack()

                    err.mainloop()
                      
        submit_but=Button(log_libs, text="SUBMIT", font=("Times New Roman",18), command=actionll, padx=30, pady=10)
        submit_but.grid(row=3, column=0, padx= 100, pady=30)

        log_libs.mainloop()

        
def register():
    reg_sc=Tk()
    reg_sc.title("Register")
    reg_scr=Frame(reg_sc)
    reg_scr.pack()
    reg_scr.configure(background="black")
    head_reg=Label(reg_scr, text="You are registering as ?", font=("Monotype Corsiva",28), anchor="center", bg="black", fg="white",  padx=30,pady=30)
    head_reg.pack()

    libr_but_reg=Button(reg_scr, text="Librarian", font=("Times New Roman",20), padx=10, pady=10, command=reg_lib)
    libr_but_reg.pack(side=LEFT, padx=40, pady=10)

    patr_but_reg=Button(reg_scr, text="Patron", font=("Times New Roman",20), padx=10, pady=10, command=reg_pat)
    patr_but_reg.pack(side=RIGHT, padx=40, pady=10)

    reg_sc.mainloop()

def login():
    login_sc=Tk()
    login_sc.title("Login Screen")
    login_scr=Frame(login_sc)
    login_scr.pack()
    login_scr.configure(background="black")
    head_log=Label(login_scr, text="You are logging in as ?", font=("Monotype Corsiva",28), anchor="center", bg="black", fg="white",  padx=30,pady=30)
    head_log.pack()

    libr_but=Button(login_scr, text="Librarian", font=("Times New Roman",20), padx=10, pady=10, command=log_lib)
    libr_but.pack(side=LEFT, padx=50, pady=10)

    patr_but=Button(login_scr, text="Patron", font=("Times New Roman",20), padx=10, pady=10, command=log_pat)
    patr_but.pack(side=RIGHT, padx=50, pady=10)

    login_sc.mainloop()

def main_screen():
    main=Tk()
    main.title("Library Management System")
    mains=Frame(main)
    mains.pack()
    mains.configure(background="black")
    head_mains=Label(mains, text="Welcome to the library management system", font=("Monotype Corsiva",32, "underline"), anchor="center", bg="black", fg="white",  padx=30,pady=30)
    head_mains.pack()

    log_but=Button(mains, text="Login", font=("Times New Roman",20), padx=10, pady=10, command=login)
    log_but.pack(side=LEFT,padx=90, pady=20)

    regist_but=Button(mains, text= "Register", font=("Times New Roman",20), padx=10, pady=10, command=register)
    regist_but.pack(side=LEFT, padx=10,pady=20)

    exit_but=Button(mains, text="Exit", font=("Times New Roman",20), padx=10, pady=10, command=mains.destroy)
    exit_but.pack(side=LEFT, padx= 90,pady=20)

    main.mainloop()
main_screen()
