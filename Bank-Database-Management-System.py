import pymysql
from datetime import datetime

print("Welcome To Wellish Farmgo Bank Database. This Bank Database provides an easier and less")
print("Cumbersome way for Account Management for all our Customers and Employees")

print()
print()
print("To enter into the database type 'WellishFarmgo' in the Enter DataBase Name Column")
print()
while True:
    db1=input("Enter DataBase Name:")
    if db1=="WellishFarmgo" or db1=="WELLISHFARMGO" or db1=="wellishfarmgo" or db1=="Wellishfarmgo":
        break
pwd=input("Enter your SQL password")
db=pymysql.connect(host="localhost",user="root",password=pwd)
cur=db.cursor()
cur.execute("CREATE DATABASE if not exists "+db1)
print("database created")


#Connecting to a database at backend
db=pymysql.connect(host="localhost",user="root",password=pwd,db=db1)
print("connected successfully")
cur=db.cursor()
cur.execute("show databases")
print(cur.fetchall())
print()
print()
print()


#Creating a table
numrow=cur.execute('Create table if not exists EmpTable ( \
                                      EmpID int(4) primary key, \
                                      EmpName varchar(20) , \
                                      JoinDate date ) ; ' )
print("table created")






#Create Customer Record Table
numrow=cur.execute('Create table if not exists CusTable ( \
                                     CustID int(4) primary key, \
                                     CustName varchar(30) , \
                                     CustJoin date ) ; ' )
print("table created")




#Create Customer Account Table
numrow=cur.execute('Create table if not exists AccTable ( \
                                     AccID int(4) primary key, \
                                     AccName varchar(30) , \
                                     Balance int , \
                                     LastTransDate date ) ; ')


#Create Transaction Table
numrow=cur.execute('Create table if not exists Transact ( \
                                      AccID int(4) primary key , \
                                      AccName varchar (30) , \
                                      WithdrawalAmount int , \
                                      DepositedAmount int(10), \
                                      DateOfTransaction date ) ; ')
                                     








#Menu




#Adding a record in Employee Table
def add():
    l2=[]
    print()
    print()
    print("What is an Employee ID?")
    print()
    print("ø Employee ID is an unique and mandatory code used for Security Purpose")
    print("ø Employee ID must lie between 100 and 999")
    print("ø Employee ID must be unique i.e. no other employee should have same Employee ID")
    print()
    while True:
        a=int(input("Enter the New Employee's ID"))
        query=cur.execute("Select EmpID from EmpTable ; ")
        plus=cur.fetchall()
        v=0
        for k in plus:
            if k[v]==a:
                print("This ID Exists Already")
                break
        else:
            break
    print()
    b=input("Enter the New Employee's Name")
    c=input("Enter the Date of Joining (YYYY-MM-DD)")
    q="insert into EmpTable values (%d,'%s','%s' )"%(a,b,c)
    cur.execute(q)
    db.commit()
    print("Record of",b,"Inserted")




    


#Add a value in Customer Record & Account Table
def add1():
    l1=[]
    print()
    print()
    print("What is an Customer ID?")
    print()
    print("ø Customer ID is an unique and mandatory code used for Security Purpose")
    print("ø Customer ID must lie between 1000 and 9999")
    print("ø Customer ID must be unique i.e. no other employee should have same Employee ID")
    print()
    while True:
        a=int(input("Enter the New Customer ID"))
        query=cur.execute("Select CustID from CusTable ; ")
        plus=cur.fetchall()
        v=0
        for k in plus:
            if k[v]==a:
                print("This ID Exists Already")
                break
        else:
            break
    print()
    l=input("Enter Name of the Customer:")
    m=int(input("Enter the Minimum Amount you want to deposit in your account to create it:"))
    if m<1000:
        print ("To Create an Account, You must deposit more than $1000")
    if m>1000000:
        print("This Value is exceeding the Maximum limit of creating an Account")
    n=datetime.today().strftime('%Y-%m-%d')
    q="insert into CusTable values (%d,'%s','%s')"%(a,l,n)
    cur.execute(q)
    db.commit()
    w="insert into AccTable values (%d,'%s',%d,'%s')"%(a,l,m,n)
    cur.execute(w)
    db.commit()
    print("Account of",l,"Created")






