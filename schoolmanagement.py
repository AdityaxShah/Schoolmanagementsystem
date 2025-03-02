import mysql.connector as mysql                                
# making connecting mysql with python
from prettytable import PrettyTable                            
# used to design the table and arrange data 
cobj=mysql.connect(host='localhost', user='root', passwd='1234', database='vak')      # opening mysql and using database

def insert():                                                 
# code for input 
    while True:
        xyz=0
        try:
            sname=input("\nEnter Student Name : ")
            admno=int(input("Enter Admission No : "))
            cursor = cobj.cursor()                                
# taking cursor to mysql
            sql = "SELECT * FROM student;"
            cursor.execute(sql)
            results = cursor.fetchall()                           
# taking all data in results as list containing tuple
            for c in results:
                if c[1]==admno:                                   
                    xyz=1
            if xyz==1:
                print("This admssion no already exist.\nRe-Enter the data.\n")
                continue
            else :
                dob=input("Enter Date of Birth(yyyy-mm-dd): ")
                clas=int(input("Enter class for Admission: "))
                house=input("Enter House: ")
                cursor = cobj.cursor()
                sql="INSERT INTO student(sname,admno,dob,class,house)VALUES('%s',%s,'%s','%s','%s');"%(sname,admno,dob,clas,house)  #giving valuse to place holders
                cursor.execute(sql)                              
# execute the query in sql
                cobj.commit()                                    
# changes in mysql
                break
        except:
                print("Unknown error occured...\nRe-Enter the data.\n")

def display():                                                    
# Code for viewing all data
    try:
        cursor = cobj.cursor()
        sql = "SELECT * FROM student;"
        cursor.execute(sql)
        results = cursor.fetchall()                              
# taking all data in results as list containing tuple
        x=PrettyTable()                                          
# using pretty table
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            clas=c[3]
            house=c[4]
            x.field_names = ["Student name", "Admission no", "Date of Birth", "Class",'House']    # column name in pretty table
            x.add_row([sname,admno ,dob ,clas, house ])          
# adding rows in pretty table
        print(x)                                                
# printing pretty table with data
    except:
        print ("Error: unable to fetch data")

def update():                                                    
# Code for updatigthe data
    try:
        cursor=cobj.cursor()
        while True:
            print('''\n+--------------------------------------+
|1.STUDENT NAME                        |
+--------------------------------------+
|2.ADMISSION NO.                       |
+--------------------------------------+
|3.DATE OF BIRTH                       |
+--------------------------------------+
|4.CLASS                               |
+--------------------------------------+
|5.HOUSE                               |
+--------------------------------------+''')
            x=int(input("Enter the serial no. of the data you want to update:"))
            if x in (1,3,4,5):
                y=input("Enter the Admission no. of the student:")
            elif x==2:
                y=input("Enter the Student Name :")
            #For the inputs     
            if x == 1:
                z=input ("Enter the New Student Name:")
                sql = "Update student set sname='{}' where admno={}".format(z,y)
                cursor.execute(sql)
                cobj.commit()
            elif x==2:
                z=int(input("Enter the New Admission no.:"))
                sql = "Update student set admo={} where sname={}".format(z,y)
                cursor.execute(sql)
                cobj.commit()
            elif x==3:
                z=input("Enter the New Date of Birth:")
                sql = "Update student set dob='{}' where admno={}".format(z,y)
                cursor.execute(sql)
                cobj.commit()
            elif x==4:
                z=int(input("Enter the New Class:"))
                sql = "Update student set class={} where admno={}".format(z,y)
                cursor.execute(sql)
                cobj.commit()
            elif x==5:
                z=input("Enter the New House:")
                sql = "Update student set house='{}' where admno={}".format(z,y)
                cursor.execute(sql)
                cobj.commit()
            else:
                print("Enter the correct choice.")
                c=input("Do you want to enter again (y/n)")
                if c in ('Y','y'):
                    continue
                elif c in ('N','n'):
                    break
                else:
                    print("Enter the correct choice...")
            c=input("Do you want to enter again (y/n):")
            if c in ('Y','y'):
                continue
            elif c in ('N','n'):
                break
            else:
                print("invalid choice...")
                print("Exiting the Update...")
                break
            
    except:
        print("UNKNOWN ERROR OCCURED")
        
def search():                                           
# Code for searching the Data
    flag=0
    while True:
        try:
            a=int(input("\nEnter the Admission no of the Student you want to search:"))
            cursor = cobj.cursor()
            sql = "SELECT * FROM student;"
            cursor.execute(sql)
            results = cursor.fetchall()                 