#Add a value in Transaction table/ Make a Transaction
def add2():
    o=int(input("Enter Your Customer ID"))
    rname="Select CustName from CusTable where CustID=%d; "%o
    cur.execute(rname)
    rna=cur.fetchone()
    n=""
    for r in rna :
        if n.isalpha() or n.isspace():
            r=r+n
    n=datetime.today().strftime('%Y-%m-%d')
    a=0
    print()
    if o<1000:
        print()
        print("Invalid Customer ID")
    p=input("To Deposit type D, To Withdraw type W")
    if p=="D" or p=="d":
        q=int(input("Enter the amount you want to deposit:"))
        query="Insert into Transact values (%d,'%s',%d,%d,'%s')"%(o,r,a,q,n)
        cur.execute(query)
        db.commit()
        query2="update AccTable set Balance=Balance+(%d) where AccID=%d; "%(q,o)
        cur.execute(query2)
        db.commit()
        query4="update AccTable set LastTransDate='%s' where AccID=%d"%(n,o)
        cur.execute(query4)
        db.commit()
        print(q,"$ Deposited into",r,"'s Account")
    if p=="W" or p=="w":
        t=int(input("Enter the amount you want to withdraw:"))
        if t>50000:
            print("The amount entered is more than the daily limit of a single customer!!!")
            t=int(input("Enter a Valid amount (not more than 50000"))
        query="insert into transact values (%d,'%s',%d,%d,'%s')"%(o,r,t,a,n)
        cur.execute(query)
        db.commit()
        query3="update AccTable set Balance=Balance-(%d) where AccID=%d; "%(t,o)
        cur.execute(query3)
        db.commit()
        query5="update AccTable set LastTransDate='%s' where AccID=%d"%(n,o)
        cur.execute(query5)
        db.commit()
        print(t,"$ Withdrawn from",r,"'s Account")
        
    






    


#Modification of a record in the Employees Table
def modify( ):
    d=int(input("Enter Employee ID whose Name and Date of Joining are to be modified:"))
    g=int(input("What do you want to modify? 1.Employee Name 2.Date of Joining (Write 1 or 2)"))
    if g==1:
        e=input("Enter new name:")
        query="update EmpTable set EmpName='%s' where EmpID=%d; "%(e,d)
    if g==2:
        f=input("Enter Changed Date of Joining (YYYY-MM-DD)")
        query="update EmpTable set JoinDate='%s' where EmpID=%d; "%(f,d)
    cur.execute(query)
    db.commit()
    print("Updated")






#Modification of a record in the Customer Record Table
def modify1( ):
    d=int(input("Enter Customer ID whose Name and Date of Account Creation are to be modified:"))
    print()
    g=int(input("What do you want to modify? 1.Customer Name 2.Date of Account Creation (Write 1 or 2)"))
    print()
    if g==1:
        e=input("Enter New Name:")
        query="Update CusTable set CustName='%s' where CustID=%d; "%(e,d)
        query2="Update AccTable set AccName='%s' where AccID=%d; "%(e,d)
        query3="Update Transact set AccName='%s' where AccID=%d; "%(e,d)
        cur.execute(query)
        cur.execute(query2)
        cur.execute(query3)
        db.commit()
        
    if g==2:
        f=input("Enter Changed Date of Joining (YYYY-MM-DD)")
        query="update CusTable set CustJoinDate='%s' where CustID=%d; "%(f,d)
        cur.execute(query)
        cur.execute(query2)
        cur.execute(query3)
        db.commit()
    print("Updated")








#Deletion of record in Employee Table
def dele():
    h=int(input("Enter Employee's ID whose record has to be deleted:"))
    query="delete from EmpTable where EmpID=%d"%h
    cur.execute(query)
    db.commit()
    print("Record Deleted")
    


#Deletion of record in Customer Record table
def dele1():
    h=int(input("Enter Customer's ID whose record has to be deleted:"))
    query="delete from CusTable where CustID=%d"%h
    cur.execute(query)
    db.commit()
    print("Record Deleted Successfully")






# Search the Employee Record in the employee table
def view():
    i=int(input("Enter Employee ID to be searched:"))
    query=cur.execute("Select * from EmpTable where EmpID=%d; "%i)
    pus=cur.fetchall()
    d=0
    for k in pus:
        if k[d]==i:
            print("Record Found",k)
            break
    else:
        print("Record Not Found")






# Search the record in Customer Table Records
def view1(): 
    i=int(input("Enter Customer ID to be searched:"))
    query=cur.execute("Select * from CusTable where CustID=%d; "%i)
    stu=cur.fetchall()
    c=0
    for k in stu:
        if k[c]==i:
            print("Record Found",k)
            break
    else:
        print("Record Not Found")




#View Balance
def view2():
    i=int(input("Enter Customer ID whose balance you want to see!"))
    query=cur.execute("Select Balance from AccTable where AccID=%d; "%i)
    m=cur.fetchall()
    print (m)


#View Account Detail
def view3():
    i=int(input("Enter Customer ID whose balance you want to see!"))
    query=cur.execute("Select * from AccTable where AccID=%d; "%i)
    x=cur.fetchall()
    print("AccID\t    AccountName\t    Balance    LastDateofTrans    ")
    for row in x:
        print("{}\t    {}\t    {}\t    {}\t    " . format (row[0],row[1],row[2],row[3]))
        #{ } substitutes values of row[ ]
        