# taking all data in results as list containing tuple
            x=PrettyTable()                             
# using pretty table
            for c in results:
                if c[1]== a:
                    x.field_names = ["Student name", "Admission no", "Date of Birth", "Class",'House']      
# column name in pretty table
                    x.add_row([c[0],c[1],c[2],c[3],c[4]])                         # adding rows in pretty table
                    print(x,"\n")                                                 # printing pretty table with data
                else:
                    flag=flag+1
            if flag!=4:
                print("No data found with admission no.",a,".")
            c=input('Do you want to Search again (y/n):')
            if c in ('Y','y'):
                continue
            elif c in ('N','n'):
                break
            else :
                print("Invalid choice.")
                print("Exiting the search.")
                break
        except:
            print ("Error: Unable to Fetch Data...")
            c=input('Do you want to enter again (y/n):')
            if c in ('Y','y'):
                continue
            elif c in ('N','n'):
                break
            else :
                print("Invalid choice.")
                print("Exiting the search.")
                break
def delete():                                                  
# code for deleting the data
    while True:
        try:
            a=int(input("\nEnter the Admission no of the Student you want to issue TC:"))
            cursor = cobj.cursor()
            sql = "SELECT * FROM student;"
            cursor.execute(sql)
            results = cursor.fetchall()                        
# taking all data in results as list containing tuple
            for c in results:
                if c[1]==a:
                    print('Issue TC will permanently delete the Data of that student.')
                    sql="delete from student where admno={}".format(a)
                    cursor.execute(sql)                        
# execute the query 
                    cobj.commit()                              
# to make changes in mysql 
                    print("Your record has been deleted.\n")
                    break
            else:
                print("No data with this admission no found.")
            c=input('Do you want to Delete Another Data(y/n):')
            if c in ('Y','y'):
                continue
            elif c in ('N','n'):
                break
            else:
                print("Invalid choice.")
                break
        except:
            print("Error...Data not found.")
            c=input('Do you want to enter again (y/n):')
            if c in ('Y','y'):
                continue
            elif c in ('N','n'):
                break
            else:
                print("Invalid choice.")
                print("Exiting the Issue TC")
                break
def stumanage():                                             
# Main code for the management
    print('''\n+--------------------------------------+
| WELCOME TO STUDENT MANAGEMENT SYSTEM |
+--------------------------------------+''')
    while True:
        print('''\n+--------------------------------------+
|A.NEW ADMISSION                       |
+--------------------------------------+
|B.UPDATE STUDENT DETAILS              |
+--------------------------------------+
|C.SEARCH THE DETAILS                  |
+--------------------------------------+
|D.ISSUE TC                            |
+--------------------------------------+
|E.SEE ALL THE DATA                    |
+--------------------------------------+
|F.EXIT                                |
+--------------------------------------+''')
        zy=0
        i=input("Enter your choice (A-F) : ")
        if i in('a','A'):
            insert()
            k=input("DO you want to see Modified Details (y/n):")
            if k in ('Y','y'):
                print('\nModified details are..\n')
                display()
            else:
                print("Exiting New Admission.")
                          
        elif i in ('b','B'):
            print("\nDetails for Updating data :\n")
            update()
            k=input("DO you want to see Modified Details (y/n):")
            if k in ('Y','y'):
                print('\nModified details are..\n')
                display()
            else :
                print("Exiting Update Details")
            
        elif i in('c','C'):
            search()
        elif i in ('d','D'):
            delete()
            k=input("DO you want to see Modified Details (y/n):")
            if k in ('Y','y'):
                print('\nModified details are..\n')
                display()
        elif i in ('e','E'):
            print('Details are as follows:')
            display()
        elif i in ('F','f'):
            print('''\n                   (｡◕‿◕｡)...THANK YOU...(｡◕‿◕｡)\n''')
            break                                              
# break the while loop
        else:
            print('Enter correct choice...!!')
            while zy==0:
                c=input("Do you want to enter again (y/n)")
                if c in ('Y','y'):
                    zy=1
                elif c in ('N','n'):
                    zy=2
                    print('''\n                   (｡◕‿◕｡)...THANK YOU...(｡◕‿◕｡)\n''')
                else:
                    print("Enter the correct choice...")
                    zy=0
        if zy==1:
            continue                                          
# restart the while loop from starting
        if zy==2:
            break

stumanage()                         #MAIN PROGRAM
cobj.close()