#View Transaction History
def view4():
    i=int(input("Enter Customer ID whose Transaction History you want to see:"))
    query=cur.execute("Select * from Transact where AccID=%d; "%i)
    m=cur.fetchall()
    print(m)


#View all records of the Customer
def allrecords():
    query=cur.execute("Select * from AccTable; ")
    x=cur.fetchall()
    print("AccID\t     AccountName\t    Balance    LastDateofTrans    ")
    for row in x:
        print("{}\t    {}\t    {}\t    {}\t    " . format (row[0],row[1],row[2],row[3]))
        #{ } substitutes values of row[ ]
        


#View Debited Amount
def viewdebited():
    a=int(input("Enter Customer ID to Calculate Debited Amount"))
    query="Select sum(WithdrawalAmount) from Transact where AccID=%d; "%a
    cur.execute(query)
    m=cur.fetchall()
    print(m)




#View Credited Amount
def viewcredited():
    a=int(input("Enter Customer ID to Calculate Total Credited Amount;"))
    query="Select sum(DepositedAmount) from Transact where AccID=%d; "%a
    cur.execute(query)
    m=cur.fetchall()
    print(m)










    






#Execution of all the functions!!


while True:
    print("What do you want to do?")
    print()
    print("A) LOGIN AS EMPLOYEE")
    print("B) ACCESS CUSTOMER RECORDS")
    print("C) ACCESS CUSTOMER ACCOUNTS DATA")
    print("D) MAKE A TRANSACTION")
    print("E) LOG OUT OF WELLS FARGO DATABASE")
    print()
    print("Write A/B/C/D/E for your choice")
    print()
    print()
    z=input("Enter your choice")
    print()




    
    if z=="A" or z=="a":
        while True:
           print()
           print("Make your Choice:")
           print("1. ADD THE DETAILS OF A NEW EMPLOYEE")
           print("2. MODIFY THE DETAILS OF AN EXISTING EMPLOYEE")
           print("3. DELETE THE RECORDS OF AN EMPLOYEE")
           print("4. SEARCH THE DETAILS OF AN EMPLOYEE")
           print("5. VIEW THE DETAILS OF ALL THE CUSTOMERS")
           print("6. LOG OUT OF THE EMPLOYEE TABLE")
           print()
           print("Write 1/2/3/4/5/6 for your choice!")
           print()
           print()
           j=int(input("Enter Your Choice:"))
           if j==1:
               add()
           if j==2:
               modify()
           if j==3:
               dele()
           if j==4:
               view()
           if j==5:
               allrecords()
           if j==6:
               break
       




    if z=="B" or z=="b":
        while True:
            print()
            print("1. CREATE A NEW ACCOUNT AS A NEW USER)")
            print("2. MODIFY THE ACCOUNT OF THE USER")
            print("3. DELETE THE USER'S ACCOUNT")
            print("4. SEARCH THE DETAILS OF THE CUSTOMER")
            print("5. VIEW DETAILS OF ALL CUSTOMERS")
            print("6.LOG OUT OF THE CUSTOMER TABLE")
            print("Write 1/2/3/4/5/6 for your choice!")
            print()
            print()
            j=int(input("Enter your Choice"))
            if j==1:
                 add1()
            if j==2:
                modify1()
            if j==3:
                dele1()
            if j==4:
                view1()
            if j==5:
                allrecords()
            if j==6:
                break






    if z=="C" or z=="c":
        while True:
            print()
            print("1. CHECK BALANCE")
            print("2. VIEW ACCOUNT DETAILS")
            print("3. LOG OUT OF THE CUSTOMER ACCOUNTS TABLE")
            print("Write 1/2/3 for your choice!")
            print()
            print("To add ,modify or delete the account Go to Customer Records Table")
            print()
            print()
            j=int(input("Enter your Choice:"))
            if j==1:
                view2()
            if j==2:
                view3()
            if j==3:
                break


            
    if z=="D" or z=="d":
        while True:
            print()
            print("1. MAKE A TRANSACTION")
            print("2. VIEW TRANSACTION HISTORY")
            print("3. VIEW TOTAL DEBITED AMOUNT")
            print("4. VIEW TOTAL CREDITED AMOUNT")
            print("5. LOG OUT OF THE TRANSACTION TABLE")
            print("Write 1/2/3/4/5 for your choice")
            print()
            print()
            j=int(input("Enter your Choice:"))
            if j==1:
                add2()
            if j==2:
                view4()
            if j==3:
                viewdebited()
            if j==4:
                viewcredited()
            if j==5:
                break
    if z=="E" or z=="e":
        print("******Thanks for using Wells Fargo Bank! Have a Nice Day******")
        break


                
                


          
                        




                
                


          
                